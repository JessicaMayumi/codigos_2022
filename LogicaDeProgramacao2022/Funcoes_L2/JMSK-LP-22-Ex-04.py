def eh_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        result = True
    else:
        result = False

    return result

x = int (input("Insira um ano: "))
print (eh_bissexto(x))