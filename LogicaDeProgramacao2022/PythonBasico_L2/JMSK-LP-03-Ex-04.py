conta_bancaria = int(input("Digite o n° da sua conta bancária: "))
a=conta_bancaria//10000

x1=conta_bancaria%10000
b=x1//1000

x2=conta_bancaria%1000
c=x2//100

x3=conta_bancaria%100
d=x3//10

x4=conta_bancaria%10
e=x4//1

print(a,b,c,d,e)

s = 6*a + 5*b + 4*c + 3*d + 2*e
digito_verificador = s%7

print(digito_verificador)
print("Número completo: {:05d}-{:d}".format(conta_bancaria, digito_verificador))