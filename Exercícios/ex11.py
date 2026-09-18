#Exercício 10 — Notas da turma

#Peça ao usuário quantos alunos há na turma. Depois, peça a nota de cada aluno e guarde numa lista. No final, mostre:

#Todas as notas digitadas

#A média da turma

#A maior nota

#A menor nota

#Quantos alunos ficaram acima da média

try:
    n = int(input("Digite o número de alunos na turma: "))
    notas = []

    for i in range(n):
        nota = float(input(f"Digite a nota do {i+1}º aluno: "))
        notas.append(nota)

    media = sum(notas) / n if n > 0 else 0
    maior_nota = max(notas) if notas else None
    menor_nota = min(notas) if notas else None
    acima_da_media = sum(1 for nota in notas if nota > media)

    print("\nLista de notas digitadas:")
    print(notas)

    print("\nNotas da turma:")
    for i, nota in enumerate(notas, start=1):
        print(f"Aluno {i}: {nota}")

    print(f"\nMédia da turma: {media}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Número de alunos acima da média: {acima_da_media}")
except ValueError:
    print("O input só pode ser um número.")
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")
