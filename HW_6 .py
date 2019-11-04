storage = [[] for x in range(5)]


def hash(key):
    ind = sum(list(map(ord, key)))
    ind = sum(list(map(int, str(ind))))
    return ind % len(storage)


def set_value(key, value):
    ind = hash(key)
    if not storage[ind]:
        storage[ind] = [[key, value]]
    else:
        for i in range(len(storage)):
            for x in range(len(storage[i])):
                if storage[i][x][0] == key:
                    storage[i][x][1] = value
                    break
                else:
                    storage[i].append([key, value])


def get_value(key):
    ind = hash(key)
    for i in range(len(storage[ind])):
        if key == storage[ind][i][0]:
            return storage[ind][i][1]

print (get_vaue('cab'))
print (get_value('abc'))
set_value('abc', 2)
set_value('abc', 3)
set_value('cab', 32)
set_value('cab', 23)

print (storage)
