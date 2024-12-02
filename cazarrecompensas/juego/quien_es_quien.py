import reflex as rx
from .personajes import PERSONAJES
from ..areadepruebas.areapruebas import action_bar

def juego():
    caras = PERSONAJES.keys()
    return rx.vstack( 
        
        rx.box(
            rx.grid(
                *[
                    rx.box(
                        rx.image(src=f"../pj{cara}.jpg", width="100%", height="100%"),
                    
                    
                    )
                    for cara in caras
                ],
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


