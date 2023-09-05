import os
import django
import sys

package_path = os.path.dirname(os.path.abspath(__file__))


from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lfg_bank.settings')
if not os.environ.get('DJANGO_ALREADY_SETUP', False):
    os.environ['DJANGO_ALREADY_SETUP'] = '1'
    django.setup()
    
app = Celery('lfg')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'pyamqp://guest:guest@broker//'  # Usando o nome do serviço do Docker
app.autodiscover_tasks()
app.conf.imports = ('lfg_bank.celery',)
app.conf.task_routes = {
    'lfg_bank.celery.hello': {'queue': 'hello'},
    'lfg_bank.celery.debug_task': {'queue': 'debug'},
}
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

# Load task modules from all registered Django apps.
# Define as filas e trocas (Exchanges) do Celery

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task(name='hello')
def hello():
    return 'hello world'