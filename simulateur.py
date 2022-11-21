import random

class Echeancier:
    def __init__(self):
        self.echeancier = []

    def ajouter(self, date, fonction):
        self.echeancier.append((date, fonction))
        # on tri l'echeancier par date croissante
        self.echeancier.sort(key=lambda x: x[0])

    def prochain(self):
        return self.echeancier.pop(0)

    def estVide(self):
        return len(self.echeancier) == 0

    def __str__(self):
        return str(self.echeancier)




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