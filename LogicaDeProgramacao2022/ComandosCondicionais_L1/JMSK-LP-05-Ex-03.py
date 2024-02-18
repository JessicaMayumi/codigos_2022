numero1= int ( input ( " Digite um número: "))
numero2= int ( input ( " Digite outro número: "))

if numero1 == numero2:
    print ( "Seus números são iguais " )

else: 
    print ( "Seus números são diferentes " )

if numero1 > numero2:
    print ( numero2, numero1 )

elif numero1 < numero2:
    print ( numero1, numero2)

else:
    print ("Os dois são iguais")
    print ( numero1, numero2 )