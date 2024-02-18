# Multiplicamos a temperatura em ºC por 1,8 e somamos 32 ao resultado.
print ("Celsius\tFahrenheit")

i = 0


while i <= 100:
    f = (i*1.8)+32
    print ("{}°C\t{}°F".format(i,f))
    i += 10
