from .estandarizador_valores import estandarizador_valores
from .sinonimos_caracteristicas import SINONIMOS_CLAVES, SINONIMOS_VALORES
from .limpiador_entrada import limpiador_entrada

def lector_entrada(entrada: str):
    negativo = False
    clave = []
    valor = []
    entrada_limpia = limpiador_entrada(entrada)
    for palabra in entrada_limpia.split(" "):
        for clavedict in SINONIMOS_CLAVES.keys():
            if palabra in clavedict:
                clave.append(estandarizador_valores(palabra))

        for clavedict in SINONIMOS_VALORES.keys():
            if palabra in clavedict:
                valor.append(estandarizador_valores(palabra))

        if palabra.lower() == "no":
            negativo = True

    if clave and not valor:
        valor.append(True)

    return clave, valor, negativo

