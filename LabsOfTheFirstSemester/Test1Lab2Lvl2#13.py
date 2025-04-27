from math import pi, sqrt
a=int(input('Add the number for A:'))
b=int(input('Add the number for B:'))
s=0
fig=input('What square do u want: square, ring between A and B or triangle?:')
if fig=='square':
    s=a*b
elif fig=='ring':
    if a<b:
        print('Error: A should be bigger than B')
    else:
        s=pi*(a*a-b*b)
elif fig=='triangle':
    s=sqrt((a/2+b)*(b-a/2)*(b-a/2))
if a<b and fig=='ring':
    print('UHAveAnEroor,Bro')
else:
    print('UrSquareIs:', round(s, 3))
