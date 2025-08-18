#Pedra, Papel ou Tesoura

import random

opcoes = ['Pedra', 'Papel', 'Tesoura']

escolha_pc = random.choice(opcoes)

escolha_jogador = str(input('Faça sua escolha entre Pedra, Papel ou Tesoura: '))

print(f'A escolha da máquina foi: {escolha_pc}')
print(f'Sua escolha foi: {escolha_jogador}')

if escolha_pc == 'Tesoura' and escolha_jogador == 'Papel':
    print('A máquina ganhou')

elif escolha_pc == 'Tesoura' and escolha_jogador == 'Pedra':
    print('O jogador ganhou')

elif escolha_pc == 'Tesoura' and escolha_jogador == 'Tesoura':
    print('Empate')

elif escolha_pc == 'Papel' and escolha_jogador == 'Tesoura':
    print('O jogador ganhou')

elif escolha_pc == 'Papel' and escolha_jogador == 'Pedra':
    print('A máquina ganhou')

elif escolha_pc == 'Papel' and escolha_jogador == 'Papel':
    print('Empate')

elif escolha_pc == 'Pedra' and escolha_jogador == 'Tesoura':
    print('A máquina ganhou')

elif escolha_pc == 'Pedra' and escolha_jogador == 'Papel':
    print('O jogador ganhou')

elif escolha_pc == 'Pedra' and escolha_jogador == 'Pedra':

    print('Empate')
