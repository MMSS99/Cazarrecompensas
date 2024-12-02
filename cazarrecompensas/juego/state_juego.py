import reflex as rx
import random
from .partida.personajes_aleatorios import personajes_aleatorios

class State_juego(rx.State):
    listapersonajes=personajes_aleatorios()
    personaje_a_adivinar=random.choice(personajes_aleatorios())
