m=[4, 34, 342, 43, 71, 342, 44, 43, 24, 43, 342]
t=[]
s=0
for i in range (len(m)):
    if m[i]==max(m):
        t.append(i)
for i in range(len(t)):
    for l in range(t[0]):
        s=s+m[l]
    m[t[i]]=s
print(m)
