#task 3
import math 
a=float(0.1)
b=float(1)
h=float(0.1)
z=0
i=0
y=0
s=0
j=float(0.0001)
while a<=b:
    z=1
    s=(math.cos(1*a))/(math.factorial(1))
    i=1
    while abs(s)>=j:
        i+=1
        z=z+s
        s=(math.cos(i*a))/(math.factorial(i))
    y=math.cos(math.sin(a))*math.exp(math.cos(a))
    print('Значение:', a, z , y, i)
    a+=h
