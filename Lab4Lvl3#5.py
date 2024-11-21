#в массиве n*n максимальный по модулю элемент перенести на пересечение k-стобца и k-строки 
print('old')
m=[[1,2,3,2,21],[8,0,-9,-9,8],[89,76,14,0,0],[7,9,67,88,0],[-98,90,86,67,89]]
for t in m:
    print(t)
maxm=0
j=0
valp=0
while j<=4:
    for i in range(5):
        if abs(m[j][i])>maxm:
            maxm=abs(m[j][i])
            indi=i
            indj=j
    j+=1
indp=int(input('Write the number:'))
if indp>=0 and indp<=4:
    m[indj][indi], m[indp][indp]=m[indp][indp], m[indj][indi]
    print('new')
    for g in m:
        print(g)
else:
    print('Ошибка введения числа')

