# Módulo reportes
# Muestra por pantalla los resultados del análisis y genera el gráfico de barras.

import matplotlib.pyplot as plt

from configuracion import ASIGNATURAS, NOTA_APROBACION, NOTA_APLAZO

COLOR_BARRAS = "#2a78d6"
COLOR_TEXTO = "#333333"
ANCHO_LINEA = 106

# Nombres cortos para las columnas de la tabla de estudiantes
ABREVIATURAS = {
    "programacion": "Prog",
    "bases_d_datos": "BD",
    "estadistica": "Estad",
    "arq_nube": "Nube",
    "ap_automatico": "ApAut",
    "cap_informacion": "CapInf",
}


def imprimir_titulo(titulo):
    print()
    print("=" * ANCHO_LINEA)
    print(titulo)
    print("=" * ANCHO_LINEA)


def formatear_promedio(promedio):
    """Muestra un promedio con 2 decimales, o '-' si no existe (None)."""
    if promedio is None:
        return "-"
    return format(promedio, ".2f")


# ----------------------------------------------------------------------
# 1. Información detallada de cada estudiante
# ----------------------------------------------------------------------

def mostrar_detalle_estudiantes(curso):
    imprimir_titulo("INFORMACIÓN DETALLADA DE CADA ESTUDIANTE")

    # Encabezado de la tabla: una columna corta por asignatura
    encabezado = f"{'Estudiante':<22}"
    for clave, nombre in ASIGNATURAS:
        encabezado = encabezado + f"{ABREVIATURAS[clave]:>7}"
    encabezado = encabezado + f"{'Prom':>8}{'Sin apl.':>10}{'Aplazos':>9}  {'Situación':<10}"
    print(encabezado)
    print("-" * ANCHO_LINEA)

    for estudiante in curso.get_estudiantes():
        linea = f"{estudiante.get_nombre_completo():<22}"
        for clave, nombre in ASIGNATURAS:
            linea = linea + f"{estudiante.get_nota(clave):>7}"
        linea = linea + f"{formatear_promedio(estudiante.calcular_prom()):>8}"
        linea = linea + f"{formatear_promedio(estudiante.calcular_prom_sin_aplazos()):>10}"
        linea = linea + f"{estudiante.contar_aplazos():>9}"
        linea = linea + f"  {estudiante.obtener_sit():<10}"
        print(linea)

    print("-" * ANCHO_LINEA)
    referencias = "Referencias:"
    for clave, nombre in ASIGNATURAS:
        referencias = referencias + " " + ABREVIATURAS[clave] + " = " + nombre + "."
    print(referencias)
    print(f"Prom = promedio con aplazos. Sin apl. = promedio sin contar las notas menores a {NOTA_APLAZO}.")
    print(f"Situación: Aprobado si el promedio con aplazos es mayor o igual a {NOTA_APROBACION}.")


# ----------------------------------------------------------------------
# 2. Estadísticas comparativas entre asignaturas
# ----------------------------------------------------------------------

def mostrar_estadisticas_asignaturas(curso):
    imprimir_titulo("ESTADÍSTICAS POR ASIGNATURA")

    print(f"{'Asignatura':<28}{'Promedio':>10}{'% aprobados':>14}")
    print("-" * 52)
    for clave, nombre in ASIGNATURAS:
        promedio = curso.calcular_promedio_asignatura(clave)
        porcentaje = curso.calcular_porcentaje_aprobados_asignatura(clave)
        print(f"{nombre:<28}{promedio:>10.2f}{porcentaje:>13.1f}%")
    print("-" * 52)

    mayor = curso.obtener_asignatura_mayor_rendimiento()
    menor = curso.obtener_asignatura_menor_rendimiento()
    print("Asignatura con MAYOR rendimiento:", buscar_nombre_asignatura(mayor),
          f"(promedio {curso.calcular_promedio_asignatura(mayor):.2f})")
    print("Asignatura con MENOR rendimiento:", buscar_nombre_asignatura(menor),
          f"(promedio {curso.calcular_promedio_asignatura(menor):.2f})")


def buscar_nombre_asignatura(clave_buscada):
    """Retorna el nombre para mostrar de una asignatura a partir de su clave."""
    for clave, nombre in ASIGNATURAS:
        if clave == clave_buscada:
            return nombre
    return clave_buscada


# ----------------------------------------------------------------------
# 3. Resumen general del grupo
# ----------------------------------------------------------------------

def mostrar_resumen_general(curso):
    imprimir_titulo("RESUMEN GENERAL DEL GRUPO")

    total = curso.cantidad_estudiantes()
    aprobados = curso.contar_aprobados()
    reprobados = total - aprobados

    print("Curso:", curso.get_nombre())
    print("Cantidad de estudiantes:", total)
    print("Aprobados:", aprobados)
    print("Reprobados:", reprobados)
    print(f"Porcentaje de aprobación general: {curso.calcular_porcentaje_aprobacion():.1f}%")
    print(f"Promedio general del grupo: {curso.calcular_promedio_general():.2f}")


# ----------------------------------------------------------------------
# 4. Gráfico de barras
# ----------------------------------------------------------------------

def agregar_valores_sobre_barras(eje, barras, valores, sufijo):
    """Escribe el valor de cada barra encima de ella."""
    for posicion in range(len(barras)):
        barra = barras[posicion]
        x = barra.get_x() + barra.get_width() / 2
        y = barra.get_height()
        texto = format(valores[posicion], ".1f") + sufijo
        eje.text(x, y, texto, ha="center", va="bottom", fontsize=9, color=COLOR_TEXTO)


def generar_grafico(curso, ruta_imagen, mostrar_ventana):
    """Genera un gráfico con dos paneles de barras:
    - promedio por asignatura (con una línea en la nota de aprobación),
    - porcentaje de estudiantes aprobados por asignatura.
    Guarda la imagen en ruta_imagen y, si mostrar_ventana es True, la muestra.
    """
    nombres = []
    promedios = []
    porcentajes = []
    for clave, nombre in ASIGNATURAS:
        nombres.append(nombre.replace(" ", "\n", 1))   # nombres en dos líneas
        promedios.append(curso.calcular_promedio_asignatura(clave))
        porcentajes.append(curso.calcular_porcentaje_aprobados_asignatura(clave))

    figura, (eje_promedios, eje_aprobados) = plt.subplots(1, 2, figsize=(14, 5.5))

    # Panel 1: promedio por asignatura
    barras = eje_promedios.bar(nombres, promedios, color=COLOR_BARRAS, width=0.6)
    agregar_valores_sobre_barras(eje_promedios, barras, promedios, "")
    eje_promedios.axhline(NOTA_APROBACION, color="#888888", linestyle="--", linewidth=1,
                          label="Nota de aprobación (" + str(NOTA_APROBACION) + ")")
    eje_promedios.legend(loc="upper left", frameon=False, fontsize=9)
    eje_promedios.set_ylim(0, 10.5)
    eje_promedios.set_ylabel("Promedio")
    eje_promedios.set_title("Promedio por asignatura")

    # Panel 2: porcentaje de aprobados por asignatura
    barras = eje_aprobados.bar(nombres, porcentajes, color=COLOR_BARRAS, width=0.6)
    agregar_valores_sobre_barras(eje_aprobados, barras, porcentajes, "%")
    eje_aprobados.set_ylim(0, 110)
    eje_aprobados.set_ylabel("% de estudiantes con nota >= " + str(NOTA_APROBACION))
    eje_aprobados.set_title("Porcentaje de aprobados por asignatura")

    # Estilo común: ejes y grilla discretos
    for eje in (eje_promedios, eje_aprobados):
        eje.spines["top"].set_visible(False)
        eje.spines["right"].set_visible(False)
        eje.grid(axis="y", color="#e5e5e5", linewidth=0.8)
        eje.set_axisbelow(True)
        eje.tick_params(axis="x", labelsize=9)

    figura.suptitle(f"Rendimiento del grupo - {curso.cantidad_estudiantes()} estudiantes - "
                    f"aprobación general {curso.calcular_porcentaje_aprobacion():.1f}%",
                    fontsize=13)
    figura.tight_layout()
    figura.savefig(ruta_imagen, dpi=120)
    print("\nGráfico guardado en:", ruta_imagen)

    if mostrar_ventana:
        plt.show()
    plt.close(figura)
