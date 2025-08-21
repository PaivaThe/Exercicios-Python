# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

num = int(input('Digite a quantidade de números que voce quer saber da sequencia de Fibonacci: '))
cont = 0
a, b = 0, 1

while cont < num:
    print(f'{a}', end='-')
    a,b = b, a + b
    cont += 1

print(f'Fim')