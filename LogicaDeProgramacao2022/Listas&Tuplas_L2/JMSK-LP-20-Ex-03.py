lista_carros = []
lista_consumo = []
lista_consumo_total = []

for i in range(5):
    carro = input ("Insira a marca de um carro: ")
    consumo = input ("Insira quantos quilômetros ele percorre com apenas 1 litro de combustível: ")

    lista_carros.append(carro)
    lista_consumo.append(consumo)

print ( "Comparativo de Consumo de Combustível" )

for i in range(len(lista_carros)):
    print ("Veículo {}\nNome: {}\nKm por Litro: {}".format(i+1,lista_carros[i],lista_consumo[i]))

print ("Relatório Final")

for i in range(len(lista_carros)):
    consumo_total = 1000/float(lista_consumo[i])*5.25
    lista_consumo_total.append(consumo_total)
    print ("{}  -\t {}\t\t-\t{}\t-\t{:.1f} Litros\t-\tR$ {:.2f}" .format (i+1, lista_carros[i],float(lista_consumo[i]),1000/float(lista_consumo[i]),consumo_total))
    
procurar = lista_consumo_total.index(min(lista_consumo_total))
menor_consumo = lista_carros[procurar]
print ("O carro com menor consumo é o {}.".format(menor_consumo))