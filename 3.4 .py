lst = []
st = input('Элементы : ')

while st:
    lst.append(st)
    st = input('Элементы : ')

for i in set(lst):
    print(f'{lst.count(i)} | {i}')

