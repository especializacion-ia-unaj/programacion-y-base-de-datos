# Práctica 5 parte 1 - Herencia
# Temas: subclases, super(), atributos privados, isinstance y jerarquía de clases.

from personas import Persona, Alumno


# ---------------------------------------------------------------------------
# Ejercicio 3: jerarquía OperacionAritmetica
# Cada subclase tiene su propio método, con un nombre distinto.
# ---------------------------------------------------------------------------

class OperacionAritmetica:
    pass


class Suma(OperacionAritmetica):
    def sumar(self, num1, num2):
        return num1 + num2


class Resta(OperacionAritmetica):
    def restar(self, num1, num2):
        return num1 - num2


class Multiplicacion(OperacionAritmetica):
    def multiplicar(self, num1, num2):
        return num1 * num2


class Division(OperacionAritmetica):
    def dividir(self, num1, num2):
        # Si num2 es 0 se lanza ZeroDivisionError y lo maneja quien la invoca
        return num1 / num2


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


# ===========================================================================
# Programa principal
# ===========================================================================

# Ejercicio 1
print("Ejercicio 1: Cargar alumnos y mostrar el listado.")
print("Ingrese los datos de cada alumno. Para terminar, deje el nombre vacío.")

alumnos = []
nombre = input("Nombre y apellido: ")
while nombre != "":
    edad = leer_entero("Edad: ")
    dni = leer_entero("DNI: ")
    promedio = leer_real("Promedio: ")
    alumnos.append(Alumno(nombre, edad, dni, promedio))
    nombre = input("Nombre y apellido: ")

print("\nListado de alumnos:")
numero_orden = 1
for alumno in alumnos:
    print(str(numero_orden) + ") ALUMNO:", alumno)
    numero_orden = numero_orden + 1


# Ejercicio 2
print("\nEjercicio 2: Cargar personas y alumnos en una misma lista.")
integrantes = []

opcion = ""
while opcion != "3":
    print("\n1) Cargar una persona")
    print("2) Cargar un alumno")
    print("3) Terminar la carga")
    opcion = input("Elija una opción: ")

    if opcion == "1" or opcion == "2":
        nombre = input("Nombre y apellido: ")
        edad = leer_entero("Edad: ")
        dni = leer_entero("DNI: ")
        if opcion == "1":
            integrantes.append(Persona(nombre, edad, dni))
        else:
            promedio = leer_real("Promedio: ")
            integrantes.append(Alumno(nombre, edad, dni, promedio))
    elif opcion != "3":
        print("Opción inválida")

print("\nListado:")
numero_orden = 1
for integrante in integrantes:
    # Se pregunta primero por Alumno: un Alumno también ES una Persona,
    # así que isinstance(alumno, Persona) también daría True.
    if isinstance(integrante, Alumno):
        print(str(numero_orden) + ") ALUMNO:", integrante)
    elif isinstance(integrante, Persona):
        print(str(numero_orden) + ") PERSONA:", integrante)
    numero_orden = numero_orden + 1


# Ejercicio 3
print("\nEjercicio 3: Jerarquía de operaciones aritméticas.")
num1 = leer_real("Ingrese el primer número: ")
num2 = leer_real("Ingrese el segundo número: ")

suma = Suma()
resta = Resta()
multiplicacion = Multiplicacion()
division = Division()

print("Suma:", suma.sumar(num1, num2))
print("Resta:", resta.restar(num1, num2))
print("Multiplicación:", multiplicacion.multiplicar(num1, num2))
try:
    print("División:", round(division.dividir(num1, num2), 2))
except ZeroDivisionError:
    print("División: no se puede dividir por cero")
