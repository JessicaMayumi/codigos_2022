frase = input ("Insira algo: ")

novo = ""

for i in frase:
    d = i.isdigit()
    if d:
        novo += i*2
    else:
        novo += i

print(novo)