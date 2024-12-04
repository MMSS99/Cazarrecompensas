import reflex as rx
from .state_juego import State_juego as State

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.entrada,
            on_change=State.actualizar_entrada,
            placeholder="Pregúntame sobre el personaje",
            radius="small",
            width="30%",
        ),
        rx.button(
            "Comprobar",
            on_click=State.comparar_caracetristicas
        ),
        justify="center",
        width="75%"
    )

def juego():
    return rx.box(
        rx.cond(
            State.enpartida,        
            rx.vstack( 
                rx.box(
                    rx.grid(
                        rx.foreach(
                            State.listapersonajes,
                            lambda i:rx.box(
                                rx.image(src=f"../pj{i}.jpg", on_click=State.adivinar(i),width="100%", height="100%"),
                            ), 
                        ),
                    columns="8",
                    gap="5px",
                    align="center",
                    
                    ),
                
                rx.box(
                    rx.heading(
                    f"La respuesta a tu pregunta es... NO FUNCIONANDO",
                    font_size="2em",
                    align="center"
                    ),
                max_height="100%",
                align="center",
                max_width="100vh"
                ),

            
                action_bar(),
                on_mount=State.nuevapartida,
                width="60vw",
                height="60vh",
                margin="auto",
                align_items="center",
                
                
                ),
            ),
            rx.vstack(
                rx.text(
                    f"{State.correctoincorrecto}, el personaje a adivinar era..."
                ),
                rx.image(src=f"../pj{State.personaje_a_adivinar}.jpg")
            ),
        ),
        rx.button(
            "Volver al menú",
            on_click=State.salida("/"),
        ),
        on_mount=State.entradaapagina,
        background="center/cover url('../fondoprueba.jpg')",
        filter= f"blur({State.blursalidaentrada}px)",
        height="100vh",

    )

