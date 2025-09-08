#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = 0
soma = 0
num = 0
media = 0

while num != 999:
    num = int(input('Digite um número: \nCaso queira parar o código digite 999.\n'))
    if num != 999:
        soma += num
        cont += 1
    media = soma / cont

print(f'Foram digitados {cont} números e a soma de todos é {soma}')
print(f'A média é {media}')