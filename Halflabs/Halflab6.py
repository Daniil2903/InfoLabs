import math
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(x)-x**2
def df(x):
    return np.exp(x)-2*x
x0=0
speed=0.01
epochs=100
x_path=[x0]
y_path=[f(x0)]
for _ in range(epochs):
    x0=x0-speed*df(x0)
    x_path.append(x0)
    y_path.append(f(x0))
x_vals=np.linspace(-2, 2, 400)
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f(x_vals), label=r'$y = e^x - x^2$', color='blue', zorder=5)
plt.scatter(x_path, y_path, c='orange', label='Градиентный спуск')
for i in range(len(x_path)-1):
    plt.arrow(x_path[i], y_path[i],
              x_path[i+1]-x_path[i], y_path[i+1]-y_path[i],
              head_width=0.02, length_includes_head=True, color='orange')
plt.title("Функция и процесс градиентного спуска")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
