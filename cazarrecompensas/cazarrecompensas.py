import reflex as rx 
from .state_menu import State_menu as State
from .areadepruebas.areapruebas import areapruebas

def index():
    return rx.box(
        rx.vstack(
            rx.button(
                "🚧 Ir al área de pruebas 🚧",
                on_click=rx.redirect("/areapruebas"),
                background_image="url('pruebas_amarillonegro.jpeg')",
                border_radius="20px",
                margin="12px",
                padding="12px",
                opacity=0.5,
                _hover={
                    "opacity": 1,
                },
            ),

            align="center"
        ),


        background="center/cover url('fondoprueba.jpg')",
        width="100%",
        height="100vh",
        align="center"
        )



app = rx.App()
app.add_page(index)
app.add_page(areapruebas)