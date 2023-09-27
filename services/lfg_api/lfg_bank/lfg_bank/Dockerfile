# Estágio 1: Preparação
FROM python:3.8 as base

# setando variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# definindo o diretório de trabalho no contêiner
WORKDIR /code

# copiando todos os arquivos para o diretório de trabalho
COPY . /code/

# atualizando o pip e instalando requerimentos
RUN pip install -U pip
RUN pip install -r requirements.txt
