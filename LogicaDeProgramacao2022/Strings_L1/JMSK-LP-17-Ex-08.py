frase1 = input ("Insira uma frase: ")
frase2 = input ("Insira outra frase: ")

print ("Tamanho de '{}': {} caracteres" .format (frase1,len(frase1)))
print ("Tamanho de '{}': {} caracteres" .format (frase2,len(frase2)))

if len(frase1) < len(frase2):
    print ("'{} é menor que '{}'" .format (frase1, frase2))

elif len(frase1) > len(frase2):
    print ("'{} é maior que '{}'" .format (frase1, frase2))

else:
    print ("As duas frases possuem o mesmo tamanho.")