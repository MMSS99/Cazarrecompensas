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
            on_click=State.comparar_caracetristicas,

            background_image="url('../btnComprobar.png')",
            background_color="transparent",
            width="140px",
            height="55px",

            scale= State.scalebtncomprobar,
            on_mouse_enter= State.botoncomprobardentro,
            on_mouse_leave=  State.botoncomprobarfuera
        ),
        justify="center",
        align="center",
        min_width="75%",
        
            
    )

def volver_al_menu() -> rx.Component:
    return rx.button(
                    on_click=State.salida("/"),

                    background_image="url('../btnVolverAlMenu.png')",
                    background_color="transparent",
                    width="380px",
                    height="60px",

                    scale= State.scalebtnvolveralmenu,
                    on_mouse_enter= State.botonvolveralmenudentro,
                    on_mouse_leave=  State.botonvolveralmenufuera
                ),

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
                    margin_bottom="12px",
                    margin_top="20px"
                    ),
                
                

            
                action_bar(),
                rx.vstack(volver_al_menu(), justify="center", align_items="center", margin_top="12px"),
                on_mount=State.nuevapartida,
                width="60vw",
                height="60vh",
                margin="auto",
                align_items="center",
                
                
                ),
            
            ),
            rx.vstack(
                rx.box(
                    rx.text( #Post-partida
                        rx.text.strong(f"{State.correctoincorrecto}", color=State.colorborder),
                        ", el personaje a adivinar era... ",
                        rx.text.strong(f"{State.personaje_a_adivinar}"),

                        font_size="1em",
                        high_contrast=True,
                    ),
                    rx.text(
                        rx.text.em(f"Intentos: {State.contador_de_intentos}"),
                        font_size="0.7em",
                        high_contrast=True,
                        align="centre"
                    ),

                    background="radial-gradient(circle, rgba(94,33,13,0.5004202364539565) 0%, rgba(121,30,9,0.5032213569021359) 46%, rgba(135,69,0,0.5116247182466737) 100%)",
                    border="solid",
                    border_radius="20px",
                    width="40%",
                    padding="12px",
                    text_align="center"
                    
                    

                ),
                rx.image(src=f"../pj{State.personaje_a_adivinar}.jpg", border="solid", border_color=State.colorborder, border_radius="20px", border_width="thick"),
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
                volver_al_menu(),
                min_width="100vh",
                padding="20px",
                align="center",
                direction="column"
            ),

            
        ),
            
        
        on_mount=State.entradaapagina,
        background="center/cover url('../fondoprueba.jpg')",
        filter= f"blur({State.blursalidaentrada}px)",
        height="100vh",
        direction="column",
        align="center"

    )

