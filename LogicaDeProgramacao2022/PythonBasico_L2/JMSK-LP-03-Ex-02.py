data=int(input("Digite uma Data: "))

d=data//10000

x=data%10000
m=x//100

a=x%100

data_invertida=a*10000+m*100+d
print("A data invertida é:" ,data_invertida)