a = int ( input ( "Insira um número: "))
b = int ( input ( "Insira outro número: "))
c = int ( input ( "Insira outro número: "))
       
if a < b and a < c:
    menor = a

    if b > c:
        maior = b
        meio = c

    else:
        maior = c
        meio = b
    
elif b < a and b < c:
    menor = b

    if a > c:
        maior = a
        meio = c

    else: 
        maior = c
        meio = a
else:
    menor = c

    if a > b:
        maior = a
        meio = b

    else: 
        maior = b
        meio = c


print ( "A ordem decrescente é: " ,maior, meio, menor )
        
