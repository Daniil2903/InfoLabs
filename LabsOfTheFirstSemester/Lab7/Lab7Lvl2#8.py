#Даны хоккеисты со штрафным временем, если штрафное время больше 10, то спорстмен удаляется. Написать программу, выводящую их в порядке приоритетности
class hockey:
    def __init__(self, num, first_penal, second_penal):
        self.num=num
        self.first_penal=first_penal
        self.second_penal=second_penal
a=hockey(1, 2.5, 0)
b=hockey(2, 0, 0)
c=hockey(3, 10, 10)
d=hockey(4, 2.5, 10)
e=hockey(5, 5, 0)
f=hockey(6, 2.5, 7)
g=hockey(7, 5, 0)
h=hockey(8, 2.5, 2.5)
#Функциональный кластер от Саши Скула и Паши Техника:
def sigma(a):
    s=a.first_penal+a.second_penal
    return(s)
def info(self):
    print('Номер игрока:', self.num, ',','Штрафы за первую игру:', self.first_penal, ',', 'Штрафы за вторую игру:', self.second_penal)
t=[]
t.append(a)
t.append(b)
t.append(c)
t.append(d)
t.append(e)
t.append(f)
t.append(g)
t.append(h)
r=0
while r<len(t):
    if sigma(t[r])>=10:
        t.pop(r)
    else:
        r+=1
for i in range(len(t)-1):
    if sigma(t[i])>sigma(t[i+1]):
        t[i], t[i+1]=t[i+1], t[i]
print('Крутые мужики:')
for i in range(len(t)):
    if i==0:
        print('Порядок приоритетности:', i+1)
        info(t[i])
    else:
        print('')
        print('Порядок приоритетности:', i+1)
        info(t[i])




