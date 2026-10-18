# Módulo vocales (Práctica 3 - Ejercicios 1 y 3)
# Contiene las funciones para contar las vocales de una palabra.

VOCALES = "aeiouáéíóúü"


def contar_vocales_iterativa(palabra):
    """Retorna la cantidad de vocales de la palabra recorriéndola con un for."""
    cantidad = 0
    for letra in palabra.lower():
        if letra in VOCALES:
            cantidad = cantidad + 1
    return cantidad


def contar_vocales_recursiva(palabra):
    """Retorna la cantidad de vocales de la palabra de forma recursiva.

    Caso base: la palabra vacía no tiene vocales.
    Caso recursivo: se analiza la primera letra y se llama a la función
    con el resto de la palabra (cada llamada tiene una letra menos).
    """
    if palabra == "":
        return 0

    primera_letra = palabra[0].lower()
    resto = palabra[1:]

    if primera_letra in VOCALES:
        return 1 + contar_vocales_recursiva(resto)
    else:
        return contar_vocales_recursiva(resto)
