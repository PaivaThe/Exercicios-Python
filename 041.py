# Leia primeiro termo e a razão de uma PA, mostre os 10 primeiros termos da progressão usando a estrutura while.

num1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
soma = 0
range = 10

while range > 0:
    print(f'{num1}')
    soma += num1
    num1 += razao 
    range -= 1

print('FIM')