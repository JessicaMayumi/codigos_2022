def conta_digitos(n, d):
    result = str(n).count(str(d))
    return int(result)

n1 = int (input("Insira um número: "))
n2 = int (input("Insira um número entre 0 e 9: "))
print ("O número {} apareceu {} em {}. ".format(n2,conta_digitos(n1, n2),n1))