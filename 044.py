cont = 0
soma = 0


while num != 999:
    num = int(input('Digite um número: \nCaso queira parar o código digite 999.\n'))
    
    soma += num
    cont += 1

print(f'Foram digitados {cont} números e a soma de todos é {soma - 999}')