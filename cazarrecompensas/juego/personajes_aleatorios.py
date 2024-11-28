from .personajes import PERSONAJES
import random

def personajes_aleatorios():
    
    return random.choice(list(PERSONAJES.keys()))