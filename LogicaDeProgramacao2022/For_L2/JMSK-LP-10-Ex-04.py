total = 0
for i in range(85, 908):
    if i%2==0:
        print ( i, end="  " )
        total = total + i
print ()
print ( "total da soma: ",total )