soma = 0
cont = 0

for c in range(0, 6):
    num1 = int(input('Digite um número int: '))

    if num1 % 2 == 0:
        soma += num1
        cont += 1

print(f'A soma dos números pares é: {soma} ')
print(f'Havia {cont} números pares')
