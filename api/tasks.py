from celery import shared_task
from .webdriver.webdriver import Ocra


@shared_task(soft_time_limit=30)
def get_people_news():
    from .parser import Parser
    try:
        ocra = Ocra.get_html_js()
        Parser.get_people(ocra)
        ocra.quit()
    except Exception as e:
        print(e)
        ocra.quit()



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
    from .webdriver.webdriver import Ocra
    a = Ocra.get_html_js('https://www.tut.by/')
    print(a)

