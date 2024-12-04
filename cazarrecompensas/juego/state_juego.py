import reflex as rx
import random
from .partida.personajes_aleatorios import personajes_aleatorios
from ..juego.partida.comprobador_caracteristicas import comprobar_caracteristicas

class State_juego(rx.State):
    listapersonajes=[]
    personaje_a_adivinar=""
    caracteristica_visor = ""
    
    
    def actualizar_caracteristicavisor (self):
        self.caracteristica_visor = comprobar_caracteristicas(self.personaje_a_adivinar, self.caracteristica)
    def nuevapartida(self):
        self.listapersonajes=personajes_aleatorios()
        self.personaje_a_adivinar=random.choice(personajes_aleatorios())
