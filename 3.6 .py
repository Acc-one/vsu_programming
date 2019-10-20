n = int(input('Введите число : '))

def pros(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True
print(pros(n))
