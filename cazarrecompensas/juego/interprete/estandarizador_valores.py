from .sinonimos_caracteristicas import SINONIMOS_CLAVES, SINONIMOS_VALORES

def estandarizador_valores(termino):
    for clave in SINONIMOS_CLAVES.keys():
        for sinonimo in clave:
            if termino.lower() == sinonimo:
                return SINONIMOS_CLAVES[clave]
            
    for clave in SINONIMOS_VALORES.keys():
        for sinonimo in clave:
            if termino.lower() == sinonimo:
                return SINONIMOS_VALORES[clave]
    