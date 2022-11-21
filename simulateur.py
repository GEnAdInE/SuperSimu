
import numpy as np


Q2 = 0
B2 = 0
nbBusRepair = 0

def ArriveFile2():
    global Q2, B2, nbBusRepair
    Q2 += 1
    nbBusRepair += 1
    if B2 < 2:
        Shedule("AccesGuichet2", 0)
    return Q2
    
# file d'attente station contrôle  
Q1 = 0

# État guichet contrôle
B1 = False

def ArriveFile1():
    global Q1, B1
    Q1 = Q1 + 1
    if Q1 == 1:
        Schedule("AccesGuichetC", 0)
    return Q1

# fonction d'exécution des evenements
def Schedule(event, delay):
    global Time
    Time = Time + delay
    print("Time = ", Time, "Event = ", event)
    

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

