y = int (input ("Insira um número: " ))
maior= y
menor = y
while True:
    x = input ("Insira outro número, caso deseje para tecle 'Enter': " )
    if x == "":
       break
    
    inteiro = int(x)

    if inteiro > maior:
        maior = inteiro
    
    if inteiro < menor:
        menor = inteiro

print ("Maior: ", maior)
print ("Menor: ", menor)

