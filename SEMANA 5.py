# Programa que calcula el área de diferentes figuras geométricas
# El usuario puede elegir entre círculo, cuadrado o rectángulo para calcular el área.
# Se utiliza la entrada de datos, operaciones aritméticas y diferentes tipos de datos.

import math


def calcular_area_circulo(radio):
    """
    Función para calcular el área de un círculo.
    :param radio: Radio del círculo (float).
    :return: Área del círculo (float).
    """
    return math.pi * radio ** 2


def calcular_area_cuadrado(lado):
    """
    Función para calcular el área de un cuadrado.
    :param lado: Lado del cuadrado (float).
    :return: Área del cuadrado (float).
    """
    return lado ** 2


def calcular_area_rectangulo(base, altura):
    """
    Función para calcular el área de un rectángulo.
    :param base: Base del rectángulo (float).
    :param altura: Altura del rectángulo (float).
    :return: Área del rectángulo (float).
    """
    return base * altura


def main():
    """
    Función principal que permite al usuario elegir la figura y calcular su área.
    Utiliza diferentes tipos de datos (int, float, string, boolean).
    """
    # Variables de entrada
    figura = input("Elige una figura (círculo, cuadrado, rectángulo): ").lower()

    # Control de flujo con booleanos
    if figura == "círculo":
        radio = float(input("Introduce el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f} unidades cuadradas.")

    elif figura == "cuadrado":
        lado = float(input("Introduce el lado del cuadrado: "))
        area = calcular_area_cuadrado(lado)
        print(f"El área del cuadrado es: {area:.2f} unidades cuadradas.")

    elif figura == "rectángulo":
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area:.2f} unidades cuadradas.")

    else:
        print("Figura no reconocida, por favor elige entre círculo, cuadrado o rectángulo.")

    # Preguntar si el usuario quiere realizar otro cálculo
    continuar = input("¿Quieres calcular el área de otra figura? (sí/no): ").lower() == "sí"

    if continuar:
        main()  # Llamar a la función principal nuevamente para seguir calculando
    else:
        print("Gracias por usar el programa.")


# Llamar a la función principal para iniciar el programa
main()
