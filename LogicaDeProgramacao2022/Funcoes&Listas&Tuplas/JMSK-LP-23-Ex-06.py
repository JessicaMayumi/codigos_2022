def vogais_consoantes(texto):
    vogais = ""
    consoantes = ""
    for i in texto:
        if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u":
            vogais += i
        else:
            consoantes += i
    return vogais, consoantes

string = input ("Insira uma palavra: ")
print ("String com as vogais da palavra '{}'.\nString com as consoantes da palavra '{}'.".format(vogais_consoantes(string)[0], vogais_consoantes(string)[1]))