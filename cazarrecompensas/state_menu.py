import asyncio
import reflex as rx
import time

class State_menu(rx.State):
    opacidadboton_areapruebas=0.5
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
