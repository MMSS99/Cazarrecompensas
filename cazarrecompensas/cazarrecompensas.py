import reflex as rx 
from .state_menu import State_menu as State
from .areadepruebas.areapruebas import areapruebas

def index():
    return rx.box(
        rx.vstack(
            rx.image(
                src="/cazarecompensas.png"
            ),
            rx.button(
                background_image="url('btnNuevaPartida.png')",
                background_color="transparent",
                width="380px",
                height="60px"
            ),
            rx.button(
                "🚧 Ir al área de pruebas 🚧",
                on_click= State.salida("/areapruebas"),
                background_image="url('pruebas_amarillonegro.jpeg')",
                border_radius="20px",
                margin="12px",
                padding="12px",

                opacity=State.opacidadboton_areapruebas,
                on_mouse_enter=State.masopacidad,
                on_mouse_leave=State.menosopacidad
            ),

            align="center"
        ),

        on_mount=State.entrada,
        background="center/cover url('fondoprueba.jpg')",
        filter= f"blur({State.blursalidaentrada}px)",
        width="100%",
        height="100vh",
        align="center"
        )



app = rx.App()
app.add_page(index)
app.add_page(areapruebas)