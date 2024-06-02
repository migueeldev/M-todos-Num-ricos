import numpy as np
import matplotlib.pyplot as plt

# Definir la ecuación diferencial
# dy/dx = f(x, y)
def f(x, y):
    return x * np.sqrt(y)

# Implementar el método de Runge-Kutta de tercer orden
def runge_kutta_3rd_order(f, x0, y0, x_end, h):
    # Inicializar las listas de resultados
    x_values = [x0]
    y_values = [y0]
    
    x = x0
    y = y0
    
    while x < x_end:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h, y - k1 + 2*k2)
        
        y += (k1 + 4*k2 + k3) / 6
        x += h
        
        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values

# Parámetros iniciales
x0 = 0
y0 = 1
x_end = 10
h = 0.1

# Resolver la ecuación diferencial
x_values, y_values = runge_kutta_3rd_order(f, x0, y0, x_end, h)

# Graficar los resultados
plt.plot(x_values, y_values, label='Runge-Kutta 3er Orden')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la EDO usando Runge-Kutta de 3er Orden')
plt.legend()
plt.grid(True)
plt.show()
