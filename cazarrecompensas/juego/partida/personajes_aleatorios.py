from .personajes import PERSONAJES
import random

def personajes_aleatorios():
    listarandom = list(PERSONAJES.keys())
    random.shuffle(listarandom)
    return listarandom