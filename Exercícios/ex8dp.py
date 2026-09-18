#Exercício 7 — Soma de N números

#Peça um número inteiro n ao usuário e depois peça n números. No final, mostre a soma de todos eles.
try:
    n = int(input("Digite o número de valores que deseja somar: "))
    soma = 0
    for contador in range(n):
        numero = float(input(f"Digite o {contador+1}º número: "))
        soma = soma + numero
    print(f"A soma dos {n} números é: {soma}")
except ValueError:
    print("O input só pode ser um número.")

try:
    n = int(input("Digite o número de valores que deseja somar: "))
    soma = 0
    contador = 0

    while contador < n:
        numero = float(input(f"Digite o {contador+1}º número: "))
        soma += numero
        contador += 1

    print(f"A soma dos {n} números é: {soma}")
except ValueError:
    print("O input só pode ser um número.")