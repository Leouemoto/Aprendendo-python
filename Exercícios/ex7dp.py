#Exercício 6 — Contagem regressiva

#Peça um número inteiro ao usuário e mostre uma contagem regressiva até 0

try:
    numero = int(input("Digite um número inteiro para iniciar a contagem regressiva: "))

    if numero < 0:
        print("Por favor, digite um número inteiro não negativo.")
    else:
        print("Contagem regressiva:")
        for  contador in range(numero, -1,-1):
            print(contador)
except ValueError:
    print("O input só pode ser um número inteiro.") 

    # Exercício 6 — Contagem regressiva

# Peça um número inteiro ao usuário e mostre uma contagem regressiva até 0

try:
    numero = int(input("Digite um número inteiro para iniciar a contagem regressiva: "))

    if numero < 0:
        print("Por favor, digite um número inteiro não negativo.")
    else:
        print("Contagem regressiva:")
        contador = numero

        while contador >= 0:
            print(contador)
            contador -= 1

except ValueError:
    print("O input só pode ser um número inteiro.")