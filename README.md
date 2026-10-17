# TaskTracker

Aplicação de linha de comando (CLI) em Python para organizar tarefas de estudantes que estão conciliando faculdade, estágio e vida pessoal.

Projeto desenvolvido na **Fase 2** do trabalho de Ciência de Dados (CEUB), a partir do planejamento lógico feito na Fase 1 (disponível em [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf)).

**Autor:** Vitor Calasans Vieira Corrêa da Costa

---

## Funcionalidades

- **Cadastrar nova tarefa** com título, descrição, prioridade e data limite.
- **Visualizar as tarefas cadastradas**, com todas as informações organizadas no terminal.
- **Validação dos dados** digitados:
  - o título é obrigatório e não pode ser vazio nem conter só espaços;
  - a prioridade só aceita `Alta`, `Média` (ou `Media`) e `Baixa`;
  - a data limite deve estar no formato `DD/MM/AAAA` e não pode ser anterior a hoje.
- **Status automático:** toda tarefa nova começa como `Pendente`.
- **Aviso de lista vazia** quando ainda não há tarefas cadastradas.

## Tecnologias utilizadas

- **Python 3** (somente a biblioteca padrão, sem instalar nada extra)
- **Git** para o versionamento
- **GitHub** para a publicação do repositório

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md                   # Documentação principal
├── .gitignore                  # Arquivos ignorados pelo Git
├── docs/
│   └── planejamento_logico.pdf # Planejamento da Fase 1
└── src/
    └── main.py                 # Código-fonte da aplicação
```

## Como instalar e executar

1. Tenha o **Python 3** instalado. Para conferir, rode no terminal:
   ```bash
   python --version
   ```
2. Clone o repositório (no GitHub, clique no botão verde **Code** e copie a URL):
   ```bash
   git clone <URL-do-repositório>
   ```
3. Entre na pasta do projeto:
   ```bash
   cd tasktracker-projeto
   ```
4. Execute a aplicação:
   ```bash
   python src/main.py
   ```
   No macOS/Linux, se `python` não funcionar, use `python3 src/main.py`.

## Exemplo de uso

```
==============================
         TASKTRACKER
==============================
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
Escolha uma opção: 1

--- CADASTRAR NOVA TAREFA ---
Título da tarefa: Entregar relatório de estágio
Descrição (opcional): Revisar e enviar ao supervisor
Prioridade (Alta / Média / Baixa): Alta
Data limite (DD/MM/AAAA): 30/10/2026

✅ Tarefa 'Entregar relatório de estágio' cadastrada com sucesso!
```

## Próximos passos

Recursos planejados na Fase 1 que ainda serão implementados: categorias, subtarefas, tarefas recorrentes, cálculo automático do quadrante de prioridade e painel de produtividade.
