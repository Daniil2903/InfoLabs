n=int(input('Введите делимое:'))
m=int(input('Введите делитель:'))
k=(n/m)-(n//m)
if k>=m:
    print('Ошибка')
else:
    print('Частное:', n, m,'Остаток от деления:', k)
 
