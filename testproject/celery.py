import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testproject.settings')

app = Celery('testproject')
app.config_from_object('django.conf:settings', namespace='CELERY')

 
app.conf.beat_schedule = {
    'say-hello-every-1-minute': {
        'task': 'mainapp.tasks.say_hello',
        'schedule': crontab(minute='*/1')
    }
}

app.autodiscover_tasks()

