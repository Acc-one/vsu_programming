import random

a = int(input('Введите число: '))
r = random.randint(0, 100)

while a != r:
    if r < a:
        print('Ваше число больше')
        a = int(input('Введите число: '))
    elif r > a:
        print('Ваше число меньше')
        a = int(input('Введите число: '))
    else:
        print('Вы угадали число')
print('Вы угадали число')
