import reflex as rx 
from juego.personajes import personajes_aleatorios
class State(rx.State):
    personaje = ""

    def generar_personaje(self):
        self.personaje = personajes_aleatorios()
    
    
def index():
    return rx.hstack(
        rx.button(
            on_click=State.generar_personaje,
        ),
        rx.heading(State.personaje, font_size="2em"),
        )
app = rx.App()
app.add_page(index)