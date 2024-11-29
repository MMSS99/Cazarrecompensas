import pytest
from ..juego.interprete.lector_input import lector_entrada

@pytest.mark.parametrize("entrada, clave, valor, negativo",
                         [("Y va y me dice... ¡De Vallecas!", [], [], False),
                         ("No soy de Vallecas", [], [], True),
                         ("Tiene el pelo rojo", ["pelo"], ["rojo"], False),
                         ("No tiene el pelo amarillo", ["pelo"], ["amarillo"], True),
                         ("No tiene ojos", ["ojos"], [True], True),
                         ("¿No tiene el PELO 84297968247 rojo?", ["pelo"], ["rojo"], True)])

def test_lector(entrada, clave, valor, negativo):
    assert lector_entrada(entrada) == (clave, valor, negativo)