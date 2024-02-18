frase = input ("Insira algo: ")
letter = input ("Insira um caractere:")

print ("'{}' aparece {}x na frase." .format (letter,frase.count(letter)))


# inicialmente considero que a letra nao esta na frase
esta_na_frase = False
quantidade_de_vezes = 0

# verifico cada letra x da frase para ver se é igual a letra fornecida pelo usuario
for caracter in frase:
    # se x é iguasl à letra fornecida, entao resultado fica verdadeiro 
    if caracter == letter:
        quantidade_de_vezes = quantidade_de_vezes + 1
        esta_na_frase = True

# ao final de tidas as repeticoes, se a letra nao apareceu nenhuma vez,
# o resultado continua False. Se apareceu pelo menos uma vez, ao final 
# o resultado é True

if esta_na_frase:
    print ("'{}' aparece {}x na frase." .format (letter,quantidade_de_vezes))
else:
    print ("'{}' aparece {}x na frase." .format (letter,quantidade_de_vezes))

"""
# n recebe a quantidade de caracteres da frase
n = len(frase)
# i eh o contador
i = 0
# enquanto i for menor que a quantidade de caracteres
while i<n:
    # compara o i-ésimo caracter da frase com a letra fornecida pelo usuario
    if frase[i] == letter:
        esta_na_frase = True
    i = i + 1


    # n recebe a quantidade de caracteres da frase
n = len(frase)
# enquanto i for menor que a quantidade de caracteres
for i in range(n):
    # compara o i-ésimo caracter da frase com a letra fornecida pelo usuario
    if frase[i] == letter:
        esta_na_frase = True

"""
