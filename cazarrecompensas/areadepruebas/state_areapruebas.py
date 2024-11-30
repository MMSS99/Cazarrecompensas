import reflex as rx
import asyncio
import time
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

    blursalidaentrada=100
    async def entrada(self):
        while self.blursalidaentrada >= 1:
            time.sleep(0.01)
            self.blursalidaentrada -= 1
            yield

    async def salida(self, direccion):
        while self.blursalidaentrada < 100:
            time.sleep(0.01)
            self.blursalidaentrada += 1
            yield
        yield rx.redirect(direccion)