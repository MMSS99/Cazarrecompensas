import reflex as rx
from .state_areapruebas import Statepruebas as State

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.caracteristica,
            on_change=State.actualizar_caracteristica,
            placeholder="Pregúntame sobre el personaje",
            radius="small",
            width="30%",
        ),
        rx.button(
            "Comprobar",
            on_click=State.actualizar_caracteristicavisor
        ),
        justify="center",
        width="75%"
    )

def areapruebas():
    return rx.box(
        rx.vstack(
            rx.cond(
                State.personaje != "",
                rx.image(
                    src=f"../pj{State.personaje}.jpg",
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

        rx.button(
            "Volver al menú",
            on_click=rx.redirect(
                "/"
                ),
        ),
        background="center/cover url('../fondoprueba.jpg')",
        width="100%",
        height="100vh",
        align="center"
    )


app = rx.App()
app.add_page(areapruebas)