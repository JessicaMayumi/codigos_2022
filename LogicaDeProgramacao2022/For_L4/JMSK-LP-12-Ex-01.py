n=int(input("Insira um número: "))
nf = 1
nf_ant = 1
for i in range (1,n+1):
    nf *= i
    print(nf_ant," x ",i, " = ", nf)
    nf_ant = nf

print(n,"! = ",nf)
