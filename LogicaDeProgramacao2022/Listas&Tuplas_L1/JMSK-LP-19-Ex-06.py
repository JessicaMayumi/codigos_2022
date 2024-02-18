lista = []

while True:
    notas = float (input("Insira sua nota: "))
    if notas == -1:
        break
    lista.append(notas)

soma = 0
for i in lista:
    soma += i

media = soma/len(lista)

print ("Quantidade de valores: ",len(lista))
print ("Lista: ",lista)
print ("Lista Inversa: ",lista[-1::-1])
print ("Soma dos Valores: ", soma)
print ("Média dos Valores: ", media)

acima = []
abaixo = []
for i in lista:
    if i > media:
        acima.append(i)
    elif i < 7:
        abaixo.append(i)

print ("Notas acima da média: ", acima)
print ("Notas abaixo da média: ", abaixo)

print ("Programa Finalizado!")