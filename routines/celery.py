import os
from celery import Celery
from celery.exceptions import SoftTimeLimitExceeded, TimeLimitExceeded
from celery.schedules import crontab
from api.webdriver.webdriver import ocra


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'on_comment.settings')
app = Celery('on_comment')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-people': {
        'task': 'routines.celery.get_people_news',
        # 'schedule': crontab(minute='*/20', hour='8-23'),
        'schedule': 30

    }
}


@app.task(soft_time_limit=30, time_limit=40)
def get_people_news():
    from .parser import Parser
    browser = ocra.get_browser()
    try:
        Parser.get_people(browser)
        browser.quit()
    except SoftTimeLimitExceeded:
        browser.quit()
    except TimeLimitExceeded as e:
        browser.quit()