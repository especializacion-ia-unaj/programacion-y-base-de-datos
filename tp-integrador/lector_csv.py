# Módulo lector_csv
# Lee el archivo CSV con las notas y crea los objetos Estudiante.

import csv

from configuracion import ASIGNATURAS, NOTA_MINIMA, NOTA_MAXIMA
from estudiante import Estudiante

# Reemplazos para quitar las tildes de los encabezados
LETRAS_CON_TILDE = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u"}


def normalizar_texto(texto):
    """Pasa un encabezado a minúsculas, sin tildes, sin espacios en los extremos
    y con guiones bajos en lugar de espacios. Ej: " Programación " -> "programacion"."""
    texto = texto.strip().lower()
    resultado = ""
    for letra in texto:
        if letra in LETRAS_CON_TILDE:
            resultado = resultado + LETRAS_CON_TILDE[letra]
        elif letra == " ":
            resultado = resultado + "_"
        else:
            resultado = resultado + letra
    return resultado


def buscar_columnas(encabezado):
    """Retorna un diccionario {nombre de columna normalizado: posición}.

    Lanza ValueError si falta alguna columna obligatoria.
    """
    posiciones = {}
    for posicion in range(len(encabezado)):
        nombre_columna = normalizar_texto(encabezado[posicion])
        if nombre_columna != "":          # se ignoran columnas vacías (coma final)
            posiciones[nombre_columna] = posicion

    obligatorias = ["nombre", "apellido"]
    for clave, nombre in ASIGNATURAS:
        obligatorias.append(clave)

    faltantes = []
    for columna in obligatorias:
        if columna not in posiciones:
            faltantes.append(columna)

    if len(faltantes) > 0:
        raise ValueError("Faltan columnas en el archivo: " + ", ".join(faltantes))
    return posiciones


def convertir_nota(texto, asignatura):
    """Convierte el texto de una nota a número y verifica que esté en el rango válido."""
    try:
        nota = float(texto)
    except ValueError:
        raise ValueError("la nota de '" + asignatura + "' no es un número: '" + texto + "'")

    if nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
        raise ValueError("la nota de '" + asignatura + "' está fuera del rango " +
                         str(NOTA_MINIMA) + "-" + str(NOTA_MAXIMA) + ": " + texto)

    # Si la nota no tiene decimales se guarda como entero (8.0 -> 8)
    if nota == int(nota):
        nota = int(nota)
    return nota


def leer_estudiantes(ruta_archivo):
    """Lee el archivo CSV y retorna dos listas:
    - estudiantes: objetos Estudiante creados a partir de las filas válidas.
    - errores: mensajes de las filas que no se pudieron procesar.

    Lanza FileNotFoundError si el archivo no existe y ValueError si el
    encabezado no tiene las columnas necesarias.
    """
    estudiantes = []
    errores = []

    # utf-8-sig: también acepta archivos guardados desde Excel (con BOM)
    with open(ruta_archivo, "r", newline="", encoding="utf-8-sig") as archivo:
        lector = csv.reader(archivo)

        encabezado = next(lector, None)
        if encabezado is None:
            raise ValueError("El archivo está vacío")
        columnas = buscar_columnas(encabezado)

        numero_linea = 1
        for fila in lector:
            numero_linea = numero_linea + 1

            # Se saltean las líneas en blanco
            if len(fila) == 0 or "".join(fila).strip() == "":
                continue

            try:
                nombre = fila[columnas["nombre"]].strip()
                apellido = fila[columnas["apellido"]].strip()

                notas = {}
                for clave, nombre_asignatura in ASIGNATURAS:
                    texto_nota = fila[columnas[clave]].strip()
                    notas[clave] = convertir_nota(texto_nota, nombre_asignatura)

                estudiantes.append(Estudiante(nombre, apellido, notas))

            except IndexError:
                errores.append("Línea " + str(numero_linea) + ": faltan datos en la fila")
            except ValueError as error:
                errores.append("Línea " + str(numero_linea) + ": " + str(error))

    return estudiantes, errores
