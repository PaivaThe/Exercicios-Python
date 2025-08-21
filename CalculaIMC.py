# Inicio do código

# Declarando as variáveis
print('\033[35m='*40)
print('CALCULADORA IMC')
print('='*40)

peso = float(input("\033[36mDigite seu peso em KG: "))

altura = float(input("Digite sua altura em M: "))


imc = peso / (altura * altura)

def  calcula_classificacao (imc):

    if imc < 18.5:
        return "Abaixo do peso"

    elif  18.5 <= imc < 25:
        return "Peso ideal"

    elif 25 <= imc < 30:
        return "Acima do peso"

    elif 30 <= imc < 34:
        return "Obeso"

    else:
        return "Muito obeso"

print(f"\033[30;0mSeu IMC é: \033[1;34;40m{imc:.2f}")
print(f"\033[30;0mClassificaçao: {calcula_classificacao(imc)}\033[m")   
    