import reflex as rx
from .state_juego import State_juego as State

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.entrada,
            on_change=State.actualizar_entrada,
            placeholder="Pregúntame sobre el personaje",
            radius="small",
            min_width="40%",
            on_key_down=State.presionar_enter
            
        ),
        rx.button(
            "Comprobar",
            on_click=State.comparar_caracetristicas
        ),
        justify="center",
        align="center",
        min_width="75%"
    )

def juego():
    return rx.box(
        rx.cond(
            State.enpartida,        
            rx.vstack( #Grid de partida
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
                    margin_bottom="20px",
                    
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
                rx.text( #Post-partida
                    f"{State.correctoincorrecto}, el personaje a adivinar era...{State.personaje_a_adivinar}",

                    font_size="1em"
                ),
                rx.text(
                    f"Intentos: {State.contador_de_intentos}",
                    font_size="1em"
                ),
                rx.image(src=f"../pj{State.personaje_a_adivinar}.jpg"),
                rx.button(
                    on_click=State.reiniciar_partida,

                    background_image="url('../btnNuevaPartida.png')",
                    background_color="transparent",
                    width="380px",
                    height="60px",

                    scale= State.scalebtnnuevapartida,
                    on_mouse_enter= State.botonnuevapartidadentro,
                    on_mouse_leave=  State.botonnuevapartidafuera
                ),
                min_width="100vh",
                padding="20px",
                align="center",
                direction="column"
            ),

            
            ),
            rx.button(
            "Volver al menú",
            on_click=State.salida("/"),
            aling="center"
        ),
        
        on_mount=State.entradaapagina,
        background="center/cover url('../fondoprueba.jpg')",
        filter= f"blur({State.blursalidaentrada}px)",
        height="100vh",
        direction="column",
        align="center"

    )

