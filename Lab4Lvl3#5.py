#в массиве n*n максимальный по модулю элемент перенести на пересечение k-стобца и k-строки 
print('old')
m=[[1,2,3,2,21],[778878,0,-9,-9,8],[89,76,1488,0,0],[7,9,67,-88888888,0],[98,90,86,67,89]]
for t in m:
    print(t)
maxm=0
j=0
h=0
valp=0
while j<=4:
    for i in range(5):
        if m[j][i]<0:
            h=m[j][i]
            m[j][i]=-m[j][i]
        if m[j][i]>maxm:
            maxm=m[j][i]
            indi=i
            indj=j
    j+=1
indp=int(input('Write the number:'))
if indp>=1 and indp<=4:
    valp=m[indp][indp]
    print(valp)
    m[indp][indp]=h
    m[indj][indi]=valp
    print('new')
    for g in m:
        print(g)
else:
    print('Ошибка введения числа')
