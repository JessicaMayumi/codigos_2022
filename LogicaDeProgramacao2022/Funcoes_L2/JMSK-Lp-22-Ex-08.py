def encaixa(a,b):
    for i in range(len(str(b))):
        if str(b)[i] != str(a)[len(str(a))-len(str(b))+i]:
            return False
    return True

n1 = int (input("Insira um número: "))
n2 = int (input("Insira outro número: "))

s1= ""
if n1 > n2: 
    a = str(n1)
    b = str(n2)
else:
    a = str(n2)
    b = str(n1)

resposta = False
for i in range(len(b), len(a)+1):
    if encaixa(int(a[:i]), int(b)):
        resposta = True
        break
print(resposta)


"""

for i in str(n1):
        s1 += i
        if (encaixa(s1,n2)):
            print ("{} é segmento de {}.".format(n2,n1))
    
    
    for i in str(n1):
        s1 += i
        if (encaixa(s1,n2)):
            print ("{} é segmento de {}.".format(n2,n1))
        
else:
    for i in str(n2):
        s1 += i
        if (encaixa(s2,n1)):
            print ("{} é segmento de {}.".format(n1,n2))
    
  
"""
