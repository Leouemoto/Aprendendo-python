import json
from pathlib import Path


ARQUIVO_TAREFAS = Path(__file__).with_name("tarefas.json")


def carregar_tarefas():
	if not ARQUIVO_TAREFAS.exists():
		return []

	try:
		with ARQUIVO_TAREFAS.open("r", encoding="utf-8") as arquivo:
			tarefas = json.load(arquivo)
	except (json.JSONDecodeError, OSError):
		print("Não foi possível carregar as tarefas. Começando com uma lista vazia.")
		return []

	return tarefas if isinstance(tarefas, list) else []


def salvar_tarefas(tarefas):
	with ARQUIVO_TAREFAS.open("w", encoding="utf-8") as arquivo:
		json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


def mostrar_menu():
	print("\n1 - Adicionar tarefa")
	print("2 - Listar tarefas")
	print("3 - Concluir tarefa")
	print("4 - Remover tarefa")
	print("5 - Sair")


def listar_tarefas(tarefas):
	if not tarefas:
		print("Nenhuma tarefa cadastrada.")
		return

	for tarefa in tarefas:
		marcador = "X" if tarefa["concluida"] else " "
		print(f"[{marcador}] {tarefa['id']} - {tarefa['descricao']}")


def pedir_id():
	try:
		return int(input("Digite o id da tarefa: "))
	except ValueError:
		print("Id inválido. Digite um número inteiro.")
		return None


def adicionar_tarefa(tarefas):
	descricao = input("Digite a descrição da tarefa: ").strip()
	if not descricao:
		print("A descrição não pode ficar vazia.")
		return

	proximo_id = max((tarefa["id"] for tarefa in tarefas), default=0) + 1
	tarefas.append({"id": proximo_id, "descricao": descricao, "concluida": False})
	salvar_tarefas(tarefas)
	print("Tarefa adicionada com sucesso.")


def concluir_tarefa(tarefas):
	id_tarefa = pedir_id()
	if id_tarefa is None:
		return

	for tarefa in tarefas:
		if tarefa["id"] == id_tarefa:
			tarefa["concluida"] = True
			salvar_tarefas(tarefas)
			print("Tarefa concluída com sucesso.")
			return

	print("Tarefa não encontrada.")


def remover_tarefa(tarefas):
	id_tarefa = pedir_id()
	if id_tarefa is None:
		return

	for indice, tarefa in enumerate(tarefas):
		if tarefa["id"] == id_tarefa:
			tarefas.pop(indice)
			salvar_tarefas(tarefas)
			print("Tarefa removida com sucesso.")
			return

	print("Tarefa não encontrada.")


def main():
	tarefas = carregar_tarefas()

	while True:
		mostrar_menu()
		opcao = input("Escolha uma opção: ").strip()

		if opcao == "1":
			adicionar_tarefa(tarefas)
		elif opcao == "2":
			listar_tarefas(tarefas)
		elif opcao == "3":
			concluir_tarefa(tarefas)
		elif opcao == "4":
			remover_tarefa(tarefas)
		elif opcao == "5":
			salvar_tarefas(tarefas)
			print("Tarefas salvas. Até logo!")
			break
		else:
			print("Opção inválida. Escolha uma opção de 1 a 5.")


if __name__ == "__main__":
	main()
