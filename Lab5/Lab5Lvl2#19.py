#в заданной матрице удалить все строки, содержащие нулевые элементы
m=[[1,2,0],[4,1,5],[1,0,3],[5,4,10]]
def del_zero(m):
    for j in range(len(m)-1,-1,-1):
        for i in range(len(m[0])):
            if m[j][i]==0:
                m.pop(j)
                break
    return(m)
for f in m:
    print(f)
print('')
for f in del_zero(m):
    print(f)

