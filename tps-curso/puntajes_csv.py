# Módulo puntajes_csv (Práctica 6 - Problema 1 A)
# Guarda y lee puntajes en un archivo CSV.
# Cada puntaje es una tupla (nombre, puntaje, tiempo).

import csv


def guardar_puntajes(nombre_archivo, puntajes):
    """Guarda la lista de puntajes en el archivo CSV (lo sobreescribe si existe).

    Pre: puntajes es una lista de tuplas (nombre, puntaje, tiempo).
    Post: el archivo contiene un encabezado y una línea por cada puntaje.
    """
    # with cierra el archivo automáticamente, aunque ocurra un error
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre", "Puntaje", "Tiempo"])
        for nombre, puntaje, tiempo in puntajes:
            escritor.writerow([nombre, puntaje, tiempo])


def recuperar_puntajes(nombre_archivo):
    """Lee el archivo CSV, imprime cada puntaje y retorna la lista de puntajes.

    Pre: el archivo fue generado con guardar_puntajes.
    Post: retorna una lista de tuplas (nombre, puntaje, tiempo) con el puntaje como entero.
    """
    puntajes = []
    with open(nombre_archivo, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)   # se saltea la línea de encabezado
        for fila in lector:
            nombre = fila[0]
            puntaje = int(fila[1])
            tiempo = fila[2]
            print(nombre, "-", puntaje, "puntos -", tiempo)
            puntajes.append((nombre, puntaje, tiempo))
    return puntajes
