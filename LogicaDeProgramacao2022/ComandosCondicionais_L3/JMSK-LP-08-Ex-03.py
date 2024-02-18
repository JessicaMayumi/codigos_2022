n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

m = ( n1 + n2 ) / 2


if m<5.0 or n1<3 or n2<3:
    print("Sua média foi: {:.1f} - Em Exame Final " .format(m))
    nf = 10 - m
    print("Voce precisa tirar pelo menos {:.1f} no Exame Final " .format(nf))

else:
    print("Sua média foi: {:.1f} - Aprovado!" .format(m))
