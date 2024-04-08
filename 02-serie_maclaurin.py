'''Algoritmo para resolver series de Maclaurin para funciones eulier(e^x)'''

#Se importaron las siguientes librerias
from math import*
import numpy as np
import sympy as np
from tabulate import tabulate

valor_previo = 1
table = []

def func(x):
    funcion=exp(x)
    return funcion
x = float(input("Ingrese x: ")) #Ingresar el valor de x del problema a tratar

vreal = func(x)

N = int(input("Ingrese el numero de Iteraciones: ")) #Ingresar el numero de iteraciones necesarias

#Se estructura el codigo para iteraciones
n=0
resultado=1 
while n+1 <= N:
    if n+1 > 1:
        resultado = valor_previo + (x**n)/ factorial(n) #Formula de Maclaurin   
    error_relativo = ((vreal-resultado)/(vreal))  #Formula Error relativo
    
    if n+1 == 1: #Condicion que indica que en el primer termino no se calcula el error aproximado 
        Error_aproximado=""
    else:
        Error_aproximado = (resultado-valor_previo)/resultado  #Formula Error aproximado
    valor_previo = resultado
        
    if n+1 != 1 and Error_aproximado <= 0.0000001: #Condicion para terminar el ciclo(indicar cuando detenerse, en un error del 0.05)
        n=N+1
    else:
        n = n+1
        
    #Formato para imprimir los resultados
    table.append([n, resultado, error_relativo, Error_aproximado])
    print(tabulate(table, headers=["Iteraciones", "Calculos-Aproximacion", "Error Relativo", "Error Aproximado"]))
    print("")
