l1 = []
l2 = []

for i in range(20):
    n = int(input("Insira um n°: "))
    if n%2==0:
        l1.append(n)
    else:
        l2.append(n)

print ("n° pares: ",l1)
print ("n° ímpares: ",l2)
