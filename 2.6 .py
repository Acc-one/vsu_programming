st = input('Строка:')
num = int(input('Число:'))

st = list(filter(lambda s: s.isdigit(), st)) 
print(str(num) + '-е число в строке ' + st[num - 1])
    
