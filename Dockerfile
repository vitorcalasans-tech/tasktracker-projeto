# Imagem base: Python 3.11 na versão "slim" (enxuta), menor e mais rápida de baixar
FROM python:3.11-slim

# Pasta de trabalho dentro do container; os próximos comandos rodam a partir dela
WORKDIR /app

# Faz o Python mostrar as mensagens na hora, sem guardar em buffer
ENV PYTHONUNBUFFERED=1

# Copia o código-fonte do projeto para dentro do container
COPY src/ /app/src/

# Comando executado quando o container inicia: abre o menu do TaskTracker
CMD ["python", "src/main.py"]
