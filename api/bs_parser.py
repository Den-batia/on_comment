from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Pa:
    def get_list_el(self, html_text):
        soup = bs(html_text, 'html.parser')
        list_of = soup.find_all('div', class_='news-tidings__item')
        return list_of

    def get_news(self, el, url):

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
        options = Options()
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        browser.get(link)
        html = browser.page_source

        soup = bs(html, 'html.parser')
        browser.quit()
        top_comment = soup.find('div', class_='news-comment__speech news-comment__speech_base').p.text

        # print({'post_date': data_post_date,
        #        'news_text': news_text,
        #        'news_img_link': news_img_link,
        #        'news_link': link,
        #        'top_comment': top_comment})
        print(link)

pa = Pa()