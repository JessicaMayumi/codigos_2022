a = int ( input ( "Digite um número: "))
b = int ( input ( "Digite outro número: "))

if a > b and ( a % b == 0 ):
    print ( " {} e {} são múltiplos. ".format( a , b ))

elif a > b and ( a % b != 0 ):
    print ( " {} e {} não são múltiplos. ".format( a , b ))

elif a < b and ( b % a == 0 ) :
    print ( " {} e {} são múltiplos. ".format( b , a ))

else: 
    print ( " {} e {} não são múltiplos. ".format( b , a ))


