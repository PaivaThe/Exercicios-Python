num1 = int(input('Digite um número inteiro decimal: '))

print('1 - para binário')
print('2 - para octal')
print('3 - para hexadecimal')

opcao = int(input('Escolha uma Opção: '))

def escolha(opcao):
    if opcao == 1:
        return bin(num1) [2:]
    
    elif opcao == 2:
        return oct(num1) [2:]
    
    elif opcao == 3:
        return hex(num1) [2:]

resultado = escolha(opcao)
print(f'Seu resultado é {resultado}')

