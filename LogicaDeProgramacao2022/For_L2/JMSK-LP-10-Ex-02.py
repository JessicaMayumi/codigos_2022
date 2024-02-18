soma = 0
quantidade = 0

for i in range(20):
    n = int ( input ("Digite um número: " ))

    if n > 0:
        soma = soma + n

    else:
        quantidade = quantidade + 1

print ( soma )
print ( quantidade )