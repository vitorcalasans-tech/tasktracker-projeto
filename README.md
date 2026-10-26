# TaskTracker

Aplicação de linha de comando (CLI) em Python para organizar tarefas de estudantes que estão conciliando faculdade, estágio e vida pessoal. A aplicação é empacotada com **Docker**, então roda do mesmo jeito em qualquer computador.

Projeto do **Bootcamp II** (Ciência de Dados — CEUB), construído em três fases:

| Fase | Papel | Entrega |
|---|---|---|
| 1 | Arquiteto(a) de Software | Planejamento lógico e pseudocódigo ([`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf)) |
| 2 | Desenvolvedor(a) | Menu CLI em Python com regras de negócio ([`src/main.py`](src/main.py)) |
| 3 | Engenheiro(a) DevOps | Conteinerização com `Dockerfile` e orquestração com `docker-compose.yml` |

**Autor:** Vitor Calasans Vieira Corrêa da Costa

---

## 🐳 Executando com Docker

**Pré-requisito:** ter o [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e aberto. Todos os comandos abaixo devem ser executados **na pasta raiz do projeto** (onde está o `Dockerfile`).

### 1. Como construir a imagem

```bash
docker build -t tasktracker-app .
```

### 2. Como rodar o container em modo isolado

```bash
docker run -it --rm tasktracker-app
```

### 3. Como rodar via orquestração (Recomendado)

```bash
docker compose run --rm tasktracker
```

> Na primeira execução, o `docker compose` constrói a imagem automaticamente se ela ainda não existir.

### O que cada parte significa

| Trecho | Significado |
|---|---|
| `docker build` | Lê o `Dockerfile` e gera a **imagem** (o pacote com Python + código). |
| `-t tasktracker-app` | Dá o nome (*tag*) `tasktracker-app` à imagem. |
| `.` | Usa a pasta atual como contexto do build. |
| `docker run` | Cria e inicia um **container** a partir da imagem. |
| `-it` | `-i` mantém a entrada aberta e `-t` cria um terminal. Sem isso, o `input()` do menu não funciona. |
| `--rm` | Apaga o container ao sair, para não acumular containers parados. |
| `docker compose run` | Executa o serviço `tasktracker` definido no `docker-compose.yml`, já com `stdin_open` e `tty` configurados. |

---

## Arquivos de infraestrutura

### `Dockerfile` — a receita da imagem

```dockerfile
FROM python:3.11-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY src/ /app/src/
CMD ["python", "src/main.py"]
```

| Instrução | Decisão técnica |
|---|---|
| `FROM python:3.11-slim` | Base leve com Python 3.11: imagem menor e mais rápida de baixar que a versão completa. |
| `WORKDIR /app` | Define `/app` como a pasta central de operações dentro do container. |
| `ENV PYTHONUNBUFFERED=1` | Faz o Python mostrar as mensagens imediatamente, sem guardar em buffer. |
| `COPY src/ /app/src/` | Copia só o código-fonte para a imagem (sem docs ou arquivos do Git). |
| `CMD ["python", "src/main.py"]` | Comando disparado quando o container inicia: abre o menu. |

### `docker-compose.yml` — o maestro da execução

A CLI usa `input()`, e um container isolado não recebe teclado por padrão. O compose resolve isso com duas opções:

- `stdin_open: true` mantém o canal de entrada de dados aberto;
- `tty: true` aloca um terminal virtual, simulando o seu console.

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

> As tarefas ficam guardadas na memória enquanto o programa está aberto. Ao sair, a lista é apagada.

## Tecnologias utilizadas

- **Python 3.11** (somente a biblioteca padrão)
- **Docker** e **Docker Compose** para empacotamento e execução
- **Git** e **GitHub** para versionamento e publicação

## Estrutura do repositório

```
tasktracker-projeto/
├── .gitignore                  # Arquivos ignorados pelo Git
├── docs/
│   └── planejamento_logico.pdf # Planejamento da Fase 1
├── src/
│   └── main.py                 # Código Python da Fase 2
├── Dockerfile                  # Receita da imagem (Fase 3)
├── docker-compose.yml          # Orquestração da execução interativa (Fase 3)
└── README.md                   # Esta documentação
```

## Executando sem Docker (opcional)

Com o Python 3 instalado, na raiz do projeto:

```bash
python src/main.py
```

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
Título da tarefa:
❌ Erro: o título é obrigatório e não pode ficar vazio. Tente novamente.

Título da tarefa: Estudar Docker
Descrição (opcional): Revisar o Dockerfile
Prioridade (Alta / Média / Baixa): Alta
Data limite (DD/MM/AAAA): 30/12/2026

✅ Tarefa 'Estudar Docker' cadastrada com sucesso!
```
