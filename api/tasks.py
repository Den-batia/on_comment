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


@shared_task()
def test_selery():
    from .webdriver.webdriver import ocra
    a = ocra.get_html_js('https://www.tut.by/')
    print(a)

