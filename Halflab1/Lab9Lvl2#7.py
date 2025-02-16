#в массиве удвоить элемент, стоящий сразу после максимального
file=open('pivo1.txt', 'r')
s=file.readlines()
file.close()
s=s.pop(0)
s=str(s)
s=list(s.split())
t=[]
for a in s:
    a=int(a)
    t.append(a)
maxim=indi=0
for i in range(len(t)):
    if t[i]>maxim:
        indi=i
        maxim=t[i]
t[indi+1]=2*t[indi+1]
t=str(t)
file=open('pivo2.txt', 'w')
file.write(t)
file.close()

