import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'on_comment.settings')
app = Celery('on_comment')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-people': {
        'task': 'api.tasks.get_people_news',
        'schedule': crontab(minute='*/2')
        },
    # 'run-test_selery': {
    #     'task': 'api.tasks.test_selery',
    #     # 'schedule': crontab(minute='*/1')
    #     'schedule': 2
    #     },

    # 'run-realt': {
    #         'task': 'api.tasks.get_realt_news',
    #         'schedule': crontab(minute='*/1')
    #         },
    #
    # 'run-tech': {
    #         'task': 'api.tasks.get_tech_news',
    #         'schedule': crontab(minute='*/1')
    #         },
    #
    }