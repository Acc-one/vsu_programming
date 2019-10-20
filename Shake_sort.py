sp = [1, 2, 4, 3, 5, 7, 9, 10]
left = 0
right = len(sp) - 1

while left < right:
    for i in range(right):
        if sp[i] > sp [i + 1]:
            right = i
            sp[i], sp[i + 1] = sp[i + 1], sp[i]
    if left < right:
         for i in range(right, left, -1):
             left = i
             sp[i], sp[i - 1] = sp[i - 1], sp[i]

print(sp)
