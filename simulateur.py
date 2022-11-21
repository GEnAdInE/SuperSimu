Q2 = 0
B2 = False

def ArriveFile2():
    global Q2, B2
    Q2 += 1
    if not B2:
        B2 = True
        Shedule("AccesGuichet2", 0)
    return Q2

def Shedule(event, delay):
    global Q2, B2