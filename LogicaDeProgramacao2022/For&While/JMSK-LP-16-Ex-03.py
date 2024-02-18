    # para imprimir a primeira linha pode se usar while ou print
print ("\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10")

linha = 1
while linha<=10:
    # imprime tabuada de linha, de 1 ate 10
    print(linha, end="\t")
    coluna = 1
    while  coluna <= 10:
        print (linha*coluna, end="\t")
        coluna+=1
    print()
    linha = linha + 1