# Módulo estudiante
# Clase Estudiante: guarda los datos personales y las notas de un estudiante, y sabe calcular su propio rendimiento académico.

from configuracion import NOTA_APROBACION, NOTA_APLAZO


class Estudiante:
    def __init__(self, nombre, apellido, notas):
        """Crea un estudiante.

        nombre, apellido: textos.
        notas: diccionario {clave de asignatura: nota}.
        """
        self.__nombre = nombre
        self.__apellido = apellido
        self.__notas = notas

    # ------------------------------------------------------------------
    # Getters y setters
    # ------------------------------------------------------------------

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_nombre_completo(self):
        return self.__nombre + " " + self.__apellido

    def get_notas(self):
        return self.__notas

    def get_nota(self, asignatura):
        """Retorna la nota de una asignatura (por su clave)."""
        return self.__notas[asignatura]

    def set_nota(self, asignatura, nota):
        self.__notas[asignatura] = nota

    # ------------------------------------------------------------------
    # Análisis del rendimiento académico
    # ------------------------------------------------------------------

    def calcular_prom(self):
        """Promedio CON aplazos: incluye todas las notas."""
        suma = 0
        for asignatura in self.__notas:
            suma = suma + self.__notas[asignatura]
        return suma / len(self.__notas)

    def calcular_prom_sin_aplazos(self):
        """Promedio SIN aplazos: no tiene en cuenta las notas menores a NOTA_APLAZO.

        Retorna None si todas las notas son aplazos (no hay nada para promediar).
        """
        suma = 0
        cantidad = 0
        for asignatura in self.__notas:
            nota = self.__notas[asignatura]
            if nota >= NOTA_APLAZO:
                suma = suma + nota
                cantidad = cantidad + 1

        if cantidad == 0:
            return None
        return suma / cantidad

    def contar_aplazos(self):
        """Cantidad de asignaturas con nota menor a NOTA_APLAZO."""
        cantidad = 0
        for asignatura in self.__notas:
            if self.__notas[asignatura] < NOTA_APLAZO:
                cantidad = cantidad + 1
        return cantidad

    def contar_asignaturas_aprobadas(self):
        """Cantidad de asignaturas con nota mayor o igual a NOTA_APROBACION."""
        cantidad = 0
        for asignatura in self.__notas:
            if self.__notas[asignatura] >= NOTA_APROBACION:
                cantidad = cantidad + 1
        return cantidad

    def esta_aprobado(self):
        """Criterio: el estudiante aprueba si su promedio con aplazos es >= NOTA_APROBACION."""
        return self.calcular_prom() >= NOTA_APROBACION

    def obtener_sit(self):
        """Retorna la situación académica como texto."""
        if self.esta_aprobado():
            return "Aprobado"
        else:
            return "Reprobado"

    def __str__(self):
        return (self.get_nombre_completo() + " - promedio " +
                str(round(self.calcular_prom(), 2)) + " - " + self.obtener_sit())
