soma = 0
n = int ( input ("Digite um número: "))

for i in range (1,n+1):
    if i%2==0:
        soma = soma - 1/(i)
    else:
        soma = soma + 1/(i)

print ( "{:.2f}" .format(soma))