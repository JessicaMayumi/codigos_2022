soma=0
for i in range (2,30,2):
    if i%4==0:
        soma = soma - 4/(i*(i+1)*(i+2))
    else: 
        soma = soma + 4/(i*(i+1)*(i+2))

print ( 3 + soma )


# versao do professor

#pi = 3
#sinal = 1
"""
for parcelas in range(1, 6):
    pi = 3
    sinal = 1
    print("pi = 3 +", end=" ")
    for i in range(2,parcelas+1):
        pi = pi + sinal * (4/((2*i-2)*(2*i-1)*(2*i)))
        sinal = -sinal
        print("{:.3f}".format(x), end="+")
    print("=", pi)
    """

# exemplo: calculando pi com 5 parcelas (no calculo)
# valor inicial do pi (com apenas 1 parcela pi = 3.0)
pi = 3
print("pi = 3 +", end=" ")
# somando ao pi as parcelas 2 3 4 e 5
for i in range(2,6):
    if i%2==0:
        pi = pi + (4/((2*i-2)*(2*i-1)*(2*i)))
    else:
        pi = pi - (4/((2*i-2)*(2*i-1)*(2*i)))
print("=", pi)

#for i in range(15):
    #pi = pi + (sinal)*(4/(2*i-2)(2*i-1)*(2*i))
    
    #sinal = -sinal