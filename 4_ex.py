# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

#*Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

a = int(input('Введите размер n:'))
b = int(input('Введите размер m:'))
c = int(input('Введите k долек:'))
if c < a*b and (c % a == 0 or c % b == 0):
    print('yes')
else:
    print('no')
