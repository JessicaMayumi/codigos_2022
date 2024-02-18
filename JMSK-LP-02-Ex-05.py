v1= int(input('Quantos vasilhames de até um litro?'))
v2= int(input('Quantos vasilhames com mais de um litro?'))

c1= v1* 0.10
c2= v2* 0.25
total= c2+c1
print("R$ %.2f" % total)
