# Estágio 1: Preparação
FROM python:3.8 AS base

# setando variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# definindo o diretório de trabalho no contêiner
WORKDIR /code

# copiando todos os arquivos para o diretório de trabalho
COPY requirements.txt /code/
COPY . /code/

# concedendo permissão de execução aos arquivos de entrada
RUN chmod +x /code/entrypoint.sh

# atualizando o pip e instalando requerimentos
RUN pip install -U pip
RUN pip install -r /code/requirements.txt

# =============================================================================
# DevService - Configuração do Django
# =============================================================================
FROM base AS DevService
CMD ["/code/entrypoint.sh"]