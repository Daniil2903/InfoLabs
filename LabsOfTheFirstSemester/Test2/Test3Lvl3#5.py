#Даны игры футбольных клубов, вывести клубы с баллами (3 - победаю 0 - проигрыш, 1 - ничья), если баллы равны, то место определяется по разности между суммарным кол-вом голов и пропусков (у кого больше, тот и лучше), согласно местам
#Игры: фифсо-спарктак (10-5), спартак-зенит (5-6),  фифсо-зенит (8-2)
class football:
    def __init__(self, team, first_pl_goals, first_pl_looses, second_pl_goals, second_pl_looses):
        self.team=team
        self.first_pl_goals=first_pl_goals
        self.first_pl_looses=first_pl_looses
        self.second_pl_goals=second_pl_goals
        self.second_pl_looses=second_pl_looses
fifso=football('FIFSO', 10, 5, 8, 2)
spartak=football('SPARTAK', 5, 10, 5, 6)
zenit=football('ZENIT', 6, 5, 2, 8)
def first_pl(fifso, zenit):
    score1=0
    if fifso.first_pl_goals>zenit.first_pl_goals:
        score1=3
    elif fifso.first_pl_goals==zenit.first_pl_goals:
        score1=1
    elif fifso.first_pl_goals<zenit.first_pl_goals:
        score1=0
    return(score1)
def second_pl(fifso, zenit):
    score2=0
    if fifso.first_pl_goals>zenit.first_pl_goals:
        score2=3
    elif fifso.first_pl_goals==zenit.first_pl_goals:
        score2=1
    elif fifso.first_pl_goals<zenit.first_pl_goals:
        score2=0
    return(score2)
def difference(fifso):
    d=(fifso.first_pl_goals+fifso.second_pl_goals)-(fifso.first_pl_looses+fifso.first_pl_looses)
    return(d)
def info(self):
    s=self.team
    return(s)
t=[]
t.append(fifso)
t.append(spartak)
t.append(zenit)
for i in range(len(t)-1):
    if first_pl(t[i], t[i+1])<first_pl(t[i+1], t[i]):
        t[i],t[i+1]=t[i+1],t[i]
    elif first_pl(t[i], t[i+1])==first_pl(t[i+1], t[i]):
        if difference(t[i])<difference(t[i+1]):
            t[i],t[i+1]=t[i+1],t[i]
for i in range (len(t)):
    if i<len(t)-1:
        print('Место:', i+1, 'Название команды:', info(t[i]), 'Количество баллов:',first_pl(t[i], t[i+1])+second_pl(t[i], t[i+1]))
    else:
        print('Место:', i+1, 'Название команды',info(t[i]), 'Количество баллов:', first_pl(t[i], t[i-1])+second_pl(t[i], t[i-1]))


