def skob(s):
    op = s.count('(')
    cl = s.count(')')
    
    if op > cl:
        return 'Не хватает закрывающих скобок:'+ str(op - cl)
    else:
        return 'Не хватает открывающих скобок:'+ str(cl - op)
print(skob(input('Введите пример:')))
        
    
