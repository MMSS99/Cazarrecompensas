from .sinonimos_caracteristicas import SINONIMOS_CLAVES, SINONIMOS_VALORES

def lector_entrada(entrada: str):
    negativo = False
    clave = []
    valor = []
    for palabra in entrada:
        if palabra in SINONIMOS_CLAVES.keys():
            clave.append(palabra)
        if palabra in SINONIMOS_VALORES.keys():
