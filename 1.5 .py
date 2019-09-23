x = float(input('x = '))
y = float(input('y = '))
if x > 0 and y > 0:
    print('3-я четверть')
if x < 0 and y < 0:
    print('1-я четверть')
if x < 0 and y > 0:
    print('2-я четверть')
if x > 0 and y < 0:
    print('4-я четверть')
if x == 0 or y == 0:
    print('Точка лежит на оси')
