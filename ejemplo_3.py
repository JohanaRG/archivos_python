# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv

"""
    # Profe:
    # - Leer el archivo CSV alturas
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo
    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle
"""

def data_csv(archivo):
    """Recibe: El archivo a leer
       Objetivo: Leer el archivo csv y obtener la data.
       Salida: data -> lista de diccionarios
    """

    with open(archivo) as csvfile:
        data = list(csv.DictReader(csvfile))

    return data


def get_alturas(datos, genero):
    """Recibe: Datos y genero 
       Objetivo: Recorrer todas las filas del archivo CSV
        en cada iteración obtener la altura del genero objetivo.
        Acumule el valor y la cantidad de alturas.
       Salida: Sumatoria y cantidad de alturas.
    """
    sumatoria = 0
    cantidad = 0

    # for i in range(len(datos)):
    #     if genero == datos[i]["genero"]:
    #         sumatoria += float(datos[i]["altura"])
    #         cantidad += 1

    # ---------------------------------------------
    for fila in datos:
        if genero == fila["genero"]:
            sumatoria += float(fila["altura"])
            cantidad += 1


    return sumatoria, cantidad


def altura_promedio(genero):
    print("¡Ejemplo integrador!")
    # Esta función recibe el género del cual
    # se debe calcular la altura promedio
    # puede ser --> femenino o masculino

    # Utilizar el archivo CSV "alturas",
    # el cual posee dos columnas:
    # - genero
    # - altura

    # Profe:
    # - Leer el archivo CSV
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo
    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle

    # --- Comience aquí a desarrollar su código ---

    data = data_csv('alturas.csv')

    sumatoria, cantidad = get_alturas(data,genero)

    promedio =  sumatoria / cantidad

    print(f'El promedio de alturas para el genero: {genero} es: {round(promedio,2)}')
    print(f'El promedio de alturas para el genero: {genero} es: {promedio:.2f}')


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    altura_promedio("masculino")
