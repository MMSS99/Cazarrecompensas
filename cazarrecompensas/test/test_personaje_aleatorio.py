import pytest
from cazarrecompensas.juego.personajes_aleatorios import personajes_aleatorios

def test_personajes_aleatorios():
    assert personajes_aleatorios() != personajes_aleatorios()
