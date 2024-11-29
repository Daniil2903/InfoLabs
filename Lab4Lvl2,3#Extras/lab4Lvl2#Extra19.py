#удалить все строки, содержащие нулевые элементы
m=[[9,1,67,6,5],[45,8,0,3,3],[3,0,5,4,1],[88,14,6,4,9],[0,0,9,0,0]]
for y in m:
    for t in y:
        print(f'{t:<5}',end='')
    print('')
for j in range(len(m)-1,-1,-1):
    for i in range(len(m[0])):
        if m[j][i]==0:
            m.pop(j)
            break
print('')
for y in m:
    for t in y:
        print(f'{t:<5}',end='')
    print('')
