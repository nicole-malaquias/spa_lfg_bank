# Estágio 1: Preparação
FROM python:3.8 AS base

# setando variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# definindo o diretório de trabalho no contêiner
WORKDIR /code

# copiando todos os arquivos para o diretório de trabalho
COPY requirements.txt /code/

# atualizando o pip e instalando requerimentos
RUN pip install -U pip
RUN pip install -r /code/requirements.txt

# =============================================================================
# dev - Instala dependências de dev e copia o código fonte
# =============================================================================
FROM base AS dev
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY . /code/


FROM dev AS DevService
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
