# вычислить сумму 10 членов арифметической прогрессии s=p^2+(p+h)^2+...+(p+9h)^2
p=100
h=25
s=0
i=0
while i<10:
    s=s+(p+i*h)**2
    i+=1
print(s)

