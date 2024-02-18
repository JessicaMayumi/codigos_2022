n = int ( input ("Insira um nímero: "))
if n == 1 or n < 1 :
    print ("0")
elif n == 2: 
    print ("0 1")
else:
    print ("0 1", end=" ")
    i = 3
    penultimo = 0
    ultimo = 1
    while i <= n:
        atual = penultimo + ultimo
        print(atual, end=" ")
        penultimo = ultimo
        ultimo = atual
        i += 1
print()
        
