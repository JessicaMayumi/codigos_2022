numero = int ( input ( " Digite um n° de 4 dígitos: "))

unidade_de_milhar = ( numero // 1000)

x1 = ( numero % 1000)
centena = ( x1 // 100)


x2 = ( numero % 100 )
dezena = ( x2 // 10 )

unidade = ( numero % 10)


soma = ( unidade_de_milhar + centena + dezena + unidade )

print ( " A soma desses algarísmos é : ", soma)