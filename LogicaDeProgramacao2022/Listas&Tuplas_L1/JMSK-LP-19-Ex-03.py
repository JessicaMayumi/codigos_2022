lista_idade = []
lista_altura = [] 

i = 0
while i < 5:
    
    idade = int( input ("Insira sua idade: "))
    altura = int(input ("Insira sua altura: "))
    lista_idade.append(idade)
    lista_altura.append(altura)
    i += 1

print ("Lista da Idade: ",lista_idade[-1::-1])
print ("Lista da Altura: ",lista_altura[-1::-1])