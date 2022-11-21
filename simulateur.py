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
