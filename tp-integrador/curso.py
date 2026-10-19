# Módulo curso
# Clase Curso: agrupa a los estudiantes y calcula las estadísticas generales del grupo.

from configuracion import ASIGNATURAS, NOTA_APROBACION


class Curso:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__estudiantes = []   # lista de objetos Estudiante

    def get_nombre(self):
        return self.__nombre

    def get_estudiantes(self):
        return self.__estudiantes

    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    def cantidad_estudiantes(self):
        return len(self.__estudiantes)

    # ------------------------------------------------------------------
    # Estadísticas por asignatura
    # ------------------------------------------------------------------

    def calcular_promedio_asignatura(self, asignatura):
        """Promedio de todas las notas del curso en una asignatura."""
        suma = 0
        for estudiante in self.__estudiantes:
            suma = suma + estudiante.get_nota(asignatura)
        return suma / len(self.__estudiantes)

    def calcular_porcentaje_aprobados_asignatura(self, asignatura):
        """Porcentaje de estudiantes con nota >= NOTA_APROBACION en una asignatura."""
        aprobados = 0
        for estudiante in self.__estudiantes:
            if estudiante.get_nota(asignatura) >= NOTA_APROBACION:
                aprobados = aprobados + 1
        return aprobados * 100 / len(self.__estudiantes)

    def obtener_asignatura_mayor_rendimiento(self):
        """Retorna la clave de la asignatura con el promedio más alto."""
        mejor_asignatura = ASIGNATURAS[0][0]
        mejor_promedio = self.calcular_promedio_asignatura(mejor_asignatura)

        for clave, nombre in ASIGNATURAS:
            promedio = self.calcular_promedio_asignatura(clave)
            if promedio > mejor_promedio:
                mejor_promedio = promedio
                mejor_asignatura = clave
        return mejor_asignatura

    def obtener_asignatura_menor_rendimiento(self):
        """Retorna la clave de la asignatura con el promedio más bajo."""
        peor_asignatura = ASIGNATURAS[0][0]
        peor_promedio = self.calcular_promedio_asignatura(peor_asignatura)

        for clave, nombre in ASIGNATURAS:
            promedio = self.calcular_promedio_asignatura(clave)
            if promedio < peor_promedio:
                peor_promedio = promedio
                peor_asignatura = clave
        return peor_asignatura

    # ------------------------------------------------------------------
    # Estadísticas generales del grupo
    # ------------------------------------------------------------------

    def contar_aprobados(self):
        cantidad = 0
        for estudiante in self.__estudiantes:
            if estudiante.esta_aprobado():
                cantidad = cantidad + 1
        return cantidad

    def calcular_porcentaje_aprobacion(self):
        """Porcentaje de estudiantes aprobados sobre el total del curso."""
        return self.contar_aprobados() * 100 / len(self.__estudiantes)

    def calcular_promedio_general(self):
        """Promedio de los promedios (con aplazos) de todos los estudiantes."""
        suma = 0
        for estudiante in self.__estudiantes:
            suma = suma + estudiante.calcular_prom()
        return suma / len(self.__estudiantes)
