def interseccao(c1,c2):
    lista = []
    for i in c1:
        for x in range(len(c2)):
            if i == c2[x]:
                lista.append(i)
    return lista

lista1 = []
lista2 = []

while True:
    n1 = input ("Insira um número para a primeira lista: ")
    if n1 == "":
        break
    lista1.append(int(n1))

while True:
    n2 = input ("Insira um número para a segunda lista (com o mesmo tamanho da anterior): ")
    if n2 == "":
        break
    lista2.append(int(n2))

print ("Os números que se repetem nas duas listas são: {}" .format(interseccao(lista1,lista2)))