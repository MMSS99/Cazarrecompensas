import pytest
from cazarrecompensas.juego.comprobador_caracteristicas import comprobar_caracteristicas

@pytest.mark.parametrize ("personaje, entrada, resultado", 
                          [("Susan", "Tiene el pelo blanco", "Si"),
                           ("Susan", "Tiene el pelo negro", "No"),
                           ("Susan", "Tiene barba", "No"),
                           ("Susan", "No tiene pendientes", "Si")
                           ])

def test_comprobar_caracteristicas(personaje, entrada, resultado):
    assert comprobar_caracteristicas(personaje, entrada) == resultado
