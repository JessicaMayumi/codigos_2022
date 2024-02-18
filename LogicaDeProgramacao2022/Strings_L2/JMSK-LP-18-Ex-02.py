print ("Comparação entre dois números")

n1 = input ("Insira um número de N algarismos: ")
n2 = input ("Insira outro número de N algarismos: ")

# assumimos que n1 e n2 estao ok
result = True

# varremos as 2 strings em paraelo, comparando caracter a caracter
# se em algum momento a comparacao "nao for boa", entao n1 e n2
# nao estao ok, ou seja: result = False
i=0
while i<len(n1):
    if n1[i] > n2[i]:
        result = False
        break
    i += 1

if result:
    print ("Todos os algarismos do primeiro n° são menores ou iguais que os do segundo n°.")
else:
    print ("Nem todos os algarismos do primeiro n° são menores que o do segundo n°.")