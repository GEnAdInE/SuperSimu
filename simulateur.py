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