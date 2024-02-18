n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a primeira nota: "))

media = (n1 + n2)/2

if media < 5.0:
    print("Sua média foi: {:.1f} - Reprovado!" .format(media))
else:
    print("Sua média foi: {:.1f} - Parabéns!" .format(media))
