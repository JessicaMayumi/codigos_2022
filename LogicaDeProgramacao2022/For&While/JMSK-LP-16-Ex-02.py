total = 0

while True:
    idade = input ("Insira a Idade: ")

    if idade == "":
        break
    
    nidade = int ( idade )

    if nidade >=3 and nidade <=12 :
        total += 14

    elif nidade >12 and nidade < 65:
        total += 23

    elif nidade >= 65:
        total += 18

print ( total )

    