# Ejercicio 1
print("Ejercicio 1: Calcular promedio de calificaciones y determinar si el estudiante aprobó o no.")
print("Ingrese tres calificaciones (0-10) para calcular el promedio y determinar si el estudiante aprobó o no.")
nota1 = float(input("Ingrese la primera calificación (0-10): "))
nota2 = float(input("Ingrese la segunda calificación (0-10): "))
nota3 = float(input("Ingrese la tercera calificación (0-10): "))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
    promedio = (nota1 + nota2 + nota3) / 3
    print("Promedio:", round(promedio, 2))
    if promedio >= 6:
        print("El estudiante aprobó")
    else:
        print("El estudiante no aprobó")
else:
    print("Error: todas las calificaciones deben estar entre 0 y 10")


# Ejercicio 2
print("\nEjercicio 2: Convertir temperaturas entre Celsius y Fahrenheit.")
print("Seleccione la opción de conversión:")
print("1) Celsius a Fahrenheit")
print("2) Fahrenheit a Celsius")
opcion = input("Elija una opción (1 o 2): ")

if opcion == "1":
    celsius = float(input("Ingrese la temperatura en °C: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "°C equivalen a", round(fahrenheit, 2), "°F")
elif opcion == "2":
    fahrenheit = float(input("Ingrese la temperatura en °F: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit, "°F equivalen a", round(celsius, 2), "°C")
else:
    print("Opción inválida")

# Ejercicio 3
print("\nEjercicio 3: Determinar si un número es positivo, negativo o cero, y si es par o impar.")
print("Ingrese un número entero para determinar su signo y paridad.")
numero = int(input("Ingrese un número entero: "))

if numero == 0:
    print("El número es cero")
else:
    if numero > 0:
        signo = "positivo"
    else:
        signo = "negativo"

    if numero % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"

    print("El número es", signo, "y", paridad)

# Ejercicio 4
print("\nEjercicio 4: Calcular descuento según el monto de la compra.")
print("Ingrese el monto de la compra para calcular el descuento.")
monto = float(input("Ingrese el monto de la compra: $"))

if monto < 0:
    print("Error: el monto no puede ser negativo")
else:
    if monto < 1000:
        porcentaje = 0
    elif monto <= 5000:
        porcentaje = 10
    else:
        porcentaje = 20

    descuento = monto * porcentaje / 100
    precio_final = monto - descuento
    print("Descuento aplicado:", porcentaje, "%  ($" + str(round(descuento, 2)) + ")")
    print("Precio final: $" + str(round(precio_final, 2)))

# Ejercicio 5
print("\nEjercicio 5: Determinar si un año es bisiesto.")
print("Ingrese un año para determinar si es bisiesto o no.")
anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(anio, "es bisiesto")
else:
    print(anio, "no es bisiesto")