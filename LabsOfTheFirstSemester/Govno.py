from random import randint
a = [randint(0, 5) for _ in range(20)]
def remove_duplicates(a):
    print(a)
    ##l=0
    ##r=0
    ##while l<len(a):
    ##    r=l+1
    ##    while r < len(a):
    ##        if a[l] == a[r]:
    ##            a.pop(r)
    ##        r += 1
    ##    l += 1
    endindex = len(a)
    l = 0
    while l < endindex:
        r = l + 1
        replace = 0
        while r < endindex:
            a[r - replace] = a[r]
            if a[l] == a[r]:
                replace += 1
                print('rep', replace)
            r += 1
            print('r', r)
        endindex = endindex - replace
        l += 1
        print('l', l)
        print('end', endindex)
    print(a)
    print(a[:endindex])
        
a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 8, 8]
remove_duplicates(a)
