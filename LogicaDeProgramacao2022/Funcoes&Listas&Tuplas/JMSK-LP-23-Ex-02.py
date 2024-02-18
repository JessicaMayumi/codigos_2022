def inverte(t):
    nova_lista = []
    for i in range(len(t)):
        nova_lista.append(t[len(t)-1-i])
    return nova_lista

lista = []
while True:  
    x = input ("Insira um n°( press enter para parar ): ")
    if x == "":
        break
    else:
        lista.append(x)

print ("Ordem da lista invertida: ", inverte(lista))

