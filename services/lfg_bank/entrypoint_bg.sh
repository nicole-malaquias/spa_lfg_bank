#!/bin/bash

echo "Starting server"
pip install django-cors-headers

# Inicialize o Celery em segundo plano
celery -A lfg_bank worker

