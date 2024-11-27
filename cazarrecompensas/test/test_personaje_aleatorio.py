import pytest
from cazarrecompensas.juego.personajes import personajes_aleatorios

def test_personajes_aleatorios():
    assert personajes_aleatorios() in ["Susan", "Claire", "David", "Anne", "Robert", "Anita", "Joe", "George", "Bill", "Alfred", "Max", "Tom", "Alex", "Sam", "Richard", "Paul", "Maria", "Frans", "Herman", "Bernard", "Philip", "Eric", "Charles", "Peter"]
