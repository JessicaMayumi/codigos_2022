for i in range ( 100, -1, -5):
    print ( i , end= "  ")

print ()

for i in range ( 0, 101, 5):
    print ( 100 - i , end="  ")

print ()

for i in range ( 0, 101 ):
    if i%5==0:
        print ( 100 - i, end="  ")
