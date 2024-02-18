n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a primeira nota: "))

media = (n1 + n2)/2

if media<5.0 or n1<3 or n2<3:
    print("Sua média foi: {:.1f} - Reprovado!" .format(media))
else:
    print("Sua média foi: {:.1f} - Aprovado!" .format(media))
