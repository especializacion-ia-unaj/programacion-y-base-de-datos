# Práctica 6 - Archivos, matrices (imágenes) y árboles
# Temas: archivos CSV, persistencia, módulos, matrices con NumPy, bucles anidados y árboles.
#
# Requiere el archivo puntajes_csv.py en la misma carpeta y las librerías:
#     pip install matplotlib numpy scikit-image anytree

import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from anytree import Node, RenderTree

from puntajes_csv import guardar_puntajes, recuperar_puntajes


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


# ---------------------------------------------------------------------------
# Problema 2: conversión de una imagen color a escala de grises
# ---------------------------------------------------------------------------

def convertir_a_grises(imagen):
    """Recibe una imagen RGB (matriz alto x ancho x canales con valores 0-1)
    y retorna una matriz alto x ancho con el promedio de los tres canales."""
    h, w, c = imagen.shape            # h = filas, w = columnas, c = canales
    imagen_gris = np.zeros((h, w))    # matriz de ceros donde se arma el resultado

    for i in range(h):
        for j in range(w):
            rojo = imagen[i][j][0]
            verde = imagen[i][j][1]
            azul = imagen[i][j][2]
            imagen_gris[i][j] = (rojo + verde + azul) / 3
    return imagen_gris


def mostrar_canales(imagen):
    """Muestra cada canal de color por separado."""
    titulos = ["Canal Rojo", "Canal Verde", "Canal Azul"]
    for canal in range(3):
        plt.figure()
        plt.imshow(imagen[:, :, canal], vmin=0, vmax=1)
        plt.title(titulos[canal])


# ---------------------------------------------------------------------------
# Problema 3: árbol genealógico
# ---------------------------------------------------------------------------

def armar_arbol_dos_generaciones():
    """a) Arma un árbol genealógico de dos generaciones ingresando los datos por teclado."""
    apellido = input("Apellido de la familia: ")
    raiz = Node("Familia " + apellido)

    print("Primera generación. Para terminar, deje el nombre vacío.")
    nombre = input("  Integrante de la primera generación: ")
    while nombre != "":
        integrante = Node(nombre, parent=raiz)

        print("  Hijos de", nombre + ". Para terminar, deje el nombre vacío.")
        nombre_hijo = input("    Hijo/a de " + nombre + ": ")
        while nombre_hijo != "":
            Node(nombre_hijo, parent=integrante)   # segunda generación
            nombre_hijo = input("    Hijo/a de " + nombre + ": ")

        nombre = input("  Integrante de la primera generación: ")
    return raiz


def cargar_descendientes(padre, generacion_actual, total_generaciones):
    """b) Carga en forma recursiva los descendientes de 'padre'.

    Caso base: se alcanzó la cantidad de generaciones pedida -> no se piden más hijos.
    Caso recursivo: por cada hijo ingresado se cargan sus propios descendientes
    en la generación siguiente.
    """
    if generacion_actual > total_generaciones:
        return

    sangria = "  " * generacion_actual
    print(sangria + "Generación", generacion_actual, "- hijos de", padre.name,
          "(deje vacío para terminar)")
    nombre = input(sangria + "Nombre: ")
    while nombre != "":
        hijo = Node(nombre, parent=padre)
        cargar_descendientes(hijo, generacion_actual + 1, total_generaciones)
        nombre = input(sangria + "Nombre: ")


def mostrar_arbol(raiz):
    for prefijo, relleno, nodo in RenderTree(raiz):
        print(prefijo + nodo.name)


# ===========================================================================
# Programa principal
# ===========================================================================

# Problema 1 B
print("Problema 1: Guardar y leer puntajes en un archivo CSV.")
print("Ingrese los puntajes. Para terminar, deje el nombre vacío.")

puntajes = []
nombre = input("Nombre del jugador: ")
while nombre != "":
    puntaje = leer_entero("Puntaje: ")
    tiempo = input("Tiempo (mm:ss): ")
    puntajes.append((nombre, puntaje, tiempo))
    nombre = input("Nombre del jugador: ")

nombre_archivo = "puntajes.csv"
guardar_puntajes(nombre_archivo, puntajes)
print("\nContenido del archivo", nombre_archivo + ":")
recuperar_puntajes(nombre_archivo)


# Problema 2
print("\nProblema 2: Convertir una imagen color a escala de grises.")
plt.rcParams["image.cmap"] = "gray"   # para ver las imágenes en escala de grises
nombre_imagen = input("Ingrese el nombre del archivo de imagen (ej: foto.jpg): ")

try:
    # imread devuelve enteros 0-255; al dividir por 255 quedan reales entre 0 y 1
    imagen = io.imread(nombre_imagen) / 255.0
except FileNotFoundError:
    print("No se encontró el archivo", nombre_imagen)
else:
    print("Dimensiones de la imagen:", imagen.shape)

    if len(imagen.shape) != 3 or imagen.shape[2] < 3:
        print("La imagen no es a color (RGB)")
    else:
        plt.figure()
        plt.imshow(imagen, vmin=0, vmax=1)
        plt.title("Imagen original")

        mostrar_canales(imagen)

        imagen_gris = convertir_a_grises(imagen)
        plt.figure()
        plt.imshow(imagen_gris, vmin=0, vmax=1)
        plt.title("Escala de grises")

        print("Cierre las ventanas de las imágenes para continuar.")
        plt.show()


# Problema 3 a)
print("\nProblema 3 a): Árbol genealógico de dos generaciones.")
arbol = armar_arbol_dos_generaciones()
print("\nÁrbol genealógico:")
mostrar_arbol(arbol)


# Problema 3 b)
print("\nProblema 3 b): Árbol genealógico con la cantidad de generaciones que se desee.")
apellido = input("Apellido de la familia: ")
total_generaciones = leer_entero("¿Cuántas generaciones quiere cargar?: ")
raiz = Node("Familia " + apellido)
cargar_descendientes(raiz, 1, total_generaciones)
print("\nÁrbol genealógico:")
mostrar_arbol(raiz)
