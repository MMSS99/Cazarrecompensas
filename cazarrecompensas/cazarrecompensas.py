import reflex as rx 
from .juego import personajes_aleatorios
from .juego.comprobador_caracteristicas import comprobar_caracteristicas
class State(rx.State):
    personaje=""
    caracteristica = ""
    caracteristica_visor = ""
    def generar_personaje(self):
        self.personaje = personajes_aleatorios()
    def actualizar_caracteristica(self, caracteristica):
        self.caracteristica = caracteristica
    def actualizar_caracteristicavisor (self):
        self.caracteristica_visor = comprobar_caracteristicas(self.personaje, self.caracteristica)
    
    
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.caracteristica,
            on_change=State.actualizar_caracteristica,
            placeholder="Pregúntame sobre el personaje"
        ),
        rx.button(
            "Comprobar",
            on_click=State.actualizar_caracteristicavisor
            )
    )
def index():
    return rx.box(
        rx.vstack(
            rx.cond(
                State.personaje != "",
                rx.image(
                    src=f"pj{State.personaje}.jpg",
                    height="300px",
                    border="5px solid #555"
                ),
                rx.text(
                    "Selecciona un personaje", font_size="2em"
                ),
            ),
            rx.box(
                rx.heading(
                f"La respuesta a tu pregunta es... {State.caracteristica_visor}",
                font_size="2em",
                align="center"
                ),

                background="radial-gradient(circle, rgba(172,31,8,0.37923672887123594) 0%, rgba(255,0,66,0.3008053563222164) 100%)",
                border_radius="20px",
                width="40%",
                margin="12px",
                padding="12px",

            ),
            
            rx.button(
                "Nuevo Personaje",
                on_click=State.generar_personaje,
                color_scheme="tomato"
            ),
        
            action_bar(),
            align="center",
            direction="column",
            
        ),
        background="center/cover url('fondoprueba.jpg')",
        width="100%",
        height="100%",
    )


app = rx.App()
app.add_page(index)