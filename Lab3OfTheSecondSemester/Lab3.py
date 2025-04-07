import numpy as np
import random
k=int(input("k="))
b=int(input("b="))
al=0.01
be=0.01
x=np.linspace(0, 10, 50)
y=[]
for i in range(len(x)):
    y.append(x[i]+random.uniform(-1, 1))
import matplotlib.pyplot as plt
fig, ax=plt.subplots()
ax.scatter(x, y)
plt.show()
for i in range(100):
    y_predict=k*x+b
    djdk=-2/50*(x*(y-y_predict))
    djdb=-2/50*(y-y_predict)
    k=k-al*djdk
    b=b-be*djdb
fig, ax=plt.subplots()
ax.scatter(x, y)
ax.plot(y_predict, y_predict, label='linear')
plt.show()
                
    
