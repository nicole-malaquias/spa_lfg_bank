#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py create_admin
python manage.py create_initial_config_fields

echo "Starting server"

pip install django-cors-headers

# Inicialize o Celery em segundo plano
celery -A lfg_bank worker


# Inicialize o Django
python manage.py runserver 0.0.0.0:8000



