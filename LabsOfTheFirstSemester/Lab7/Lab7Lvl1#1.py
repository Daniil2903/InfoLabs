#Даны результаты спортсменов, вывести последних с результатами согласно их местам 
class sportsmen:
    def __init__(self, surname, team, first_try, second_try):
        self.surname=surname
        self.team=team
        self.first_try=first_try
        self.second_try=second_try
Gleb=sportsmen('Golubin', 'FIFSO', 1.32, 1.20)
Oleg=sportsmen('Lol', 'Kek', 1.15, 1.21)
Timur=sportsmen('Ruklin', 'FUNGG', 1.30, 1.32)
def summing(Gleb):
    s=Gleb.first_try+Gleb.second_try
    return(s)
t=[]
t.append(Gleb)
t.append(Oleg)
t.append(Timur)
for i in range (len(t)-1):
    if summing(t[i])>summing(t[i+1]):
        t[i], t[i+1]=t[i+1], t[i]
def info(self):
    print('Фамилия:',self.surname, ',', 'Команда:', self.team, ',', 'Первая попытка:', self.first_try,',', 'Вторая попытка:', self.second_try)
print('Список спортсменов в порядке убывания:')
for i in range(len(t)):
    if i==0:
        print('Место:',i+1)
        info(t[i])
    else:
        print('')
        print('Место:',i+1)
        info(t[i])
##for i in range(-len(t)):
##    if summing(Gleb)==t[i]:
##        print('sieg heil')
##    elif summing(Oleg)==t[i]:
##        print('AllJewsRIllegal')
##    elif summing(Timur)==t[i]:
##        print("I'llGoTomorrowAndSayToSonyaThatIWannaBeWithHere,SheIsSoAesthetic")
##from tabulate import tabulate as tab
##head=['Sportsman', 'Result']
##table=[['Tor'],['Wet', 23]]
##print(tab(table, headers=hed, tablefmt='grd'))
