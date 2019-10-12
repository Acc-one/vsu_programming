a = int(input('Введите номер месяца: '))

if (0 < a < 3) or (a == 12):
    print('Зима')
elif (2 < a < 6):
    print('Весна')
elif (5 < a < 9):
    print('Лето')
else:
    print('Осень')
