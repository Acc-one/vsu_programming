x = int(input ('x = '))
y = int(input ('y = '))
f = 0
for d in range(x, y + 1): 
    if not (d % 5):
        f += d
print(f)
     
    
