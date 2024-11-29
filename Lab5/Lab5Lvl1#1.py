#определить, сколькими способами можно отобрать команду из 5 команд из 8, 10, 11 кандидатов 
import math
n=int(input('Введите число кандидатов:'))
def comb(n):
    if n>=5:
        sp=math.factorial(n)/(math.factorial(5)*math.factorial(n-5))
    else:
        sp='Error'
    return(sp)
print('Количество способов:', comb(n))
    
