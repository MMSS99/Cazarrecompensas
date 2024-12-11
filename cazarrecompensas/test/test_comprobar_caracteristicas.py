import pytest
from cazarrecompensas.juego.partida.comprobador_caracteristicas import comprobar_caracteristicas

@pytest.mark.parametrize ("personaje, entrada, resultado", 
                          [("Susan", "Tiene el pelo blanco", "Si"),
                           ("Susan", "Tiene el pelo negro", "No"),
                           ("Susan", "Tiene barba", "No"),
                           ("Susan", "No tiene pendientes", "Si"),
                           ("David", "¿Es rubio?", "Si"),
                           ("David", "¿Es pelirrojo?", "No"),
                           ("David", "Vallecas", "No sé cómo responder a eso"),
                           ("David", "5429875", "No sé cómo responder a eso")
                           ])

@pytest.mark.integracion
def test_comprobar_caracteristicas(personaje, entrada, resultado):
    assert comprobar_caracteristicas(personaje, entrada) == resultado
