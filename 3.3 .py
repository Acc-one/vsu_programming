n = int(input('n = '))
print(0)
print(1)

def fib(n):
    k1 = 0
    k2 = 1
    for a in range(n-2):
        s = k1 + k2
        k1 = k2
        k2 = s
        print(s)
fib(n)
