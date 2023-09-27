from .celery import app as celery_app
from .celery import hello

__all__ = ('celery_app',)