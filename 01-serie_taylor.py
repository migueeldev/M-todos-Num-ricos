#Librerias utilizadas
import numpy as np
import sympy as sym

def politaylor(fx,x0,n):
    k = 0
    polinomio = 0
    while (k <= n):
        derivada = fx.diff(x,k)
        derivadax0 = derivada.subs(x,x0)
        divisor = np.math.factorial(k)
        terminok = (derivadax0/divisor)*(x-x0)**k
        polinomio = polinomio + terminok
        k = k + 1
    return(polinomio)

x = sym.Symbol('x')
fx = sym.sqrt(x+1) #Raiz cuadrada de x+1

x0 = 0 #XSUBcero 
xi = 0.5 #Donde se evalua el polinomio
n = 3 #Orden, en este caso orden 3

# Valor, f(xi) real
fxi = fx.subs(x,xi)

#Valor aproximado taylor
polinomio = politaylor(fx,x0,n)
pxi = polinomio.subs(x,xi)
error_real =np.abs(fxi - pxi) #Error real -> valor absoluto
print('Taylor:       ', polinomio)
print('xi:       ', xi)
print('Estimado:       ', pxi)
print('Real:       ', fxi)
print('Error Real:       ', error_real)






