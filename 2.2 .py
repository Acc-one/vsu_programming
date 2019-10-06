a = input()
b = []
    
while a:
    b.append(a)
    a = input()
    
b = sorted(b, reverse=True)
print(''.join(b))
