#вычислить значение ф-ции y при заданном значении x по формуле y=1 при abs(x)>1, и y=abs(x) при abs(x)<=1
import math
x=int(input())
y=0
if abs(x)>1:
    y=1
else:
    y=abs(x)
print(y)
