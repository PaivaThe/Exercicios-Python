#Programa que le uma lista e faz uma escolha

import random

lista = ["Maçã", "Banana", "Morango", "Abacaxi", "Laranja"]

lista_sorteada = random.choice(lista)

print(f"A opçao sorteada é: {lista_sorteada}")