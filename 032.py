num1 = int(input('Digite um número int para descobrir se ele é primo: '))
total_divisores = 0

for c in range(1, num1 + 1):
    if num1 % c == 0:
        total_divisores += 1

if total_divisores == 2:
    print(f'O número {num1} É um número primo!')
elif num1 == 0 or num1 == 1:
    print(f'O número {num1} NÃO é um número primo!')
else:
    print(f'O número {num1} NÃO é um número primo!')