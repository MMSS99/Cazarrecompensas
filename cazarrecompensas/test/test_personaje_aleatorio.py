import pytest
from cazarrecompensas.juego.partida.personajes_aleatorios import personajes_aleatorios

@pytest.mark.unidad
def test_personajes_aleatorios():
    assert personajes_aleatorios() != personajes_aleatorios()
