import asyncio
import reflex as rx
import time

class State_menu(rx.State):
    opacidadboton_areapruebas=0.5
    blursalidaentrada=100

    async def masopacidad(self):
        while self.opacidadboton_areapruebas < 1:
            time.sleep(0.01)
            self.opacidadboton_areapruebas += 0.05
            yield

    async def menosopacidad(self):
        while self.opacidadboton_areapruebas > 0.5:
            time.sleep(0.01)
            self.opacidadboton_areapruebas -= 0.1
            yield
    
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

    scalebtnnuevapartida=1.0

    def botonnuevapartidadentro(self):
        self.scalebtnnuevapartida = 1.07

    def botonnuevapartidafuera(self):
        self.scalebtnnuevapartida = 1.0
            



