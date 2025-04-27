#5
a=int(input('a='))
b=int(input('b='))
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')
x=np.linspace(0, 10, 100)
y=a*x**2+b
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)
ax.set(xlim=(0, 5), xticks=np.arange(0, 50),
       ylim=(0, 25), yticks=np.arange(0, 50))

plt.show()
