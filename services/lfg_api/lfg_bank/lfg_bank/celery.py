import os
import django
from celery import Celery

# Obtém o caminho do pacote atual
package_path = os.path.dirname(os.path.abspath(__file__))

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lfg_bank.settings')
if not os.environ.get('DJANGO_ALREADY_SETUP', False):
    os.environ['DJANGO_ALREADY_SETUP'] = '1'
    django.setup()

# Cria uma instância do Celery
app = Celery('lfg_bank')

# Configura o Celery usando as configurações do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Configura a URL do broker (RabbitMQ neste caso)
app.conf.broker_url = 'pyamqp://guest:guest@broker//'

# Configura a descoberta automática de tarefas em aplicativos Django
app.autodiscover_tasks()

# Configura o agendador do Celery para usar o Django Celery Beat
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

# Define tarefas do Celery
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task(name='hello')
def hello():
    return 'hello world'
