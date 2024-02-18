def min_max(t):
    min = t[0]
    max = t[0]
    for i in range(len(t)):
        if t[i] < min:
            min = t[i]
        if t[i] > max:
            max = t[i]
    return min,max

numeros = []
while True:  
    x = input ("Insira um n°( press enter para parar ): ")
    if x == "":
        break
    else:
        numeros.append(int(x))

print ("O menor número é {} e o maior número é {}." .format(min_max(numeros)[0], min_max(numeros)[1]))
