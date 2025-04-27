#в группе n студентов, вычислить средний балл группы и количество несдавших 
print('AmountOfStudents:')
n=int(input())
a=0
s=0
z=0
i=0
f=0
while i<n:
    print('Scores:')
    a=int(input())
    s=s+a
    i+=1
    z=s/n
    if a<=2.5:
        f+=1
print('AvergeScore:', z, ',', 'DidNotPass:', f)
