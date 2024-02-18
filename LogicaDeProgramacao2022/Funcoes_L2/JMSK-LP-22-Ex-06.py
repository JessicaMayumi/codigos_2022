def conta_digitos(n, d):
    result = str(n).count(str(d))
    return int(result)

def permutacao(a, b):
    for i in range(10):
        if conta_digitos(a, i) != conta_digitos(b, i):
            return False
    return True

n1 = int (input("Insira um n°: "))
n2 = int (input("Insira outro n°: "))

if permutacao(n1, n2):
    print ("{} é uma permutação de {}." .format(n2,n1 ))
else:
    print ("{} não é uma permutação de {}." .format(n2 ,n1 ))