a=[90, 90, 89, 89, 79, 467, 56, 34, 23]
b=[78, 90, 89, 78, 89, 89, 67]
print(a, ',', b)
def pivo(a):
    indi=0
    for i in range(len(a)):
        if a[i]==max(a):
            indi=i
            break
    return(indi)
s=0
z=0
if len(a)-pivo(a)>len(b)-pivo(b):
    for i in range(pivo(a)+1, len(a), 1):
        s=s+a[i]
    s=s/(len(a)-pivo(a)-1)
    a[pivo(a)]=s
    print('Массив А:', a, ',', 'Массив Б:', b)
elif len(a)-pivo(a)<len(b)-pivo(b):
    for i in range(pivo(b)+1, len(b), 1):
        s=s+b[i]
    s=s/(len(b)-pivo(b)-1)
    b[pivo(b)]=s
    print('Массив А:', a, ',', 'Массив Б:', b)
elif len(a)-pivo(a)==len(b)-pivo(b):
    for i in range(pivo(a)+1, len(a), 1):
        s=s+a[i]
    s=s/(len(a)-pivo(a)-1)
    a[pivo(a)]=s
    for i in range(pivo(b)+1, len(b), 1):
        z=z+b[i]
    z=z/(len(b)-pivo(b)-1)
    b[pivo(b)]=z
    print('Массив А:', a, ',', 'Массив Б:', b)
