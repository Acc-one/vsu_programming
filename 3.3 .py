n = int(input('n = '))
print(1)
def fib(n):
    k1 = 0
    k2 = 1
    a = 0
    for a in range(n):
        a += 1
        s = k1 + k2
        k1 = k2
        k2 = s
        print(s)
fib(n)
