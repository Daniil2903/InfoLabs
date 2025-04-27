file=open('Assistance.txt', 'r')
x1=file.readlines()
y1=file.readlines()
file.close()
x1=x1.pop(0)
x1=str(x1)
x1=list(x1.split())
y1=list(x1)
x1[11:22]=[]
y1[0:11]=[]
x2=[]
y2=[]
for a in x1:
    a=int(a)
    x2.append(a)
for a in y1:
    a=float(a)
    y2.append(a)
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')
x=x2
y=y2
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))
fig, ax = plt.subplots()
ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
ax.set(xlim=(0, 100), xticks=np.arange(0, 100),
       ylim=(0, 30), yticks=np.arange(0, 30))
plt.show()
