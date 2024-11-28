import reflex as rx 
from .juego import personajes_aleatorios
class State(rx.State):
    personaje=""
    caracteristica = ""
    caracteristica_visor = ""
    def generar_personaje(self):
        self.personaje = personajes_aleatorios()
    def actualizar_caracteristica(self, caracteristica):
        self.caracteristica = caracteristica
    def actualizar_caracteristicavisor (self):
        self.caracteristica_visor = self.caracteristica
    
    
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.caracteristica,
            on_change=State.actualizar_caracteristica,
            placeholder="Inserta una caracteristica"
        ),
        rx.button(
            "Comprobar caracteristica",
            on_click=State.actualizar_caracteristicavisor
            )
    )
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
            State.caracteristica_visor,
            font_size="2em"
        ),
        
        rx.button(
            "Nuevo Personaje",
            on_click=State.generar_personaje,
            color_scheme="tomato"
        ),
    
        action_bar(),
        align="center",
        direction="column",
        style={
            "background_color": "lightblue",
            "height": "100vh"
        }
    )


app = rx.App()
app.add_page(index)