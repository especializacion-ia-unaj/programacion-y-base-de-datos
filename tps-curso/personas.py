# Módulo personas
# Persona: Práctica 4 - Ejercicio 2
# Alumno:  Práctica 5 (subclase de Persona)
# imprimirDatos: Práctica 5 parte 2 - Ejercicio 1 (método polimórfico)


class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Getters y setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    def __str__(self):
        # Formato pedido: Juan Perez (40) 2098745
        return self.__nombre + " (" + str(self.__edad) + ") " + str(self.__dni)

    def imprimirDatos(self):
        print("PERSONA:", self)


class Alumno(Persona):
    def __init__(self, nombre, edad, dni, promedio):
        super().__init__(nombre, edad, dni)   # inicializa lo heredado de Persona
        self.__promedio = promedio            # atributo propio y privado

    def get_promedio(self):
        return self.__promedio

    def set_promedio(self, promedio):
        self.__promedio = promedio

    def __str__(self):
        # Se reutiliza el __str__ de Persona y se agrega el promedio
        return super().__str__() + " " + str(self.__promedio)

    def imprimirDatos(self):
        # Sobreescritura: el mismo mensaje responde distinto en Alumno
        print("ALUMNO:", self)
