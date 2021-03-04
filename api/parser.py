from .webdriver.webdriver import Ocra
from bs4 import BeautifulSoup as bs
import requests
import datetime


class Parser:

    PEOPLE_URL = 'https://people.onliner.by'
    REALT_URL = 'https://realt.onliner.by'
    TETH_URL = 'https://tech.onliner.by'
    AUTO_URL = 'https://auto.onliner.by'

    @classmethod
    def _get_tag_requests(cls, url, session, str_date):
        dom = session.get(f'{url}/{str_date}').text
        soup = bs(dom, 'html.parser')
        list_of = soup.find_all('div', class_='news-tidings__item')
        ocra = Ocra.get_html_js()
        for i in list_of:
            try:
                cls._get_news(i, url, ocra)
            except Exception:
                continue
        ocra.quit()
    @classmethod
    def _get_news(cls, el, url, ocra):

        data_post_date = el['data-post-date']
        news_link = el.find('a', class_='news-tiles__stub')
        if not news_link:
            link = el.find('a', class_='news-tidings__stub')['href']
            news_text = el.span.text
            img = el.find('div', class_='news-tidings__image')['style']

        else:
            link = news_link['href']
            news_text = el.find('div', class_='news-tiles__subtitle').text
            img = el.find('div', class_='news-tiles__image')['style']

        news_text = news_text.strip()
        news_img_link = img[img.find('https'):-2]

        link = url + link
        ocra.get(link)

        html = ocra.page_source
        soup = bs(html, 'html.parser')
        top_comment = soup.find('div', class_='news-comment__speech news-comment__speech_base').p.text

        print({'post_date': data_post_date,
               'news_text': news_text,
               'news_img_link': news_img_link,
               'news_link': link,
               'top_comment': top_comment})

    @classmethod
    def _get_session(cls, base_url):
        with requests.Session() as session:
            str_date = datetime.date.today().strftime("%Y/%m/%d")
            cls._get_tag_requests(base_url, session, str_date)

    @classmethod
    def get_people(cls):
        cls._get_session(cls.PEOPLE_URL)

    @classmethod
    def get_realt(cls):
        cls._get_session(cls.REALT_URL)

    @classmethod
    def get_tech(cls):
        cls._get_session(cls.TETH_URL)


