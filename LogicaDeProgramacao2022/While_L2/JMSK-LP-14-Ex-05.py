soma = 0
quantidade = 0

while True:
    n = input ("Insira um valor: ")
    if n=="":
        break
    n = int(n)
    if n>=0:
        soma += n
    else:
        quantidade += 1

print ("A soma dos positivos é: ", soma)
print ("A quantidade de negativos é: ", quantidade)