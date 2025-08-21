# Leia primeiro termo e a razão de uma PA, mostre os 10 primeiros termos da progressão usando a estrutura while.

num1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
termo = num1
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    
    while cont <= total:
        print(f'{termo}')
        termo += razao
        cont += 1
    
    mais = int(input('Quantos termos voce quer mostrar a mais? '))


print('FIM')
