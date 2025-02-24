import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')
x =[0, 5, 10, 15, 20, 30, 40, 50, 60, 70, 80]
y =[27.5, 21.2, 17.5, 13.7, 11.3, 8.1, 5.6, 5.0, 4.4, 4.3, 4.0]
# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 100), xticks=np.arange(1, 100),
       ylim=(0, 30), yticks=np.arange(1, 30))

plt.show()
