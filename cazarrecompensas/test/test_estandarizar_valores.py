import pytest
from cazarrecompensas.juego.interprete.estandarizador_valores import estandarizador_valores, estandarizador_claves

@pytest.mark.parametrize("valor, sinonimovalor", 
                         [("canas", "blanco"),
                          ("pelirrojo", "rojo"),
                          ])

def test_valores_estandares(valor, sinonimovalor):
    assert estandarizador_valores(valor) == sinonimovalor

@pytest.mark.parametrize("clave, sinonimoclave", 
                         [("pelirrojo", "pelo"),
                          ("accesorios", "pendientes"),
                          ("perilla", "barba"),
                          ("calvo", "entradas")
                          ])

def test_claves_estandares(clave, sinonimoclave):
    assert estandarizador_claves(clave) == sinonimoclave