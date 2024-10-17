m=[1, 2, 3, 4, 5, 6, 57, 68, 90]
t1=[]
t2=[]
for i in range(len(m)):
    l=i%2
    if l==0:
        t1.append(m[i])
    else:
        t2.append(m[i])
print('Чётный массив:', t1, ',', 'Нечётный массив:', t2)
