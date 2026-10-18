# Práctica 2 - Estructuras iterativas y colecciones
# Temas: while, for, break, cadenas, listas, diccionarios y conjuntos.


# Ejercicio 1
print("Ejercicio 1: Mostrar la cantidad de caracteres de cada cadena y la longitud promedio.")
print("Ingrese cadenas de caracteres. Para terminar, presione Enter sin escribir nada.")

cantidad_palabras = 0
total_caracteres = 0

cadena = input("Ingrese una cadena: ")
while cadena != "":
    longitud = len(cadena)
    print("La cadena", cadena, "tiene", longitud, "caracteres")
    cantidad_palabras = cantidad_palabras + 1
    total_caracteres = total_caracteres + longitud
    cadena = input("Ingrese una cadena: ")

# Si no se ingresó ninguna cadena no se puede dividir por cero
if cantidad_palabras > 0:
    promedio = total_caracteres / cantidad_palabras
    print("Longitud promedio de las palabras ingresadas:", round(promedio, 2))
else:
    print("No se ingresó ninguna cadena")


# Ejercicio 2
print("\nEjercicio 2: Multiplicar un número por 365 y mostrar el resultado dígito por dígito.")
numero = int(input("Ingrese un número entero: "))
resultado = numero * 365
print("Resultado:", resultado)

# Se convierte a string para poder recorrer los dígitos.
# Si el número es negativo se descarta el signo "-".
texto_resultado = str(resultado)
if texto_resultado[0] == "-":
    texto_resultado = texto_resultado[1:]

print("Dígitos desde el menos significativo al más significativo:")
# Se recorren las posiciones desde la última hasta la primera (paso -1)
for posicion in range(len(texto_resultado) - 1, -1, -1):
    print(texto_resultado[posicion])


# Ejercicio 3
print("\nEjercicio 3: Obtener el menor y el mayor de una secuencia de números que termina en 0.")
numero = int(input("Ingrese un número (0 para terminar): "))

if numero == 0:
    print("No se ingresaron números")
else:
    # El primer número ingresado es, por ahora, el menor y el mayor
    menor = numero
    mayor = numero

    while numero != 0:
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero
        numero = int(input("Ingrese un número (0 para terminar): "))

    print("Menor:", menor)
    print("Mayor:", mayor)

    # Valores enteros comprendidos entre el mínimo y el máximo (sin incluirlos)
    valores_intermedios = []
    for valor in range(menor + 1, mayor):
        valores_intermedios.append(valor)
    print("Valores comprendidos entre", menor, "y", mayor, ":", valores_intermedios)


# Ejercicio 4
print("\nEjercicio 4: Determinar si dos palabras son palíndromos entre ellas.")
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

# a) Recorriendo cada palabra y comparando carácter por carácter:
#    el primer carácter de palabra1 con el último de palabra2, y así sucesivamente.
son_palindromos = True
if len(palabra1) != len(palabra2):
    son_palindromos = False
else:
    ultima_posicion = len(palabra2) - 1
    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[ultima_posicion - i]:
            son_palindromos = False
            break   # ya encontramos una diferencia, no hace falta seguir

if son_palindromos:
    print("a) Recorriendo: son palíndromos entre ellas")
else:
    print("a) Recorriendo: no son palíndromos entre ellas")

# b) Usando funciones predefinidas de lista:
#    se convierte cada palabra en lista, se invierte la segunda y se comparan.
lista1 = list(palabra1)
lista2 = list(palabra2)
lista2.reverse()

if lista1 == lista2:
    print("b) Con funciones de lista: son palíndromos entre ellas")
else:
    print("b) Con funciones de lista: no son palíndromos entre ellas")


# Ejercicio 5
print("\nEjercicio 5: Contar productos vendidos por marca en un kiosco.")
print("Ingrese la marca de cada producto vendido. Para terminar, presione Enter sin escribir nada.")

ventas_por_marca = {}     # diccionario: marca -> cantidad vendida
marcas_distintas = set()  # conjunto: no guarda marcas repetidas

marca = input("Marca del producto vendido: ")
while marca != "":
    # Se pasa a minúsculas para que "Coca" y "coca" cuenten como la misma marca
    marca = marca.strip().lower()

    if marca in ventas_por_marca:
        ventas_por_marca[marca] = ventas_por_marca[marca] + 1
    else:
        ventas_por_marca[marca] = 1

    marcas_distintas.add(marca)
    marca = input("Marca del producto vendido: ")

print("\nListado de ventas del día:")
for marca, cantidad in ventas_por_marca.items():
    print(marca, "->", cantidad, "productos")

print("Cantidad de marcas diferentes:", len(marcas_distintas))
