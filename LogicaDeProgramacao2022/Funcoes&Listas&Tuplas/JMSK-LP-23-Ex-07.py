def pares_impares(x):
    tupla = ([],[])
    for i in x:
        if i%2 == 0:
            tupla[0].append(i)
        else:
            tupla[1].append(i)
    return tupla

lista = []
while True:
    numeros = input ("Insira um número: ")
    if numeros == "":
        break
    lista.append(int(numeros))

print ("Dos números que você digitou,\nOs números pares são {}\nE os números ímpares são {}" .format(pares_impares(lista)[0], pares_impares(lista)[1]))