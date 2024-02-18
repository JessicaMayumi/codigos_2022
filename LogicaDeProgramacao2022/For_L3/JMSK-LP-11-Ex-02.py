soma = 0
n = int ( input ("Digite um número: "))

for i in range (n):
    a= (n-i)/(i+1)
    soma = soma + a

print ( "{:.3f}" .format(soma))