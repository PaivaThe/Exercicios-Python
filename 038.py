import random

num2 = int
cont = 0
num1 = random.randint(0, 10)

while num1 != num2:
    num2 = int(input('Tente adivinhar o número que pensei de 1 a 10: '))
    cont += 1

    print('Errou tente de novo\n')

print(f'Parabéns voce acertou, precisou de {cont} tentativas')
