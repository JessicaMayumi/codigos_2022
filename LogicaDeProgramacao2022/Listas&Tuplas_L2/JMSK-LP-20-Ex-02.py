import random
vezes = [0,0,0,0,0,0]
lados = [1,2,3,4,5,6]

for i in range(100):
    n = random.randint(1,6)
    vezes[n-1]+= 1

for i in range(len(lados)):
    print ("{}\t{}".format(lados[i],vezes[i]))
