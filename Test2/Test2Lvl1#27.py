print('Old matrix')
m=[[1,2,3,4,5,6,7],
   [23,4,4,5,6,7,9],
   [45,6,7,89,67,54,54],
   [23,56,76,78,65,67,54],
   [76,90,87,65,44,32,32]]
for y in m:
    for t in y:
        print(f'{t:>5}',end='')
    print('')
##def pivo(m, i):
##    maxi=0
##    for j in range(len(m[0])):
##        if m[i][t]>maxi:
##            maxi=m[i][j]
##        m[4][len(m)-(1+i)]=maxi
##    return(m)
##i=1
##print(pivo(m, i))
t=[]
for i in range(len(m)):
    maxi=0
    for j in range(len(m[0])):
        if m[i][j]>maxi:
            maxi=m[i][j]
    t.append(maxi)
for j in range(len(t)):
    m[len(m)-(1+j)][3]=t[j]
print('New matrix')
for y in m:
    for t in y:
        print(f'{t:>5}',end='')
    print('')
