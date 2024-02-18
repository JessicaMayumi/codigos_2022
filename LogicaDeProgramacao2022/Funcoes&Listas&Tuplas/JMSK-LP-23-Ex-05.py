def media_turma(lista):
    menor = lista[0]
    maior = lista[0]
    media = 0
    for i in range(len(lista)):
        media += lista[i]
        if lista[i]<menor:
            menor = lista[i]
        if lista[i]>maior:
            maior = lista[i]
    return media/len(lista),menor,maior

notas = []
while True:
    x = input ("Insira uma nota: ")
    if x == "":
        break
    notas.append(int(x))

print ("A maior nota é {}\nA menor nota é {}\nA média das notas é {} ".format(media_turma(notas)[2], media_turma(notas)[1], media_turma(notas)[0]))