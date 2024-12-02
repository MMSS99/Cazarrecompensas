import reflex as rx
from .personajes_aleatorios import personajes_aleatorios

class State_juego(rx.State):
    listapersonajes=personajes_aleatorios()
