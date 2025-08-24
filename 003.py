# Programa que le um angulo qualquer e mostre o valor do seno, cosseno e tangente

import math

angulo = float(input("Digite o angulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno de {angulo} é {seno:.2f}')
print(f'O cosseno de {angulo} é {cosseno:.2f}')
print(f'A tangente de {angulo} é {tangente:.2f}')
