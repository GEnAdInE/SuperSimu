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
    

# TODO tous niquer

def AccesPosteControle():
    global fileDattControle
    global posteControlStatus
    fileDattControle = fileDattControle - 1
    posteControlStatus = False
    DepartPosteControle() #TODO : truc de temps

def AccesPosteReparation1():
    global fileDattRepairs
    global posteReparation1Status
    fileDattRepairs = fileDattRepairs - 1
    posteReparation1Status = False
    DepartPosteReparation1() #TODO : truc de temps


def AccesPosteReparation2():
    global fileDattRepairs
    global posteReparation2Status
    fileDattRepairs = fileDattRepairs - 1
    posteReparation2Status = False
    DepartPosteReparation2() #TODO : truc de temps
