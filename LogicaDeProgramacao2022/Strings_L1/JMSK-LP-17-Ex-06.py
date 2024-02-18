frase = input ("Insira algo: ")
letter = input ("Insira um caractere:")

nova = ""

for i in frase:
    if i != letter:
        nova += i

print (nova)
