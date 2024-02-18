media_alunos = []

for i in range (2):
    print("Aluno:",i+1)
    soma = 0
    for j in range(4):
        nota = float (input ("Insira sua nota: "))
        soma += nota
    media = soma/4
    media_alunos.append(media)

print (media_alunos)