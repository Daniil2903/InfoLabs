#вычислить сумму S=1+1/2...1/10
s=0
for i in range(1,11):
    s+=1/i
    print(s)
print(round(s,3))
    
