import reflex as rx
from ..juego import personajes_aleatorios
from ..juego.comprobador_caracteristicas import comprobar_caracteristicas

class Statepruebas(rx.State):
    personaje=""
    caracteristica = ""
    caracteristica_visor = ""
    def generar_personaje(self):
        self.personaje = personajes_aleatorios()
    def actualizar_caracteristica(self, caracteristica):
        self.caracteristica = caracteristica
    def actualizar_caracteristicavisor (self):
        self.caracteristica_visor = comprobar_caracteristicas(self.personaje, self.caracteristica)