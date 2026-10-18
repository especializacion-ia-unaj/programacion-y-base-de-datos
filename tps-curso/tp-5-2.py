# Práctica 5 parte 2 - Sobreescritura y polimorfismo
# Temas: métodos polimórficos, sobreescritura, binding dinámico, getters y setters.

from personas import Persona, Alumno


# ---------------------------------------------------------------------------
# Ejercicio 2: jerarquía OperacionAritmetica con el método polimórfico evaluar.
# La superclase define la interfaz común y cada subclase la sobreescribe.
# ---------------------------------------------------------------------------

class OperacionAritmetica:
    def evaluar(self, num1, num2):
        """Este método debe ser redefinido en cada subclase."""
        pass

    def get_nombre(self):
        return "Operación"


class Suma(OperacionAritmetica):
    def evaluar(self, num1, num2):
        return num1 + num2

    def get_nombre(self):
        return "Suma"


class Resta(OperacionAritmetica):
    def evaluar(self, num1, num2):
        return num1 - num2

    def get_nombre(self):
        return "Resta"


class Multiplicacion(OperacionAritmetica):
    def evaluar(self, num1, num2):
        return num1 * num2

    def get_nombre(self):
        return "Multiplicación"


class Division(OperacionAritmetica):
    def evaluar(self, num1, num2):
        return num1 / num2

    def get_nombre(self):
        return "División"


# ---------------------------------------------------------------------------
# Ejercicio 3: empleados de un club
# ---------------------------------------------------------------------------

class Empleado:
    def __init__(self, nombre, sueldo_basico):
        self.__nombre = nombre
        self.__sueldo_basico = sueldo_basico

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_sueldo_basico(self):
        return self.__sueldo_basico

    def set_sueldo_basico(self, sueldo_basico):
        self.__sueldo_basico = sueldo_basico

    def calcularSueldoACobrar(self):
        """Interfaz común: cada tipo de empleado lo calcula de manera diferente."""
        return self.__sueldo_basico


class Jugador(Empleado):
    def __init__(self, nombre, sueldo_basico, partidos_jugados, goles):
        super().__init__(nombre, sueldo_basico)
        self.__partidos_jugados = partidos_jugados
        self.__goles = goles

    def get_partidos_jugados(self):
        return self.__partidos_jugados

    def set_partidos_jugados(self, partidos_jugados):
        self.__partidos_jugados = partidos_jugados

    def get_goles(self):
        return self.__goles

    def set_goles(self, goles):
        self.__goles = goles

    def calcular_promedio_goles(self):
        # Si no jugó partidos, el promedio es 0 (se evita dividir por cero)
        if self.__partidos_jugados == 0:
            return 0
        return self.__goles / self.__partidos_jugados

    def calcularSueldoACobrar(self):
        # Los atributos privados de Empleado se acceden con sus getters
        sueldo = self.get_sueldo_basico()
        if self.calcular_promedio_goles() > 0.5:
            sueldo = sueldo + self.get_sueldo_basico()   # plus de otro sueldo básico
        return sueldo


class Entrenador(Empleado):
    def __init__(self, nombre, sueldo_basico, campeonatos_ganados):
        super().__init__(nombre, sueldo_basico)
        self.__campeonatos_ganados = campeonatos_ganados

    def get_campeonatos_ganados(self):
        return self.__campeonatos_ganados

    def set_campeonatos_ganados(self, campeonatos_ganados):
        self.__campeonatos_ganados = campeonatos_ganados

    def calcular_plus(self):
        if self.__campeonatos_ganados >= 1 and self.__campeonatos_ganados <= 4:
            return 5000
        elif self.__campeonatos_ganados >= 5 and self.__campeonatos_ganados <= 10:
            return 30000
        elif self.__campeonatos_ganados > 10:
            return 50000
        else:
            return 0   # no ganó campeonatos

    def calcularSueldoACobrar(self):
        return self.get_sueldo_basico() + self.calcular_plus()


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
print("Ejercicio 1: Listado de personas y alumnos con el método polimórfico imprimirDatos().")
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
    # Ya no hace falta isinstance: cada objeto sabe cómo imprimirse
    print(str(numero_orden) + ")", end=" ")
    integrante.imprimirDatos()
    numero_orden = numero_orden + 1


# Ejercicio 2
print("\nEjercicio 2: Operaciones aritméticas con el método polimórfico evaluar().")
num1 = leer_real("Ingrese el primer número: ")
num2 = leer_real("Ingrese el segundo número: ")

operaciones = [Suma(), Resta(), Multiplicacion(), Division()]
for operacion in operaciones:
    # El mismo mensaje (evaluar) se ejecuta distinto según el objeto receptor
    try:
        print(operacion.get_nombre() + ":", round(operacion.evaluar(num1, num2), 2))
    except ZeroDivisionError:
        print(operacion.get_nombre() + ": no se puede dividir por cero")


# Ejercicio 3
print("\nEjercicio 3: Sueldos de los empleados del club.")
empleados = []

opcion = ""
while opcion != "3":
    print("\n1) Cargar un jugador")
    print("2) Cargar un entrenador")
    print("3) Terminar la carga")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        sueldo_basico = leer_real("Sueldo básico: $")
        partidos = leer_entero("Partidos jugados: ")
        goles = leer_entero("Goles anotados: ")
        empleados.append(Jugador(nombre, sueldo_basico, partidos, goles))
    elif opcion == "2":
        nombre = input("Nombre: ")
        sueldo_basico = leer_real("Sueldo básico: $")
        campeonatos = leer_entero("Campeonatos ganados: ")
        empleados.append(Entrenador(nombre, sueldo_basico, campeonatos))
    elif opcion != "3":
        print("Opción inválida")

print("\nSueldos a cobrar:")
for empleado in empleados:
    sueldo = empleado.calcularSueldoACobrar()   # polimorfismo
    print(empleado.get_nombre(), "-> $" + str(round(sueldo, 2)))
