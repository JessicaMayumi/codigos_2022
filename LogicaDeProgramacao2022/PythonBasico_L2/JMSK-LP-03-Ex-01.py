n=int(input("Digite um n° de até 3 dígitos: "))

centena=n//100

x=n%100
dezena=x//10

unidade=x%10

m=unidade*100+dezena*10+centena

print("N° invertido:" ,m)
