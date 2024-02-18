data = input ("Insira sua data de nascimento (dd/mm/aaaa): ")

dia = data[0:2]
ano = data[6:10]
mes = data[3:5]

if data[3:5] == "01":
    mes = "janeiro"
elif data[3:5] == "02":
    mes = "fevereiro"
elif data[3:5] == "03":
    mes = "março"
elif data[3:5] == "04":
    mes = "abril"
elif data[3:5] == "05":
    mes = "maio"
elif data[3:5] == "06":
    mes = "junho"
elif data[3:5] == "07":
    mes = "julho"
elif data[3:5] == "08":
    mes = "agosto"
elif data[3:5] == "09":
    mes = str("setembro")
elif data[3:5] == "10":
    mes = "outubro"
elif data[3:5] == "11":
    mes = "novembro"
else:
    mes = "dezembro"

print ("Você nasceu em {} de {} de {}." .format (dia, mes, ano))

#maneira mais facil de fazer com 'dicionarios no python'