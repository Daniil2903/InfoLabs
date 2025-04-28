import math
func="math.exp(x)-x**2"
difffunc="math.exp(x)-2*x"
print(func, difffunc)
x0=0
epochs=100
xlist=[]
ylist=[]
while epochs>=0:
    for i in range(100):
        xlist.append(x0-0.01*(math.exp(x0)-2*x0))
        ylist.append(math.exp(x0)-x0**2)
        x0=xlist[i]
    epochs-=1
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')
x =xlist
y =ylist
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))
fig, ax = plt.subplots()
ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
ax.set(xlim=(-1), xticks=np.arange(2),
       ylim=(0), yticks=np.arange(2))
plt.show()
