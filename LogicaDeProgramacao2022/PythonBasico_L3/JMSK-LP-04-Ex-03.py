centavos = int ( input ("Digite o valor dos centavos: "))

moeda_50 = ( centavos // 50 )
moeda_25_1 = ( centavos % 50 )
moeda_25_2 = ( moeda_25_1 //25 )
moeda_10_1 = ( moeda_25_1 % 25)
moeda_10_2 = ( moeda_10_1 //10)
moeda_5_1 = ( moeda_10_1 % 10)
moeda_5_2 = ( moeda_5_1 //5)
moeda_1_1 = ( moeda_5_1 % 5)
moeda_1_2 = ( moeda_1_1 //1)
 
print ( "N° de moedas de 50 centavos: ", moeda_50 )
print ( "N° de moedas de 25 centavos: ", moeda_25_2 )
print ( "N° de moedas de 10 centavos: ", moeda_10_2 )
print ( "N° de moedas de 5 centavos: ", moeda_5_2 )
print ( "N° de moedas de 1 centavos: ", moeda_1_2 )