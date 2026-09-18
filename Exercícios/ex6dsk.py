#Exercício 5 — Maior de dois números, mas agora com try/except. Ele vai te fazer praticar if, elif e else juntos.

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if numero1 > numero2:
        print(f"O primeiro número é maior que o segundo número.")
    elif numero2 > numero1:
        print(f"O segundo número é maior que o primeiro número.")
    else:
        print(f"Os números {numero1} e {numero2} são iguais.")
except ValueError:
    print("O input só pode ser um número.")