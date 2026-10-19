# Trabajo Integrador - Programación y Base de Datos
#
# Programa principal. Uso:
#     python main.py                          (usa datos/estudiantes.csv)
#     python main.py ruta/al/archivo.csv      (usa otro archivo)
#     python main.py ruta/al/archivo.csv --sin-ventana   (solo guarda el gráfico)

import os
import sys

from curso import Curso
from lector_csv import leer_estudiantes
from reportes import (mostrar_detalle_estudiantes, mostrar_estadisticas_asignaturas,
                      mostrar_resumen_general, generar_grafico)

# Rutas por defecto, relativas a la carpeta de este archivo
CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_POR_DEFECTO = os.path.join(CARPETA_PROYECTO, "datos", "estudiantes.csv")
IMAGEN_GRAFICO = os.path.join(CARPETA_PROYECTO, "grafico_rendimiento.png")


def obtener_argumentos():
    """Retorna la ruta del CSV y si se debe abrir la ventana del gráfico."""
    ruta_archivo = ARCHIVO_POR_DEFECTO
    mostrar_ventana = True

    for argumento in sys.argv[1:]:
        if argumento == "--sin-ventana":
            mostrar_ventana = False
        else:
            ruta_archivo = argumento
    return ruta_archivo, mostrar_ventana


def main():
    ruta_archivo, mostrar_ventana = obtener_argumentos()
    print("Sistema de gestión académica")
    print("Archivo de datos:", ruta_archivo)

    # Etapa 1: leer el CSV y crear los objetos Estudiante
    try:
        estudiantes, errores = leer_estudiantes(ruta_archivo)
    except FileNotFoundError:
        print("Error: no se encontró el archivo", ruta_archivo)
        return
    except ValueError as error:
        print("Error en el formato del archivo:", error)
        return

    if len(errores) > 0:
        print("\nAtención: algunas filas no se pudieron procesar y se omitieron:")
        for error in errores:
            print("  -", error)

    if len(estudiantes) == 0:
        print("No hay estudiantes válidos para analizar.")
        return

    curso = Curso(os.path.basename(ruta_archivo))
    for estudiante in estudiantes:
        curso.agregar_estudiante(estudiante)

    # Etapas 2 a 4: análisis y presentación de resultados
    mostrar_detalle_estudiantes(curso)
    mostrar_estadisticas_asignaturas(curso)
    mostrar_resumen_general(curso)
    generar_grafico(curso, IMAGEN_GRAFICO, mostrar_ventana)


main()
