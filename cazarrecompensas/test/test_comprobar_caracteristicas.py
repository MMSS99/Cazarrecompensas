import pytest
from cazarrecompensas.juego.comprobador_caracteristicas import comprobar_caracteristicas

def test_comprobar_caracteristicas():
    assert comprobar_caracteristicas("Susan", "pelo") == "rubio"
    assert comprobar_caracteristicas("Claire", "ojos") == "marron"
    assert comprobar_caracteristicas("Joe", "gafas") == True
    assert comprobar_caracteristicas("Alfred", "ojos") == "azul"
    assert comprobar_caracteristicas("Susan", "ratata") == False

