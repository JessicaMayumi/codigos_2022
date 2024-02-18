frase = input ("Insira uma frase: ")

espaco=0
vogais=0

for i in frase:
    if i==" ":
        espaco+=1

    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vogais+=1

print ("O n° de vogais é",vogais)
print ("O n° de espacos vazios é",espaco)