def inverte_lista(l): #inverte a lista que será recebida em 'inverte_duplo'
    nova_lista = []
    for i in range(len(l)):
        nova_lista.append(l[len(l)-1-i])
    return nova_lista

def inverte_string(s): #inverte a string do indice i da lista recebida em 'inverte_duplo'
    nova_string = ""
    for i in range(len(s)):
        nova_string += s[len(s)-1-i]
    return nova_string

def inverte_duplo(x): #lista que une as duas listas, retornando diretamente toda a lista invertida
    nova_lista = inverte_lista(x)
    for i in range(len(x)):
        nova_lista[i] = inverte_string(nova_lista[i])
    return nova_lista

lista = []
while True:  
    x = input ("Insira um n°( press enter para parar ): ")
    if x == "":
        break
    else:
        lista.append(x)

print (inverte_duplo(lista))