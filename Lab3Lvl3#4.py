m=[4, 34, 342, 43, 71, 342, 44, 43, 24, 43, 342]
print(m)
maximum = max(m)
s = 0
for i in range(len(m)):
    if m[i] == maximum:
        m[i] = s
    s += m[i]
print(m)
