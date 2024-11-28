import pytest
from cazarrecompensas.juego.comprobador_caracteristicas import comprobar_caracteristicas

@pytest.mark.parametrize ("Personaje, Caracteristica, Resultado", 
                          [("Susan", "pelo", "blanco"),
                           ("Claire", "ojos", "marron"),
                           ("Joe", "gafas", True),
                           ("Alfred", "ojos", "azul"),
                           ("Susan", "caracteristicainexistente", False)])

def test_comprobar_caracteristicas(Personaje, Caracteristica, Resultado):
    assert comprobar_caracteristicas(Personaje, Caracteristica) == Resultado
