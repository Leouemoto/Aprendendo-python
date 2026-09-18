#Exercício 7 — Soma de N números

#Peça um número inteiro n ao usuário e depois peça n números. No final, mostre a soma de todos eles.
try:
    n = int(input("Digite o número de valores que deseja somar: "))
    soma = 0
    for i in range(n):
        numero = float(input(f"Digite o {i+1}º número: "))
        soma += numero
    print(f"A soma dos {n} números é: {soma}")
except ValueError:
    print("O input só pode ser um número.")