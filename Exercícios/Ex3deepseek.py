#Exercício 3 — Calculadora simples
#Conceitos: os mesmos do exercício 2, mas com várias operações.

#Peça dois números e mostre:

#soma

#subtração

#multiplicação

#divisão


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
média = (numero1 + numero2) / 2   


if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "não é possível dividir por zero"


print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Média: {média}")
