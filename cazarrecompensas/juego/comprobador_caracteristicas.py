from .personajes import PERSONAJES

def comprobar_caracteristicas(personaje, caracteristica):
    print (PERSONAJES)
    if caracteristica in PERSONAJES[personaje].keys():
        return PERSONAJES[personaje][caracteristica]
    else:
        return False
    
comprobar_caracteristicas("Susan", "pelo")
