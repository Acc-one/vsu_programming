storage = [[] for x in range(5)]


def hash(key):
    ind = sum(list(map(ord, key)))
    ind = sum(list(map(int, str(ind))))
    return ind % len(storage)


def set_value(key, value):
    ind = storage[hash(key)]
    for i in ind:
        if key == i[0]:
            i[1] = value
            break
    else:
        ind.append([key, value])


def del_value(key):
    ind = hash(key)
    for i in range(len(storage[ind])):
        if key == storage[ind][i][0]:
            del storage[ind][i]       


def get_value(key):
    ind = hash(key)
    for i in range(len(storage[ind])):
        if key == storage[ind][i][0]:
            return storage[ind][i][1]


set_value('abc', 2)
set_value('abc', 3)
set_value('cab', 32)
set_value('cnb', 2)
set_value('abcd', 2)

print(storage)

del_value('cnb')

print(get_value('cab'))
print(get_value('abc'))

print(storage)
