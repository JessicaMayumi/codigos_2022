suco = float(input("Valor do Suco: R$"))
prato_principal = float(input("Valor do Prato Principal: R$"))
sobremesa = float(input("Valor da Sobremesa: R$"))

soma = ( suco + prato_principal + sobremesa )
acrescimo = ( soma / 10 )
total_da_conta = ( soma + acrescimo )

print("O valor da sua conta é R$ %.2f" % total_da_conta)
