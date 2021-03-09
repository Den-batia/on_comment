from celery import shared_task
from .webdriver.webdriver import ocra


@shared_task(soft_time_limit=30)
def get_people_news():
    from .parser import Parser
    try:
        ocra.init_browser()
        if ocra.browser:
            Parser.get_people(ocra.browser)
            ocra.quite_browser()
        else:
            print('noooooooooooooooooooo')
            return
    except Exception as e:
        print(e)
        # ocra.quite_browser()



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

