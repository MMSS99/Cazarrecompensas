from personajes import PERSONAJES

def comprobar_caracteristicas(personaje, caracteristica):
    if caracteristica in PERSONAJES[personaje].keys():
        return PERSONAJES[personaje][caracteristica]
    else:
        return False
