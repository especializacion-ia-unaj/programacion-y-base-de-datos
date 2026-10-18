# Práctica 3 - Programación modular, funciones y recursión
# Temas: funciones, parámetros, retorno de varios valores, módulos, recursión y excepciones.

import math
import random

from vocales import contar_vocales_iterativa, contar_vocales_recursiva


# ---------------------------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------------------------

def leer_entero(mensaje):
    """Pide un número entero y lo vuelve a pedir mientras el dato no sea válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número entero.")


def leer_real(mensaje):
    """Pide un número real y lo vuelve a pedir mientras el dato no sea válido."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número.")


# ---------------------------------------------------------------------------
# Ejercicio 2: función a analizar
# ---------------------------------------------------------------------------

def ne(num1, num2):
    if num1 > num2:
        aux = num1
        num1 = num2
        num2 = aux

    for i in range(num1 + 1, num2):
        print(i)

# Descripción de la función ne:
# Recibe dos números enteros e imprime, de menor a mayor, todos los enteros que están estrictamente entre ellos (sin incluir los extremos).
# Si num1 es mayor que num2, primero los intercambia usando una variable auxiliar, para que el for siempre vaya del menor al mayor.
# Si los números son iguales o consecutivos, no imprime nada.


# ---------------------------------------------------------------------------
# Ejercicio 4
# ---------------------------------------------------------------------------

def cantidad_y_suma_de_digitos(numero):
    """Retorna dos valores: la cantidad de dígitos del número y la suma de esos dígitos."""
    numero = abs(numero)   # el signo no es un dígito

    if numero == 0:
        return 1, 0

    cantidad = 0
    suma = 0
    while numero > 0:
        digito = numero % 10       # último dígito
        suma = suma + digito
        cantidad = cantidad + 1
        numero = numero // 10      # se descarta el último dígito
    return cantidad, suma


# ---------------------------------------------------------------------------
# Ejercicio 5
# ---------------------------------------------------------------------------

def generar_numeros_aleatorios(cantidad, minimo, maximo):
    """Retorna una lista con 'cantidad' números reales aleatorios entre minimo y maximo."""
    numeros = []
    for i in range(cantidad):
        numeros.append(random.uniform(minimo, maximo))
    return numeros


def ordenar_lista(numeros):
    """Ordena la lista de menor a mayor (la modifica directamente)."""
    numeros.sort()


def mostrar_lista(numeros):
    """Muestra cada número de la lista con su posición y dos decimales."""
    posicion = 1
    for numero in numeros:
        print(posicion, ")", round(numero, 2))
        posicion = posicion + 1


# ---------------------------------------------------------------------------
# Ejercicio 6
# ---------------------------------------------------------------------------

def existe_apellido(apellidos, buscado, posicion):
    """Retorna True si 'buscado' está en la lista a partir de 'posicion', False si no.

    Caso base 1: se llegó al final de la lista -> no está.
    Caso base 2: el apellido de la posición actual es el buscado -> está.
    Caso recursivo: se busca en la posición siguiente.
    """
    if posicion == len(apellidos):
        return False
    if apellidos[posicion].lower() == buscado.lower():
        return True
    return existe_apellido(apellidos, buscado, posicion + 1)


# ---------------------------------------------------------------------------
# Ejercicio 7
# ---------------------------------------------------------------------------

def contar_apariciones(numero, numeros, posicion):
    """Retorna cuántas veces aparece 'numero' en la lista a partir de 'posicion'.

    Caso base: se llegó al final de la lista -> 0 apariciones.
    Caso recursivo: se cuenta la posición actual (1 o 0) y se suma
    lo que devuelve la llamada con la posición siguiente.
    """
    if posicion == len(numeros):
        return 0

    if numeros[posicion] == numero:
        return 1 + contar_apariciones(numero, numeros, posicion + 1)
    else:
        return contar_apariciones(numero, numeros, posicion + 1)


# ---------------------------------------------------------------------------
# Ejercicio 8
# ---------------------------------------------------------------------------

def calcular_diametro(radio):
    """Retorna el diámetro de un círculo a partir de su radio."""
    return 2 * radio


def calcular_perimetro(radio):
    """Retorna el perímetro de un círculo a partir de su radio."""
    return 2 * math.pi * radio


# ===========================================================================
# Programa principal
# ===========================================================================

# Ejercicio 1
print("Ejercicio 1: Contar las vocales de una palabra.")
palabra = input("Ingrese una palabra: ")
print("a) Versión iterativa:", contar_vocales_iterativa(palabra), "vocales")
print("b) Versión recursiva:", contar_vocales_recursiva(palabra), "vocales")


# Ejercicio 2
print("\nEjercicio 2: Analizar la función ne (ver la descripción en el código).")
print("Ejemplo: ne(8, 3) imprime los enteros que hay entre 3 y 8:")
ne(8, 3)


# Ejercicio 3
print("\nEjercicio 3: Diccionario con la cantidad de vocales de cada palabra.")
print("Ingrese palabras. Para terminar, presione Enter sin escribir nada.")
vocales_por_palabra = {}
palabra = input("Palabra: ")
while palabra != "":
    vocales_por_palabra[palabra] = contar_vocales_iterativa(palabra)
    palabra = input("Palabra: ")
print("Diccionario:", vocales_por_palabra)


# Ejercicio 4
print("\nEjercicio 4: Cantidad de dígitos y suma de los dígitos de un número.")
numero = leer_entero("Ingrese un número entero: ")
cantidad, suma = cantidad_y_suma_de_digitos(numero)
print("El número", numero, "tiene", cantidad, "dígitos y su suma es", suma)


# Ejercicio 5
print("\nEjercicio 5: Generar 100 números reales aleatorios y mostrarlos ordenados.")
numeros_aleatorios = generar_numeros_aleatorios(100, 0, 100)
ordenar_lista(numeros_aleatorios)
mostrar_lista(numeros_aleatorios)


# Ejercicio 6
print("\nEjercicio 6: Buscar un apellido en una lista (recursivo).")
apellidos = ["Perez", "Sand", "Arlt", "Claymore", "Gomez"]
print("Lista de apellidos:", apellidos)
buscado = input("Ingrese el apellido a buscar: ")
if existe_apellido(apellidos, buscado, 0):
    print("El apellido", buscado, "está en la lista")
else:
    print("El apellido", buscado, "no está en la lista")


# Ejercicio 7
print("\nEjercicio 7: Contar cuántas veces aparece un número en una lista (recursivo).")
numeros = [3, 7, 3, 1, 9, 3, 7]
print("Lista de números:", numeros)
numero = leer_entero("Ingrese el número a contar: ")
apariciones = contar_apariciones(numero, numeros, 0)
print("El número", numero, "aparece", apariciones, "veces")


# Ejercicio 8
print("\nEjercicio 8: Diámetro y perímetro de un círculo.")
radio = leer_real("Ingrese el radio del círculo: ")
if radio < 0:
    print("Error: el radio no puede ser negativo")
else:
    print("Diámetro:", round(calcular_diametro(radio), 2))
    print("Perímetro:", round(calcular_perimetro(radio), 2))
