import numpy as np
import matplotlib.pyplot as plt

def interpolacion_lineal(f, x1, x2):
    y1 = f(x1)
    y2 = f(x2)
    return lambda x: y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)

f = lambda x: x**2

x0 = 0
x1 = 2
x = np.linspace(2, 3, 100)
y = f(x)

plt.plot(x, y, label='f(x)')
plt.plot(x0, f(x0), 'ro')
plt.plot(x1, f(x1), 'ro')
plt.plot(x, interpolacion_lineal(f, x0, x1)(x), label='Interpolacion lineal')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
