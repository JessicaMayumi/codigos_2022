frase = input ("Insira algo: ")

letter=""
for i in frase:
    letter+=i
    print (letter)

#segunda maneira

n = len(frase)
for i in range(n):
    print(frase[:(i+1)])
