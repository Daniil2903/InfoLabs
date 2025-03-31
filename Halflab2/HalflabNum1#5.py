#5
a=int(input('a='))
b=int(input('b='))
n=0
k=0
if a>10 and b>20:
       n=a+20
       k=b+20
elif a>0 and a<10 and b<20:
       n=10
       k=25
elif a>0 and a<10 and b>20:
       n=10
       k=b+20
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')
x=np.linspace(0, 10, 100)
y=a*x**2+b
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)
ax.set(xlim=(0, 5), xticks=np.arange(0, n),
       ylim=(0, 25), yticks=np.arange(0, k))

plt.show()
