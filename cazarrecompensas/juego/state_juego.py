import reflex as rx
import random
from .partida.personajes_aleatorios import personajes_aleatorios

class State_juego(rx.State):
    listapersonajes=[]
    personaje_a_adivinar=""
    def nuevapartida(self):
        self.listapersonajes=personajes_aleatorios()
        self.personaje_a_adivinar=random.choice(personajes_aleatorios())
