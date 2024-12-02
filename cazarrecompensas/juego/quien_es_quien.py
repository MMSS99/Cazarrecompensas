import reflex as rx
from .state_juego import State_juego as State
from .personajes import PERSONAJES
from ..areadepruebas.areapruebas import action_bar

def juego():
    return rx.vstack( 
        
        rx.box(
            rx.grid(
                rx.foreach(
                    State.listapersonajes,
                    lambda i:rx.box(
                        rx.image(src=f"../pj{i}.jpg", width="100%", height="100%"),
                    
                    
                    ),
                    
                ),
                columns="8",
                gap="5px",
                align="center",
            ),
            max_height="100%",
            align="center",
            max_width="100vh"

        ),
        action_bar(),
        padding="10px",
        display="flex",
        align="center",
        width="100%",
        justify_content="center",
        align_items="center",
        background="center/cover url('../fondoprueba.jpg')",
        height="100vh",

    
    
    )


