s1 = input ("Insira uma palavra: ")
s2 = input ("Insira uma palavra: ")

novo = ""

x = 0
y = 0

l1 = len(s1)
l2 = len(s2)

while x<l1 and y<l2:
    novo += s1[x] + s2[y]
    x += 1
    y += 1

while x<l1:
    novo+= s1[x]
    x+=1

while y<l2:
    novo+= s2[y]
    y+=1

print (novo)