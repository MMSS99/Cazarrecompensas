def limpiador_entrada(entrada : str):
    return (''.join(caracter for caracter in entrada.lower() if caracter.isalpha() or caracter.isspace()).strip())