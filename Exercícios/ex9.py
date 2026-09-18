#Exercício 8 — Maior e menor número

#Peça n números ao usuário e, no final, mostre:

#A soma de todos

#A média

#O maior número digitado

#O menor número digitado

try:
    n = int(input("Digite o número de valores que deseja informar: "))
    soma = 0
    maior = None
    menor = None

    for contador in range(n):
        numero = float(input(f"Digite o {contador+1}º número: "))
        soma += numero

        if maior is None or numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero

    media = soma / n if n > 0 else 0

    print(f"A soma dos {n} números é: {soma}")
    print(f"A média dos {n} números é: {media}")
    print(f"O maior número digitado é: {maior}")
    print(f"O menor número digitado é: {menor}")

except ValueError:
    print("O input só pode ser um número.")