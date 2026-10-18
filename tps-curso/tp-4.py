# Práctica 4 - Programación Orientada a Objetos
# Temas: clases, constructor, atributos privados, métodos, __str__ y módulos.
# Requiere los archivos personas.py y calendario.py en la misma carpeta.

from personas import Persona
from calendario import Fecha


# ---------------------------------------------------------------------------
# Ejercicio 1: clase Temperatura
# ---------------------------------------------------------------------------

class Temperatura:
    def calcularCelsius(self, fahrenheit):
        """Recibe una temperatura en °F y retorna su equivalente en °C."""
        return (fahrenheit - 32) * 5 / 9

    def calcularFahrenheit(self, celsius):
        """Recibe una temperatura en °C y retorna su equivalente en °F."""
        return celsius * 9 / 5 + 32


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


def leer_fecha(titulo):
    """Pide día, mes y año, y retorna un objeto Fecha válido."""
    print(titulo)
    while True:
        dia = leer_entero("  Día: ")
        mes = leer_entero("  Mes: ")
        anio = leer_entero("  Año: ")
        try:
            return Fecha(dia, mes, anio)
        except ValueError as error:
            print("  Fecha inválida:", error, "- vuelva a ingresarla.")


# ===========================================================================
# Programa principal
# ===========================================================================

# Ejercicio 1
print("Ejercicio 1: Conversión de temperaturas con la clase Temperatura.")
conversor = Temperatura()

temp_fahrenheit = leer_real("Ingrese una temperatura en °F: ")
temp_celsius = leer_real("Ingrese una temperatura en °C: ")

print(temp_fahrenheit, "°F equivalen a", round(conversor.calcularCelsius(temp_fahrenheit), 2), "°C")
print(temp_celsius, "°C equivalen a", round(conversor.calcularFahrenheit(temp_celsius), 2), "°F")


# Ejercicio 2
print("\nEjercicio 2: Cargar personas y mostrar el listado.")
print("Ingrese los datos de cada persona. Para terminar, deje el nombre vacío.")

personas = []
nombre = input("Nombre y apellido: ")
while nombre != "":
    edad = leer_entero("Edad: ")
    dni = leer_entero("DNI: ")
    personas.append(Persona(nombre, edad, dni))
    nombre = input("Nombre y apellido: ")

print("\nListado de personas:")
numero_orden = 1
for persona in personas:
    print(str(numero_orden) + ")", persona)   # print usa el método __str__
    numero_orden = numero_orden + 1


# Ejercicio 3
print("\nEjercicio 3: Diferencia en días entre dos fechas.")
fecha1 = leer_fecha("Primera fecha:")
fecha2 = leer_fecha("Segunda fecha:")

diferencia = abs(fecha1.a_dias() - fecha2.a_dias())
print("Entre", fecha1.mostrar(), "y", fecha2.mostrar(), "hay", diferencia, "días (aproximadamente)")

# Ejemplo de uso del método para modificar la fecha
fecha1.modificar(1, 1, 2026)
print("La primera fecha se modificó a:", fecha1)
