print('old')
m=[[1,3,4,5,6,4],[2,3,2,1,2,3],[3,4,0,5,4,3],[3,4,3,2,12,2],[34,4,5,4,300,4],[0,4554,4,3,2,2]]
maxim=0
indi=0
l=0
f=6
for u in m:
    for z in u:
        print(f'{z:<7}',end='')
    print('')
for i in range(6):
    if m[i][i]>maxim:
        maxim=m[i][i]
        for j in range(indi, i):
            for l in range(j+1, 6):
                m[j][l] = 0
        indi=i
print('new')
for y in m:
    for i in y:
        print(f'{i:<7}', end='')
    print('')
    
