"""
    -- Maneira Errada --

resultado = ""
decimal = int (input ("Insira um número: "))

while decimal >=0:
    div_int = decimal%2
    div_string = str(div_int)
    resultado = div_string + resultado
    x = div_int//2
"""

#   -- Maneira Certa --

result = ""
numero = int (input ("Insira um número: "))
q = numero
while q!=0:
    r = q%2
    result = str(r) + result
    q = q//2

print(result)
