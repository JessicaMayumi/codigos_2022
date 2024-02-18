import random
def sorteia_dado():
    return random.randint(1,6)

# lista de quantidade de vezes
quantidade = [0,0,0,0,0,0]


for i in range(1000000):
    quantidade[sorteia_dado()-1]+=1
    

for i in range (len(quantidade)):
    print ("{} = {:.2f}%." .format (i+1, (quantidade[i-1])/1000000*100))