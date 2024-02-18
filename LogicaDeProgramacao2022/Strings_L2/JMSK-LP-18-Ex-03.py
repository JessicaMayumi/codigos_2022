palavra = input ("Insira uma palavra: ")

nova = ""

i = 1
while i <= len(palavra):
    nova = palavra[-i] + nova
    print (nova)
    i += 1
   