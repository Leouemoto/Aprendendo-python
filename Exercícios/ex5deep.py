#Exercício 4 — Par ou ímpar

#Peça um número e diga se ele é par ou ímpar.

#Dica: em Python, numero % 2 retorna o resto da divisão por 2. Se o resto for 0, o número é par.

try:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
except ValueError:
    print("O input só pode ser um número inteiro.")