n = int ( input("Insira um número: "))
i = 1
a = 0
while i <= n:
    a += (n-(i-1))/(i)
    i +=1
    
print (a)