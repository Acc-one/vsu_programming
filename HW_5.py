from collections import deque


def doter(a):
    return not len(a) % 2 and a[0] == 'Д'


def bfs(dq, people):
    visit = []
    while dq:
        vekt = dq.popleft()
        if vekt not in visit:
            if doter(vekt):
                return vekt
                break
            dq += people.get(vekt, [])
            visit.append(vekt)
    return 'Никто не найден'


fr = {
    'Женя': ['Рустам', 'Виталий', 'Алексей',],
    'Рустам': ['Дима', 'Саша'],
    'Виталий': ['Женя'],
    'Саша': ['Рустам', 'Дима']
}

d = deque(fr['Женя'])

print(bfs(d, fr))
