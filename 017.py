print('='*40)
print('Analisador de Triangulos')
print('='*40)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmento pode formar um triangulo')
    if r1 == r2 == r3:
        print('É um triangulo Equilátero')
    
    elif r1 == r2 or r1 == r3 or r2 == r3: 
        print('É um trinagulo Isósceles')

    elif r1 != r2 or r1 != r3 or r2 != r3:
        print('É um trinagulo Escaleno')

else:
    print('Nao forma um triangulo')