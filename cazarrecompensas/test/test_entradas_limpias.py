import pytest
from cazarrecompensas.juego.interprete.limpiador_entrada import limpiador_entrada

@pytest.mark.parametrize ("entrada, salida", 
                          [("Y va y me dice... ¡De Vallecas!", "y va y me dice de vallecas"),
                           ("¿Tiene el pelo rojo?", "tiene el pelo rojo"),
                           ("5784165 rojo rojO", "rojo rojo"),
                           ("VALLE     CAS", "valle     cas")
                           ])

@pytest.mark.unidad
def test_entradaslimpias(entrada, salida):
    assert limpiador_entrada(entrada) == salida