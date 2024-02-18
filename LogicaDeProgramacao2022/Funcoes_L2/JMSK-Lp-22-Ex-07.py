def encaixa(a,b):
    for i in range(len(str(b))):
        if str(b)[i] != str(a)[len(str(a))-len(str(b))+i]:
            return False
    return True

n1 = int (input("Insira um número: "))
n2 = int (input("Insira outro número: "))

if encaixa(n1, n2):
    print ("{} encaixa em {}." .format(n2,n1))

else: 
    print ("{} não encaixa em {}." .format(n2,n1))