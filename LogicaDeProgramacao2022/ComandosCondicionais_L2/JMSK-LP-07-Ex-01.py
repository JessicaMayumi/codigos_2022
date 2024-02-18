a = int ( input ( "Insira um número: "))
b = int ( input ( "Insira outro número: "))
c = int ( input ( "Insira outro número: "))

if ( a < b ) and (a < c):
    print ( "O menor número é: ",a )

elif ( a > b ) and ( b < c):
    print ( "O menor número é: ",b )

else: 
    print ( "O menor número é: ",c )
