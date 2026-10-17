"""
TaskTracker - Fase 2
Aplicação de linha de comando (CLI) para cadastrar e listar tarefas.

Autor: Vitor Calasans Vieira Corrêa da Costa
Curso: Ciência de Dados - CEUB
"""

# Lista que guarda todas as tarefas enquanto o programa está aberto.
tarefas = []


def cadastrar_tarefa():
    """Coleta os dados, monta o dicionário da tarefa e salva na lista."""
    print("\n--- CADASTRAR NOVA TAREFA ---")

    titulo = input("Título da tarefa: ").strip()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = input("Prioridade (Alta / Média / Baixa): ").strip()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }

    tarefas.append(tarefa)
    print(f"\n✅ Tarefa '{titulo}' cadastrada com sucesso!")


def listar_tarefas():
    """Mostra todas as tarefas ou avisa que a lista está vazia."""
    print("\n--- TAREFAS CADASTRADAS ---")

    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        descricao = tarefa["descricao"] or "(sem descrição)"
        print(f"\nTarefa {numero}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {descricao}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite']}")
        print(f"  Status:      {tarefa['status']}")

    print(f"\nTotal: {len(tarefas)} tarefa(s).")


def mostrar_menu():
    """Exibe as opções do menu principal."""
    print("\n==============================")
    print("         TASKTRACKER")
    print("==============================")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    """Loop principal: mostra o menu até o usuário escolher sair."""
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            print("\nAté logo! 👋")
            break
        else:
            print("❌ Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
