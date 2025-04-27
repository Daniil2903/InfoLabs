print('дана матрица 7х5, если количество элементов столбца больше, чем отрицательных, то заменить максимальный элемент этого столбца на 0, в противном случае заменить на его номер')
print('old')
a=[[1,0,24,-2,3],
   [-3,-1,-4,5,-5],
   [6,-6,7,-7,8],
   [-8,9,-9,10,-10],
   [11,0,12,-12,13],
   [-13,14,-14,15,-15],
   [16,-10,17,-17,18]]
for s in a:
    print(s)
j=0
print('new')
while j<=4:
    k=0
    neg=0
    pos=0
    indi=0
    indj=0
    for i in range(7):
        if a[i][j]<0:
            neg+=1
        elif a[i][j]>0:
            pos+=1
        if a[i][j]>k:
            k=a[i][j]
            indi=i
            indj=j
    if pos>neg:
        a[indi][indj]=0
    elif neg>pos:
        a[indi][indj]=indi
    elif pos==neg:
        a=a
    j+=1
for n in a:
    print(n)
