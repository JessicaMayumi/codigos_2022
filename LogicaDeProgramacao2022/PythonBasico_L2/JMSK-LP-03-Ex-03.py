codigo_da_matricula=int(input("Digite o n° da matrícula: "))

ano=codigo_da_matricula//10000

x=codigo_da_matricula%10000

semestre=x//1000
numero=codigo_da_matricula%1000

print("Ano de matricula: ", ano)

print("Semestre de matrícula: ", semestre)

print("Número da matrícula: ", numero)