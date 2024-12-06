from .personajes import PERSONAJES
from .comprobador_caracteristicas import comprobar_caracteristicas

def comparador_caracteristicas(listadepj, pjaadivinar, entrada):
    listacambiada = []
    for personaje in listadepj:
        if personaje in PERSONAJES.keys():
            if comprobar_caracteristicas(personaje, entrada) == comprobar_caracteristicas(pjaadivinar, entrada):
                listacambiada.append(personaje)
            else:
                listacambiada.append(str(personaje) + "NO")
        else:
            listacambiada.append(personaje)
    return listacambiada