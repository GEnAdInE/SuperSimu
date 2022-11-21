# file d'attente station contrôle  

def ArriveFile1(Q1):
    Q1 = Q1 + 1
    if Q1 == 1:
        Schedule("DepartFile1", 0.5)

# fonction d'exécution des evenements
def Schedule(event, delay):
    global Time
    Time = Time + delay
    print("Time = ", Time, "Event = ", event)
    