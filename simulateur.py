import numpy as np
import threading
from random import random
import matplotlib.pyplot as plt
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

    def __init__(self, numSimu, nbBusAvantStop):
        self.numSimu = numSimu
        self.schedule = Echeancier()
        self.nbBusAvantStop = nbBusAvantStop

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

        self.nbBusPointControle = 0
        self.listeTempsAttenteControle = []

    
    # Arrivee d'un bus
    def arriveeBus(self):

        # On ajoute l'heure système à la liste des temps d'attente
        self.listeTempsAttenteControle.append(self.heureSysteme)

        self.nbBus += 1

        # Ajout d'un évenement d'arrivée dans la file de controle
        self.schedule.append((self.arriveFileControle, self.heureSysteme))

        # Ajout d'un nouvel evenement suivant la loi exponentielle de paramètre 0.5
        self.schedule.append((self.arriveeBus,self.heureSysteme + np.random.exponential((3/4) * 60))) # 120min = 2h
            
    # arrivé bus dans la file de controle
    def arriveFileControle(self):
        self.Q1 = self.Q1 + 1
        if self.B1 == True:
            self.schedule.append((self.accesPosteControle, self.heureSysteme))
        
    # accès guichet controle
    def accesPosteControle(self):

        self.listeTempsAttenteControle[self.nbBusPointControle] = self.heureSysteme - self.listeTempsAttenteControle[self.nbBusPointControle]

        self.nbBusPointControle += 1
        
        if (self.nbBusPointControle >= self.nbBusAvantStop):
            self.schedule.insert(0, (self.FinSimulation, self.heureSysteme))
            return

        
        self.Q1 -= 1
        self.B1 = False
        self.schedule.append((self.departPosteControl, self.heureSysteme + np.random.uniform(15, 65)))

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
        self.schedule.append((self.departReparation, self.heureSysteme + np.random.uniform(168, 330)))

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
        
        self.schedule.append((self.arriveeBus, self.heureSysteme + np.random.exponential((3/4) * 60))) # 120min = 2h

        self.attenteMaxQ1 = 0
        self.attenteMaxQ2 = 0

        self.nbBusPointControle = 0

    def FinSimulation(self):
        self.schedule.clear()
        
        
        

    def run(self):
        # init heure système
        self.heureSysteme = 0

        # Ajout de l'évènement de début de simulation
        self.schedule.append((self.DebutSimu, self.heureSysteme))

        # Tant qu'il y a des evenements dans l'echeancier
        while self.schedule != []:

            # Extraction du prochain evenement
            nextEvent = self.schedule.prochain()

            # Mise à jour de l'heure système
            self.heureSysteme = nextEvent[1]


            # Execution de l'evenement
            nextEvent[0]()

        # Fin de la simulation



if __name__ == '__main__': 

    nbBusAvantStop = int(10E2)
    nbIterationSimu = int(10E4)

    # Matrice nbIterationSimu x nbBusAvantStop
    matriceTempsAttente = np.zeros((nbIterationSimu, nbBusAvantStop))


    
    # Affiche un graphique de la distribution des temps d'attente
    def afficherGraphiqueTempsAttente(liste):
        plt.plot(liste)
        plt.title("Temps d'attente moyen d'un bus avant contrôle")
        plt.xlabel("Numéro du bus dans le système")
        plt.ylabel("Temps d'attente avant contrôle (min)")
        plt.margins(0)

        
    

    def moyennesWelch(matrice):
        moyennes = np.zeros((matrice.shape[1]))
        
        for i in range(0, matrice.shape[1]):
            moyennes[i] = np.mean(matrice[:, i])
                
        return moyennes



    def moyennesLisses(moyennes, w = 5):
        yW=0
        moyennesLisses = []

        for i in range (len(moyennes)):
            
            if i <= w :
                for j in range (-(i-1),i):
                    yW = yW + moyennes[i+j]
                yW = yW / (2*i - 1 )

            elif w + 1 <= i <= len(moyennes) - w :
                for j in range (-w,w):
                    yW = yW + moyennes[i+j]
                yW = yW / (2*w + 1)

            moyennesLisses.append(yW)
        return moyennesLisses

    threads = []
    simus = []

    for i in range(0, nbIterationSimu):
        #print("Simulation n°{}".format(i))
        simulateur = Simulateur(i, nbBusAvantStop)
        simus.append(simulateur)
        
        t = threading.Thread(target=simulateur.run)
        threads.append(t)
        t.start()


    for t in threads:
        t.join()

    
    for simulateur in simus:

        temp = simulateur.listeTempsAttenteControle
        # On supprime les valeurs après l'indice nbBusAvantStop
        del temp[nbBusAvantStop:]

        matriceTempsAttente[simulateur.numSimu] = temp

    

    moyennes = moyennesWelch(matriceTempsAttente)
    afficherGraphiqueTempsAttente(moyennes)
    afficherGraphiqueTempsAttente(moyennesLisses(moyennes))

    # Faire la moyenne des 200 dernières moyennes   
    moyenne200DernieresMoyennes = np.mean(moyennes[-(moyennes.size-200):])
    print(moyenne200DernieresMoyennes)

    plt.legend(["Moyennes Welch", "Moyennes de Welch lissées"])
    plt.show()