# Módulo calendario (Práctica 4 - Ejercicio 3)
#
# Estado de un objeto Fecha: día, mes y año (atributos privados).
# Comportamiento: modificar la fecha, mostrarla en formato día/mes/año
# y convertirla a una cantidad aproximada de días.


class Fecha:
    def __init__(self, dia, mes, anio):
        # Al crear la fecha se inicializa con los valores recibidos.
        # Se reutiliza modificar() para no repetir las validaciones.
        self.modificar(dia, mes, anio)

    def modificar(self, dia, mes, anio):
        """Cambia la fecha. Lanza ValueError si el día o el mes no son válidos."""
        if dia < 1 or dia > 31:
            raise ValueError("El día debe estar entre 1 y 31")
        if mes < 1 or mes > 12:
            raise ValueError("El mes debe estar entre 1 y 12")
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    def get_dia(self):
        return self.__dia

    def get_mes(self):
        return self.__mes

    def get_anio(self):
        return self.__anio

    def mostrar(self):
        """Retorna la fecha en formato numérico día/mes/año."""
        return str(self.__dia) + "/" + str(self.__mes) + "/" + str(self.__anio)

    def __str__(self):
        return self.mostrar()

    def a_dias(self):
        """Convierte la fecha a días según la ayuda del enunciado (año*365 + mes*30 + día)."""
        return self.__anio * 365 + self.__mes * 30 + self.__dia
