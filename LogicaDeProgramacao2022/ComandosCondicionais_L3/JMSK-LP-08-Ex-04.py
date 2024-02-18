linha = int ( input ( "Digite um número da linha: " ))
coluna = int ( input ( "Digite um número da coluna: "))

if linha % 2 == 0 and coluna % 2 == 1:
    print ( "Quadrado Branco")

elif linha % 2 == 1 and coluna % 2 == 0: 
    print ( "Quadrado Branco")

elif linha % 2 == 0 and coluna % 2 == 0:
    print ( "Quadrado Preto")

else:
    print ( "Quadrado Preto")