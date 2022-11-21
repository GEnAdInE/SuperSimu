




# Echeancier d'evenements
echeancier = Echeancier()
dateSysteme = 0
nbBus = 0
dureesSimulation = [40, 80, 160, 240]



# Fonction d'initialisation de la simulation
def debutSimulation(nbHeures):
    global dateSysteme
    dateSysteme = 0
    echeancier.ajouter(dateSysteme + nbHeures * 60, finSimulation)
    arriveeBus()


# Arrivee d'un bus
def arriveeBus():
    global dateSysteme, nbBus

    nbBus += 1

    # Ajout d'un évenement d'arrivée dans la file de controle
    echeancier.ajouter(dateSysteme, arriveeFileC)

    # Ajout d'un nouvel evenement suivant la loi exponentielle de paramètre 1/2
    echeancier.ajouter(dateSysteme + random.expovariate(0.5), arriveeBus)




for duree in dureesSimulation:
    init(duree)

    while echeancier:
        # On recupere le prochain evenement
        evenement = echeancier.pop(0)
        dateSysteme = evenement[0]
        # On execute l'evenement
        evenement[1]()

    print("Fin de la simulation apres " + str(duree) + " heures")

import numpy as np

class Schedule:
    
    def __init__(self, duree):
        self.duree_simulation = duree
        self.schedule = []

    def arriveFileReparation(self):
        self.Q2 += 1
        self.nbBusRepair += 1
        if self.B2 < 2:
            self.schedule.append("AccesGuichetR", 0)
            
    def arriveFileControle(self):
        self.Q1 = self.Q1 + 1
        if self.Q1 == 1:
            self.schedule.append("AccesGuichetC", 0)
        
    def accesPosteControle(self):
        self.Q1 -= 1
        self.B1 = False
        self.schedule.append("DepartControle", "AJOUTER TEMPS")    
    


def departPosteControl():
    global statusControl
    statusControl = 0
    if NombreBusFileControl > 0:
        # Ici mettre date à l'heure précis
        AccesControl()
    if np.random.normal(0, 1) < 0.3:
        # Ici mettre date à l'heure précis
        AccesFileR()

def AccesPosteControle():
    global fileDattControle
    global posteControlStatus
    fileDattControle = fileDattControle - 1
    posteControlStatus = False
    DepartPosteControle() #TODO : truc de temps

def AccesPosteReparation():
    global fileDattRepairs
    global posteReparation1Status
    fileDattRepairs = fileDattRepairs - 1
    posteReparation1Status = False
    DepartPosteReparation1() #TODO : truc de temps

def DepartReparation():
        global posteReparation1Status
        posteReparation1Status = True
        if fileDattRepairs > 0:
            #Prendre en compte le temps ma gatée
            AccesReparation()

    def AccesPosteReparation(self):
        self.Q2 -= 1
        self.B2 += 1
        self.schedule.append("DepartReparation", "AJOUTER TEMPS")    


def DebutSimu(dureeSimu):
    global NbBus,NbBusRep,AireQc,AireQr,AireBr,Qc,Qr,Bc,Br

    NbBus,NbBusRep,AireQc,AireQr,AireBrr,Qc,Qr = 0,0,0,0,0,0,0
    Bc,Br = False,False
    ArriveBus() # a data x
    #TODO : FAIRE FIN DANS dureeSimu


