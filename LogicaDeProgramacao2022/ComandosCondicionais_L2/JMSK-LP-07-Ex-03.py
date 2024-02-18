nota1 = float ( input ( "1° nota: "))
nota2 = float ( input ( "2° nota: "))
nota3 = float ( input ( "3° nota: "))

media = ( nota1 + nota2 + nota3 ) / 3

if media >= 7:
    print ( "Sua média é:", media)
    print ( "Aprovado!")

elif ( media < 7 ) and ( media >= 4 ):
    print ( "Sua média é: ", media )
    print ( "Você está em prova final! ")

else:
    print ( "Sua média é:", media)
    print ( "Reprovado!")
