N=10

num=int(input("Digite um número: "))
soma = num
maior = num
menor = num


for i in range (N-1):
    num=int(input("Digite um número: "))
    soma=soma+num
    media=soma/10
    if num>maior:
        maior = num
    if num<menor:
        menor = num



media = soma / N
print("A média desses números é: {:.2f}" .format(media))
print("O maior desses números é: ", maior)
print ("O menor de desses números é: ",menor)