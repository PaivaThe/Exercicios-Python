num1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
soma = 0

for c in range(0, 10):
   print(f'{num1}')
   soma += num1 
   num1 += razao

print('FIM')