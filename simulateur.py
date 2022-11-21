# dureesSimulation = [40, 80, 160, 240]

'''for duree in dureesSimulation:
    init(duree)

    while echeancier:
        # On recupere le prochain evenement
        evenement = echeancier.pop(0)
        dateSysteme = evenement[0]
        # On execute l'evenement
        evenement[1]()

    print("Fin de la simulation apres " + str(duree) + " heures")'''

import numpy.random as np


class Echeancier(list):
    def __init__(self, *args, **kwargs):
        super(Echeancier, self).__init__(*args, **kwargs)

    # Override de la method append pour ajouter un evenement
    def append(self, evenement):
        super(Echeancier, self).append(evenement)

        # On trie la liste par date (1er element du tuple)
        self.sort(key=lambda x: x[0])
        

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
        self.DebutSimu()
    
    # Arrivee d'un bus
    def arriveeBus(self):
        self.nbBus += 1

        # Ajout d'un évenement d'arrivée dans la file de controle
        self.schedule.append((self.arriveFileControle, self.heureSysteme))

        # Ajout d'un nouvel evenement suivant la loi exponentielle de paramètre 0.5
        self.schedule.append((self.arriveeBus,self.heureSysteme + np.exponential((4/3)) * 120)) # 120min = 2h
            
    # arrivé bus dans la file de controle
    def arriveFileControle(self):
        self.Q1 = self.Q1 + 1
        if self.Q1 == 1:
            self.schedule.append((self.accesPosteControle, self.heureSysteme))
        
    # accès guichet controle
    def accesPosteControle(self):
        self.Q1 -= 1
        self.B1 = False
        self.schedule.append((self.departPosteControl, self.heureSysteme + np.uniform(0.25, 13/12)))

    def departPosteControl(self):
        
        self.B1 = True
        if self.Q1 > 0:
            # Ici mettre date à l'heure précis
            self.schedule.append((self.accesPosteControle, self.heureSysteme))
        if np.uniform(0, 1) < 0.3:

            # Ici mettre date à l'heure précis
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
        self.heureSysteme = 0
        self.nbBus = 0
        self.nbBusRepair = 0
        self.Q1 = 0
        self.Q2 = 0
        self.B1 = True
        self.B2 = 0

        self.AireQ1 = 0
        self.AireQ2 = 0
        self.AireB2 = 0
        
        self.schedule.append((self.arriveesBus, self.heureSysteme + np.exponential((4/3)) * 120)) # 120min = 2h
        self.schedule.append((self.FinSimulation, self.duree_simulation))

    def FinSimulation(self):

        # TODO : Vider l'échéancier
        # TODO : Changer variables
        # TODO : Ajouter variable pour nb d'heures de simulation

        print("Temps d'attention moyen avant contrôle : ", self.AireQ1 / self.nbBus)
        print("Temps d'attention moyen avant réparation : ", self.AireQ2 / self.nbBusRepair)
        print("Temps d'utilisation moyen du centre de réparation : ", self.AireB2 / (2 * self.duree))

        

