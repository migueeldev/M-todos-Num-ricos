'''Programa que calcula el numero de iteraciones
utilizando series de maclaurin hasta una tolerancia especificada'''

import math

def maclaurin_series(x, tolerancia):
    aproximacion = 1.0
    termino_actual = 1.0
    n = 1

    while abs(termino_actual) > tolerancia:
        termino_actual *= x / n
        aproximacion += termino_actual
        n += 1

    return n - 1  # El número de iteraciones necesarias

def main():
    valor_x = float(input("Ingrese el valor de x para la serie de Maclaurin: "))
    valor_tolerancia = float(input("Ingrese la tolerancia deseada: ")) #ejemplo: 1e-7

    iteraciones = maclaurin_series(valor_x, valor_tolerancia)

    print(f"Se necesitaron {iteraciones} iteraciones para alcanzar la tolerancia deseada.")

if __name__ == "__main__":
    main()

