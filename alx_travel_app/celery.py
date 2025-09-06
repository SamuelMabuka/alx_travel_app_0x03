import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')

# Use RabbitMQ as the broker
app.conf.broker_url = 'amqp://guest:guest@localhost:5672//'

# Load task modules from all registered apps
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
