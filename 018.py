#Programa para aprovar um empréstimo bancário

valorcasa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = valorcasa / (anos * 12)

if prestacao <= (salario * 0.3):
    print('Emprestimo aprovado!')
    print(f'Valor da sua prestação é: {prestacao}')

else:
    print('Empréstimo negado!')