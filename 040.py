# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

import math

num_fatorado = int(input('Digite um número para saber seu fatorial: '))
cont = num_fatorado
resultado = math.factorial(num_fatorado)

while cont > 0: 
    print(f'{cont}', end = '')
    print(' x ' if cont > 1 else f' = {resultado}', end ='') 
    cont -= 1

