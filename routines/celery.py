import os
from celery import Celery
# from celery import task
from celery.schedules import crontab
from datetime import timedelta

# from rest_framework.generics import get_object_or_404

# from ..api.models import NewsTag

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'on_comment.settings')


app = Celery('on_comment')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(1.0, test.s('hello'), name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(1.5, test.s('world'), expires=10)
#
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )

@app.task(name='aa')
def test():
    # news_tag = get_object_or_404(NewsTag, tag_name='people')
    print(111)


app.conf.beat_schedule = {
    'run-people': {
        'task': 'api.tasks.get_people_news',
        'schedule': crontab(minute='*/1')
        },

    'run-realt': {
            'task': 'api.tasks.get_realt_news',
            'schedule': crontab(minute='*/1')
            },

    'run-tech': {
            'task': 'api.tasks.get_tech_news',
            'schedule': crontab(minute='*/1')
            },

    }