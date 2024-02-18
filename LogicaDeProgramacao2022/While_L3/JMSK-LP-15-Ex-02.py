i = 1
graos_atual = 1
graos_anterior = 1

while i+1 <= 64:
    graos_atual += graos_anterior*2
    graos_anterior *= 2
    i += 1
    
print ( graos_atual )
