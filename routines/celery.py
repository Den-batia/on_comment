import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'on_comment.settings')
app = Celery('on_comment')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()


app.conf.beat_schedule = {
    'run-people': {
        'task': 'routines.celery.get_people_news',
        # 'schedule': crontab(minute='*/20', hour='8-23'),
        'schedule': 10,

    }
}


@app.task()
def get_people_news():
    from .parser import Parser
    Parser.get_people()