def potencia(x, y):
    valor = 1
    for i in range(y):
        valor *= x
    return valor

x = float (input ("Insira um n°: "))
y = int (input ("Insira outro n°: "))
print (potencia(x, y))