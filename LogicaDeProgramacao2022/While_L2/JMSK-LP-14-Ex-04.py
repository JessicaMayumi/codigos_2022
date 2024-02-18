numero = int ( input ("Insira  um número: "))
quantidade=0

while numero//1!=0:
    quantidade += 1
    numero = ( numero//10 )

print(quantidade)