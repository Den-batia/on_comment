from celery import shared_task


@shared_task
def get_people_news():
    from .parser import Parser
    Parser.get_people()


@shared_task
def get_realt_news():
    from .parser import Parser
    Parser.get_realt()


@shared_task
def get_tech_news():
    from .parser import Parser
    Parser.get_tech()

