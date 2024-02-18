n = int(input("Insira um número: "))
fator = 2

if n < 2:
    print ("Erro")

else:   
    while fator <=n:
        if n%fator==0:
            n//=fator
        else:
            fator+=1
        print (fator)
