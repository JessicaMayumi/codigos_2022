print ("Qual o melhor Sistema Operacional para uso em servidores?")
"""
As possíveis resposta_ints são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
"""

nomes = ["Windows","Unix","Linux","Netware","Mac","Outros"]
votos = [0,0,0,0,0,0]
porcentagem = [0,0,0,0,0,0]

#votos
while True:
    resposta = input ("Insira um n° de 1 à 6: ")

    if resposta== "":
        break
    
    resposta_int= int(resposta)
    votos[resposta_int-1]+=1

#porcentagem
    soma = sum(votos)
    for i in range(len(porcentagem)):
        porcentagem[i]=(votos[i]/soma)*100

 

#resultado
for x in range(len(nomes)):
    print ("{}\t\t {}\t {:.2f}".format(nomes[x],votos[x],porcentagem[x]))

print ("Total \t\t {}".format(soma,))
