def numero(n):
    return len(str(n))

x = int (input("Digite um n°:"))
if x > 0:
    print ("O número de digitos desse n° é: ",numero(x))
else: 
    print ("Você digitou um n° inválido!")