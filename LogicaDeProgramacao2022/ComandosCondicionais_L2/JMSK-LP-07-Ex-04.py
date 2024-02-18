a = float ( input ( "Insira um número: "))
b = float ( input ( "Insira outro número: "))
c = float ( input ( "Insira outro número: "))
    # classificar se eh triangulo
if not( a + b > c and a + c > b and b + c > a ):
    print( "Não é Triângulo" )
else:
    # classificar o tipo de triangulo
    if ( a == b ) and ( a == c ):
        print ( "É um Triângulo Equilátero" )
    
    elif ( a != b ) and ( b != c ) and ( a != c ):
        print ( "É um Triângulo Escaleno" )
    
    else:
        print ( "É um Triângulo Isósceles" ) 

        