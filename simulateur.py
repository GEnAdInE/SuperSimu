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
import time

class Schedule:
    
    def __init__(self, duree):
        self.duree_simulation = duree
        self.schedule = []
    
    # Arrivee d'un bus
    def arriveeBus(self):
        self.nbBus += 1

        # Ajout d'un évenement d'arrivée dans la file de controle
        self.schedule.append("ArriveFileControle", 0)

        # Ajout d'un nouvel evenement suivant la loi exponentielle de paramètre 0.5
        self.schedule.append((self.arriveesBus,time.time + np.exponential((4/3)) * 120)) # 120min = 2h
            
    # arrivé bus dans la file de controle
    def arriveFileControle(self):
        self.Q1 = self.Q1 + 1
        if self.Q1 == 1:
            self.schedule.append("AccesGuichetC", 0)
        
    # accès guichet controle
    def accesPosteControle(self):
        self.Q1 -= 1
        self.B1 = False
        self.schedule.append("DepartControle", time.time + np.uniform(0.25, 13/12))

    def departPosteControl(self):
        
        self.B1 = True
        if self.Q1 > 0:
            # Ici mettre date à l'heure précis
            self.schedule.append("AccesGuichetC", 0)
        if np.uniform(0, 1) < 0.3:

            # Ici mettre date à l'heure précis
            self.schedule.append("AccesFileRéparation", 0)

    # accès guichet réparation
    def arriveFileReparation(self):
        self.Q2 += 1
        self.nbBusRepair += 1
        if self.B2 < 2:
            self.schedule.append("AccesGuichetR", 0)

    # accès guichet réparation
    def accesPosteReparation(self):
        
        self.Q2 -= 1
        self.B2 += 1
        self.schedule.append("DepartReparation", time.time + np.uniform(168, 330))

    def departReparation(self):
        
        self.B2 -= 1
        if self.Q2 > 0:
            
            self.schedule.append("AccesGuichetR", 0)


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


        self.schedule.append((self.arriveesBus,time.time + np.exponential((4/3)) * 120)) # 120min = 2h
        ArriveBus() # a data x
        #TODO : FAIRE FIN DANS dureeSimu


