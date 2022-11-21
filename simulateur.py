import numpy as np


def departPosteControl():
    global statusControl
    statusControl = 0
    if NombreBusFileControl > 0:
        # Ici mettre date à l'heure précis
        AccesControl()
    if np.random.normal(0, 1) < 0.3:
        # Ici mettre date à l'heure précis
        AccesFileR()
