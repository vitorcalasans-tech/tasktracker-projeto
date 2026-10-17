"""
TaskTracker - Fase 2
Aplicação de linha de comando (CLI) para cadastrar e listar tarefas.

Autor: Vitor Calasans Vieira Corrêa da Costa
Curso: Ciência de Dados - CEUB
"""

from datetime import datetime

# Lista que guarda todas as tarefas enquanto o programa está aberto.
# Cada tarefa é um dicionário com: titulo, descricao, prioridade,
# data_limite e status.
tarefas = []

# Opções aceitas para prioridade. A chave é o que o usuário digita
# (já em minúsculas) e o valor é como a prioridade fica gravada.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


# ----------------------------------------------------------------------
# Funções de validação (regras de negócio)
# ----------------------------------------------------------------------

def ler_titulo():
    """Pede o título até que o usuário digite algo que não seja vazio."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("❌ Erro: o título é obrigatório e não pode ficar vazio. Tente novamente.\n")


def ler_prioridade():
    """Pede a prioridade até que seja Alta, Média (ou Media) ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta / Média / Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("❌ Erro: prioridade inválida. Digite apenas Alta, Média ou Baixa.\n")


def ler_data_limite():
    """Pede a data no formato DD/MM/AAAA e não aceita datas no passado."""
    while True:
        entrada = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(entrada, "%d/%m/%Y").date()
        except ValueError:
            print("❌ Erro: data inválida. Use o formato DD/MM/AAAA (ex.: 25/10/2026).\n")
            continue

        if data < datetime.now().date():
            print("❌ Erro: a data limite não pode ser anterior a hoje.\n")
            continue

        return entrada


# ----------------------------------------------------------------------
# Funcionalidades do menu
# ----------------------------------------------------------------------

def cadastrar_tarefa():
    """Coleta os dados, monta o dicionário da tarefa e salva na lista."""
    print("\n--- CADASTRAR NOVA TAREFA ---")

    titulo = ler_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",  # definido automaticamente no cadastro
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


# Só executa o menu quando o arquivo é rodado diretamente
# (python src/main.py), e não quando é importado por outro arquivo.
if __name__ == "__main__":
    main()
