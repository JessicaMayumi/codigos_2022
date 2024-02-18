p1 = input ("Insira uma palavra: ")
p2 = input ("Insira outra palavra: ")

x = 0
y = 0

#suponhamos que sejam iguais
conf=True

if len(p1)!=len(p2):
    print ("As duas palavras não são inversas.")

else:
    for i in range(len(p1)):
        if p1[i-1] == p2[-i]:
            conf = True
        else:
            conf = False
            break

    if conf:
        print ("'{}' é inversa de '{}'.".format(p1,p2))
    else:
        print ("As duas palavras não são inversas.")