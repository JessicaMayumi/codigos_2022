n1 = input ("Insira um número: ")
n2 = input ("Insira um número para verificar o n° de vezes que ele aparece: ")
n3 = input ("Insira outro número para verificar o n° de vezes que ele aparece: ")

quantidade_n2 = 0
quantidade_n3 = 0

for i in n1:
    if i==n2:
        quantidade_n2 += 1
    elif i==n3:
        quantidade_n3 +=1

print ("A quantidade de vezes que {} aparece é {}." .format(n2, quantidade_n2))
print ("E a quantidade de vezes que {} aparece é {}." .format(n3, quantidade_n3))
