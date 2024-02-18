frase = input ("Insira algo: ")
letter = input ("Insira um caractere:")


quantidade = 0
for i in frase:
    if letter.upper() == i.upper():
        quantidade+=1

if quantidade >0:
    print ("A letra fornecida aparece {}x na frase.".format(quantidade))

else:
    print ("A letra fornecida não aparece na frase.")