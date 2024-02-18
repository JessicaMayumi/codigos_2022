n = input ("Insira um n°: ")

novo = ""

for i in n:
    if int(i)==9:
        novo += "0"
    else:
        novo += str(int(i)+1)

print (novo)