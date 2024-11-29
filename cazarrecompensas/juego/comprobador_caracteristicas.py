from .personajes import PERSONAJES
from .interprete.lector_input import lector_entrada

def comprobar_caracteristicas(personaje : str, entrada : str):
    try:
        valores_entrada = lector_entrada(entrada)
        clave_entrada = valores_entrada[0][0]
        valor_entrada = valores_entrada[1][0]
        es_negativo = valores_entrada[2]
        print (clave_entrada, valor_entrada, es_negativo)

        if valor_entrada == PERSONAJES[personaje][clave_entrada]:
            if es_negativo == False:
                return "Si"
            if es_negativo == True:
                return "No"
        else:
            if es_negativo == True:
                return "Si"
            if es_negativo == False:
                return "No"
    except IndexError:
        return "No sé cómo responder a eso"
    
    

