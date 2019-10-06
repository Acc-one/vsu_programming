b = []
a = input()

while a:
    b.append(a)
    a = input()
sorted(b,reverse = True)
print(''.join(b))
