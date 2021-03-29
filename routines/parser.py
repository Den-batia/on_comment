from bs4 import BeautifulSoup as bs
import requests
import datetime
import time
from api.models import News, NewsTag


class Parser:

    PEOPLE_URL = 'https://people.onliner.by'
    REALT_URL = 'https://realt.onliner.by'
    TETH_URL = 'https://tech.onliner.by'
    AUTO_URL = 'https://auto.onliner.by'

    @classmethod
    def _get_tag_requests(cls, url, session, str_date, news_tag, tag_name):
        dom = session.get(f'{url}/{str_date}').text
        soup = bs(dom, 'html.parser')
        list_of = soup.find_all('div', class_='news-tidings__item')
        for i in list_of:
            obj = cls._get_news(i, url)
            news_id = cls._get_news_id(session, obj['news_link'])
            top_comment = cls._get_comment(session, tag_name, news_id)
            obj.update(top_comment)
            cls._saver_db(obj, news_tag)
            time.sleep(1)

    @classmethod
    def _get_comment(cls, session, tag_name, news_id):
        res = session.get(f'https://comments.api.onliner.by/news/{tag_name}.post/{news_id}/comments?limit=15').json()
        if res['pins']:
            data = res['pins']['best']['comment']
            return {'likes': data['marks']['likes'], 'dislikes': data['marks']['dislikes'], 'top_comment': data['text']}
        return {'likes': 0, 'dislikes': 0, 'top_comment': ''}

    @classmethod
    def _get_news_id(cls, session, url):
        res = session.get(url).text
        return bs(res, 'html.parser').find('span', class_='news_view_count')['news_id']

    @classmethod
    def _get_news(cls, el, url):

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

        obj = {'post_date': data_post_date,
               'news_text': news_text,
               'news_img_link': news_img_link,
               'news_link': link
               }

        return obj

    @classmethod
    def _saver_db(cls, oj, news_tag):
        news = News.objects.update_or_create(news_tag=news_tag, post_date=oj['post_date'], defaults=oj)
        print(news)

    @classmethod
    def _get_session(cls, base_url, session, tag_name):
        news_tag = NewsTag.objects.get(tag_name=tag_name)
        str_date = datetime.date.today().strftime("%Y/%m/%d")
        cls._get_tag_requests(base_url, session, str_date, news_tag, tag_name)

    @classmethod
    def get_people(cls):
        with requests.Session() as session:
            cls._get_session(cls.PEOPLE_URL, session, tag_name='people')
            cls._get_session(cls.REALT_URL, session, tag_name='realt')
            cls._get_session(cls.TETH_URL, session, tag_name='tech')
            cls._get_session(cls.AUTO_URL, session, tag_name='auto')


