quantidade=0
total = 0
while True:
    n = input ("Insira um número, caso deseje para tecle 'Enter': " )
    if n == "":
       break
    total = total + int(n)
    quantidade += 1

media = total/quantidade

print ("Total: ",total)
print ("Média: ", media)

