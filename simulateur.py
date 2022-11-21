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

def Shedule(event, delay):
    global Q2, B2