import pytest
from ..juego.partida.comparador_caracteristicas import comparador_caracteristicas

@pytest.mark.parametrize ("listapj, pjaadivinar, entrada, listaresultante", 
                          [(["Susan", "Herman", "Paul", "Eric"], "Peter", "Tiene el pelo blanco", ["Susan", "HermanNO", "Paul", "EricNO"]),
                           (["Susan", "Herman", "Paul", "Eric"], "Bill", "Tiene el pelo blanco", ["SusanNO", "Herman", "PaulNO", "Eric"]),
                           (["Susan", "Herman", "Bill", "Richard"], "Tom", "No tiene barba", ["Susan", "Herman", "BillNO", "RichardNO"]),
                           ])

def test_comparar_caracteristicas(listapj, pjaadivinar, entrada, listaresultante):
    assert comparador_caracteristicas(listapj, pjaadivinar, entrada) == listaresultante