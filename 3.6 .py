n = int(input('Введите число : '))

def pros(n):
    if n > 3 and not n % 2 or n <= 1:
        return False 
    for i in range(3, int(n ** 0.5) + 1, 2):
        if not n % i:
            return False
    return True
print(pros(n))

    
        
    
