soma = 0
n = int ( input ("Digite um número: "))

for i in range (1,2*n,2):
    a= 1/i
    soma = soma + a

print ( "{:.2f}" .format(soma))