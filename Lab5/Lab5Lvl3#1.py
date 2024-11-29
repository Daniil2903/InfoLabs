#вычислить приведённые на скрине суммы
import math
a=int(input('Какой вариант сумм хотите вычислить:'))
def sum_1(a):
    if a==1:
        s=1
        y=0
        for x in range(1, 10, 1):
            for i in range(1, 100):
                s=s+(math.cos(i*x/10)/math.factorial(i))
                y=y+((math.e)**math.cos(x/10))*math.cos(math.sin(x))
    elif a==2:
        s=0
        y=0
        a=math.pi/5
        b=math.pi
        h=math.pi/25
        while a<=b:
            for i in range(1, 100):
                s=s+(-1)**i*(math.cos(i*a)/i**2)
                y=y+(a**2-(math.pi**2)/3)/4
            a+=h
    return(s, y)
if a==1 or a==2:
    print(sum_1(a))
else:
    print('Error')
        
                
        
    
