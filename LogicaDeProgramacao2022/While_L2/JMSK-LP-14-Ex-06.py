n = int ( input ("Insira um número: "))
a = 0
i = 1
s = -1
while i <= n:
    s = -s
    a += s*(1/i)
    i += 1
print (a)