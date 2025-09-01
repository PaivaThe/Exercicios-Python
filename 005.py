#Programa que le dados e retorne uma ordem aleatoria
import random

a = input("Primeiro aluno: ")
b = input("Segundo aluno: ")
c = input("Terceiro aluno: ")
d = input("Quarto aluno: ")

list = [a, b, c, d]

random.shuffle(list)

print(f'A ordem de apresentaçao é {list}')