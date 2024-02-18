cpf = input ("Insira seu CPF (xxx.xxx.xxx-xx): ")

#tirando os '.' e '-' e deixando só os n°

soma1 = 0
novo1 = ""

for i in cpf:
    if i!="." and i!="-":
        novo1+=i

#numeros de 1-9 sendo multiplicados por 10-2

novo2 = ""
x=2

for i in novo1[8::-1]:
    novo2 = i + novo2
    soma1+=(int(i)*x)
    x+=1

#cálculo do primeiro digito

primerio_digito = 11 - ( soma1%11 )
if primerio_digito==10:
    primerio_digito = 0

digitos = novo2 + str(primerio_digito)

#segundo digito verificador

soma2 = 0
novo4 = ""
y=2

for i in novo1[9::-1]:
    novo4 = i + novo4
    soma2+=(int(i)*y)
    y+=1

segundo_digito = 11 - (soma2%11)

if segundo_digito==10:
    segundo_digito=0

digitos += str(segundo_digito)

#verificador

if cpf[12]==str(primerio_digito) and cpf[13]==str(cpf[13]):
    print("O cpf {} é valido." .format(cpf))
else:
    print("O cpf {} não é valido." .format(cpf))