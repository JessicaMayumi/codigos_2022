frase = input ( "Insira uma frase: " )

nova = ""

for i in frase:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        nova+=i

print (nova)
