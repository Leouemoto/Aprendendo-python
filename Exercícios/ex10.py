try:
    lista = []
    while True:
        item = input("Digite um Item (ou 'sair' para encerrar): ")
        if item == "sair":
            break
        lista.append(item)
        print(f"Item adicionado: {item}")

    print("\nLista de compras:")
    for item in lista:
        print(f"- {item}")
    print(f"\nTotal de itens: {len(lista)}")
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")

    
