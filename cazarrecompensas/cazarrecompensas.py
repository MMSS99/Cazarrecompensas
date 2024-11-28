import reflex as rx 
from .juego import personajes, personajes_aleatorios
class State(rx.State):
    personaje = ""

    def generar_personaje(self):
        self.personaje = personajes_aleatorios()
    
    
def index():
    return rx.vstack(
        rx.cond(
            State.personaje != "",
            rx.image(
                src=f"pj{State.personaje}.jpg",
                width="335px",
                height="576px",
                border="5px solid #555"
            ),
            rx.text(
                "Selecciona un personaje", font_size="2em"
            ),
        ),
        rx.heading(
            State.personaje, 
            font_size="2em"
        ),
        
        rx.button(
            "Nuevo Personaje",
            on_click=State.generar_personaje,
            color_scheme="tomato"
        ),

        align="center",
        direction="column",
        style={
            "background_color": "lightblue",
            "height": "100vh"
        }
    )
app = rx.App()
app.add_page(index)