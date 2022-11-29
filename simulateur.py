import numpy.random as np
from random import random
class Echeancier(list):
    def __init__(self, *args, **kwargs):
        super(Echeancier, self).__init__(*args, **kwargs)

    # Override de la method append pour ajouter un evenement
    def append(self, evenement):
        super(Echeancier, self).append(evenement)
        
        # On trie la liste par date (1er element du tuple)
        self.sort(key=lambda x: x[1])
        

    def ajouter(self, date, evenement):
        self.append((date, evenement))

    def prochain(self):
        return self.pop(0)

    def __str__(self):
        return str(self)


class Simulateur:

    def __init__(self, duree):
        self.duree_simulation = duree
        self.schedule = Echeancier()
        

        # on initialise les variables une première fois pour qu'on puisse y avoir accès après
        # elle seront réinitialisées dans la méthode DebutSimu
        self.nbBus = 0
        self.nbBusRepair = 0
        self.Q1 = 0
        self.Q2 = 0
        self.B1 = True
        self.B2 = 0

        self.AireQ1 = 0
        self.AireQ2 = 0
        self.AireB2 = 0

    
    # Arrivee d'un bus
    def arriveeBus(self):
        self.nbBus += 1

        # Ajout d'un évenement d'arrivée dans la file de controle
        self.schedule.append((self.arriveFileControle, self.heureSysteme))

        # Ajout d'un nouvel evenement suivant la loi exponentielle de paramètre 0.5
        self.schedule.append((self.arriveeBus,self.heureSysteme + np.exponential((3/4) * 60))) # 120min = 2h
            
    # arrivé bus dans la file de controle
    def arriveFileControle(self):
        self.Q1 = self.Q1 + 1
        if self.B1 == True:
            self.schedule.append((self.accesPosteControle, self.heureSysteme))
        
    # accès guichet controle
    def accesPosteControle(self):
        self.Q1 -= 1
        self.B1 = False
        self.schedule.append((self.departPosteControl, self.heureSysteme + np.uniform(15, 65)))

    def departPosteControl(self):
        
        self.B1 = True
        if self.Q1 > 0:
            self.schedule.append((self.accesPosteControle, self.heureSysteme))
        if random() < 0.3:
            self.schedule.append((self.arriveFileReparation, self.heureSysteme))

    # accès guichet réparation
    def arriveFileReparation(self):
        self.Q2 += 1
        self.nbBusRepair += 1
        if self.B2 < 2:
            self.schedule.append((self.accesPosteReparation, self.heureSysteme))

    # accès guichet réparation
    def accesPosteReparation(self):
        
        self.Q2 -= 1
        self.B2 += 1
        self.schedule.append((self.departReparation, self.heureSysteme + np.uniform(168, 330)))

    def departReparation(self):

        self.B2 -= 1
        if self.Q2 > 0:
            self.schedule.append((self.accesPosteReparation, self.heureSysteme))

    def DebutSimu(self):
        self.nbBus = 0
        self.nbBusRepair = 0
        self.Q1 = 0
        self.Q2 = 0
        self.B1 = True
        self.B2 = 0

        self.AireQ1 = 0
        self.AireQ2 = 0
        self.AireB2 = 0
        
        self.schedule.append((self.arriveeBus, self.heureSysteme + np.exponential((3/4) * 60))) # 120min = 2h
        self.schedule.append((self.FinSimulation, self.duree_simulation))

    def FinSimulation(self):

        # TODO : Changer variables
        # TODO : Ajouter variable pour nb d'heures de simulation

        self.schedule.clear()
        if (self.nbBus > 0):
            print("Temps d'attention moyen avant contrôle : ", (self.AireQ1 / self.nbBus) / 60)
        if (self.nbBusRepair > 0):
            print("Temps d'attention moyen avant réparation : ", (self.AireQ2 / self.nbBusRepair) / 60)
        
        print("Temps d'utilisation moyen du centre de réparation : ", self.AireB2 / (2 * self.duree_simulation))

    def MAJAires(self, nextDate):
        self.AireQ1 += self.Q1 * (nextDate - self.heureSysteme)
        self.AireQ2 += self.Q2 * (nextDate - self.heureSysteme)
        self.AireB2 += self.B2 * (nextDate - self.heureSysteme)

    def run(self):
        # init heure système
        self.heureSysteme = 0

        # Ajout de l'évènement de début de simulation
        self.schedule.append((self.DebutSimu, self.heureSysteme))

        # Tant qu'il y a des evenements dans l'echeancier
        while self.schedule != []:

            # Extraction du prochain evenement
            nextEvent = self.schedule.prochain()

            # Mise à jour des aires 
            self.MAJAires(nextEvent[1])

            # Mise à jour de l'heure système
            self.heureSysteme = nextEvent[1]

            print("Heure système : ", self.heureSysteme / 60, "h")
            print("Evenement : ", nextEvent[0].__name__)

            # Execution de l'evenement
            nextEvent[0]()

        # Fin de la simulation

if __name__ == '__main__': 
    dureesSimulation = [40, 80, 160, 240]
    for duree in dureesSimulation:
        print("Simulation de durée : ", duree)
        simulateur = Simulateur(duree * 60)
        simulateur.run()
        print("Fin de la simulation : ", duree)