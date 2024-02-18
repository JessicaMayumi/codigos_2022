n = int ( input ( "Insira um número: "))
i = 1
a = 0
while i <= n:
    a += 1/(2*i-1)
    i += 1

print ("{:.2f}".format(a))