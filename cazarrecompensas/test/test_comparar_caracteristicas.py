import pytest
from ..juego.partida.comparador_caracteristicas import comparador_caracteristicas

@pytest.mark.parametrize ("personaje1, personaje2, valoracomparar, coinciden", 
                          [("Susan", "Peter", "Tiene el pelo blanco", True),
                           ("Susan", "Bill", "Tiene el pelo blanco", False),
                           ("Susan", "Tom", "No tiene barba", True),
                           ])