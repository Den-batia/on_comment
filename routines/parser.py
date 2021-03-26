from bs4 import BeautifulSoup as bs
import requests
import datetime
from api.models import News, NewsTag

class Parser:

    PEOPLE_URL = 'https://people.onliner.by'
    REALT_URL = 'https://realt.onliner.by'
    TETH_URL = 'https://tech.onliner.by'
    AUTO_URL = 'https://auto.onliner.by'

    @classmethod
    def _get_tag_requests(cls, url, session, str_date, ocra, tag_name):
        dom = session.get(f'{url}/{str_date}').text
        soup = bs(dom, 'html.parser')
        list_of = soup.find_all('div', class_='news-tidings__item')
        for i in list_of:
            cls._get_news(i, url, ocra, tag_name)

    @classmethod
    def _get_news(cls, el, url, ocra, tag_name):

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
        try:
            top_comment = soup.find('div', class_='news-comment__speech news-comment__speech_base').p.text
            likes = int(soup.find('a', class_='news-comment__button_counter_up').span.text)
            dislikes = int(soup.find('a', class_='news-comment__button_counter_down').span.text)
        except AttributeError as e:
            print('KeyError')
            top_comment = ''
            likes = 0
            dislikes = 0

        obj = {'post_date': data_post_date,
               'news_text': news_text,
               'news_img_link': news_img_link,
               'news_link': link,
               'top_comment': top_comment,
               'likes': likes,
               'dislikes': dislikes}

        cls._saver_db(obj, tag_name)

    @classmethod
    def _saver_db(cls, oj, tag_name):
        news = News.objects.update_or_create(news_tag=tag_name, post_date=oj['post_date'], defaults=oj)
        print(news)

    @classmethod
    def _get_session(cls, base_url, ocra, session, tag_name):
        news_tag = NewsTag.objects.get(tag_name=tag_name)
        str_date = datetime.date.today().strftime("%Y/%m/%d")
        cls._get_tag_requests(base_url, session, str_date, ocra, news_tag)

    @classmethod
    def get_people(cls, ocra):
        with requests.Session() as session:
            cls._get_session(cls.PEOPLE_URL, ocra, session, tag_name='people')
            cls._get_session(cls.REALT_URL, ocra, session, tag_name='realt')
            cls._get_session(cls.TETH_URL, ocra, session, tag_name='tech')
            cls._get_session(cls.AUTO_URL, ocra, session, tag_name='auto')


