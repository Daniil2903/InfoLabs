a=[90, 90, 89, 89, 79, 467, 56, 34, 23]
b=[78, 90, 89, 78, 89, 91, 67]
print(a, ',', b)
def pivo(a):
    maxa=0
    indi=0
    for i in range(len(a)):
        if a[i]>maxa:
            maxa=a[i]
            indi=i
    return(indi)
s=0
if len(a)-pivo(a)>len(b)-pivo(b):
    for i in range(pivo(a)+1, len(a)):
        s=s+a[i]
        s=s/2
    a[pivo(a)]=s
    print('Массив А:', a, ',', 'Массив Б:', b)
else:
    for i in range(pivo(b)+1, len(b)):
        s=s+b[i]
        s=s/2
    b[pivo(b)]=s
    print('Массив А:', a, ',', 'Массив Б:', b)

    
