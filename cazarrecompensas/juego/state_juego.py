import reflex as rx
import random, time, asyncio
from .partida.personajes_aleatorios import personajes_aleatorios
from ..juego.partida.comparador_caracteristicas import comparador_caracteristicas

class State_juego(rx.State):
    listapersonajes=[]
    personaje_a_adivinar=""
    entrada = ""
    contador_de_intentos = 0
    
    def counter(self):
        self.contador_de_intentos += 1
    
    def presionar_enter(self, event):
        if event == 'Enter':
            self.counter()
            return self.comparar_caracetristicas() 
        
    
    def actualizar_entrada (self, entrada):
        self.entrada = entrada

    def nuevapartida(self):
        self.listapersonajes=personajes_aleatorios()
        self.personaje_a_adivinar=random.choice(personajes_aleatorios())
        self.contador_de_intentos = 0

    def comparar_caracetristicas(self):
        self.actualizar_entrada(self.entrada)
        self.listapersonajes=comparador_caracteristicas(self.listapersonajes, self.personaje_a_adivinar, self.entrada)
        self.entrada = ''
    
    enpartida = True
    correctoincorrecto = ""
    colorborder = "white"

    def reiniciar_partida(self):
        self.enpartida = True
        self.nuevapartida()

    def adivinar(self, personaje):
        self.enpartida = False
        if personaje == self.personaje_a_adivinar:
            self.correctoincorrecto = "Correcto"
            self.colorborder = "lightgreen"
        else:
            self.correctoincorrecto = "Has metido la pata"
            self.colorborder = "red"

    blursalidaentrada=100

    async def entradaapagina(self):
        self.enpartida = True
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

    scalebtnnuevapartida=1.0
    def botonnuevapartidadentro(self):
        self.scalebtnnuevapartida = 1.07

    def botonnuevapartidafuera(self):
        self.scalebtnnuevapartida = 1.0

    scalebtnvolveralmenu=1.0
    def botonvolveralmenudentro(self):
        self.scalebtnvolveralmenu = 1.07

    def botonvolveralmenufuera(self):
        self.scalebtnvolveralmenu = 1.0

    scalebtncomprobar=1.0
    def botoncomprobardentro(self):
        self.scalebtncomprobar = 1.07

    def botoncomprobarfuera(self):
        self.scalebtncomprobar = 1.0


