# TODO tous niquer

def AccesPosteControle():
    # TODO Decrementer le nombre de client dans la files
    global fileDatt
    global postestatus
    fileDatt = fileDatt - 1
    postestatus = False
    DepartPosteControle()

