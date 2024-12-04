import reflex as rx
import random
from .partida.personajes_aleatorios import personajes_aleatorios
from ..juego.partida.comprobador_caracteristicas import comprobar_caracteristicas
from ..juego.partida.comparador_caracteristicas import comparador_caracteristicas

class State_juego(rx.State):
    listapersonajes=[]
    personaje_a_adivinar=""
    caracteristica_visor = ""
    entrada = "" #Cablear al input de la action bar como en areadepruebas
    
    
    def actualizar_entrada (self, entrada):
        self.entrada = entrada

    def nuevapartida(self):
        self.listapersonajes=personajes_aleatorios()
        self.personaje_a_adivinar=random.choice(personajes_aleatorios())

    def comparar_caracetristicas(self):
        self.actualizar_entrada(self.entrada)
        self.listapersonajes=comparador_caracteristicas(self.listapersonajes, self.personaje_a_adivinar, self.entrada)
        self.entrada = ''

