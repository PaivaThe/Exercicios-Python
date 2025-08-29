import math

b = float(input("Digite o Cateto oposto: "))
c = float(input("Digite o cateto adjacente: "))
a = math.sqrt(b ** 2 + c ** 2) 

print(f"A hipotenusa é {a:.2f}")