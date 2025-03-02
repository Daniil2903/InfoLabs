x=[[1, 1],[1, 2], [2, 1], [2, 2]]
y=[1, 1, 0, 0]
p=float(input('Доля:'))
def damn_x(x, p):
    x_train=[]
    for i in range(round(p*len(x))):
        x_train.append(x[i])
    return(x_train)
def damn_y(y, p):
    y_train=[]
    for i in range(round(p*len(y))):
        y_train.append(y[i])
    return(y_train)
    
k=3
import matplotlib.pyplot as plt
import numpy as np
fig, ax=plt.subplots()
ax.scatter(damn_x(x, p), damn_y(y, p), linewidth=2.0)
plt.show
