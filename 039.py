#Crie um programa que leia dois valores e mostre um menu na tela:

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

opcao = ''

while opcao != '5':
    print('\n[1]Soma')
    print('[2]Multiplicar')
    print('[3]Maior')
    print('[4]Novos números')
    print('[5]Sair do programa\n')
    opcao = str(input('\nEscolha uma opção para sua operação: '))
    

    if opcao == '1':
        soma = num1 + num2
        print(f'\nA soma dos números é {soma:.2f}\n')

    if opcao == '2':
        multi = num1 * num2
        print(f'\nO resultado é {multi:.2f}')
    
    if opcao == '3':
        if num1 > num2:
            print(f'\nO maior é {num1:.2f}')
        else:
            print(f'\nO maior é {num2:.2f}')
    
    if opcao == '4':
        num1 = float(input('Digite novamente o primeiro número: '))
        num2 = float(input('Digite novamente o segundo número: '))
    
print('\nFim, obrigado por usar o programa')