m=[1, 4, 54, 43, 343, 555, 65, 43, 23, 12, 3, 67, 89, 90, 7979605, 9797, 9696, 699]
s=0
t=[]
for i in range(len(m)):
    if m[i]==max(m):
        maxi=i
for i in range(maxi+1):
    s=s+m[i]/2
    t.append(m[i])
for i in range(maxi, len(m)-1):
    t.append(s)
print(t)
