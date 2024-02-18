
"""
    -- Maneira Errada --

for x in binario_string:
    binario_int = int (x)
    print (binario_int)
    while n >=0:
        decimal = binario_int*2**(n-1)
        n -= 1
    print (decimal)
"""

#   -- Maneira Certa --

binario_string = input ("Digite um número binário: ")

# A funcao len(s) retorna a quantidade de caracteres da string s
n = len(binario_string)

for x in binario_string:
    decimal += int(x)*2**(n-1)
    n -= 1

print (decimal)
    

