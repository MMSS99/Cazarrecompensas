import pytest
from cazarrecompensas.juego.interprete.estandarizador_valores import estandarizador_valores

@pytest.mark.parametrize("termino, sinonimo", 
                         [("canas", "blanco"),
                          ("pelirrojo", "rojo"),
                          ("accesorios", "pendientes"),
                          ("perilla", "barba"),
                          ("calvo", "entradas")
                          ])

def test_valores_estandares(termino, sinonimo):
    assert estandarizador_valores(termino) == sinonimo