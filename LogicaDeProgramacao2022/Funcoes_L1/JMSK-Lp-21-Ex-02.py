def imprime_nome(nome,n):
    for i in range(n):
        print (nome)

x = input ("Insira um nome: ")
y = int (input("Insira um n° de vezes para ele se repitir: "))
imprime_nome(x,y)