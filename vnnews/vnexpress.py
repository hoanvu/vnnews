import requests
import pandas as pd

from bs4 import BeautifulSoup
from vnnews import const

def get_soup(url):
    """
    Accepts an URL and return its DOM
    :param url: the URL of the web page
    :return: webpage's DOM
    """
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup


# This method return a list containing all news titles and URLs for one page
def get_links_in_url(url):
    soup = get_soup(url)
    block_mid_new = soup.find('div', {'class': 'block_mid_new'})
    news_list = block_mid_new.find_all('div', {'class': 'title_news'})
    links_in_url = []
    for news in news_list:
        links_in_url.append([news.find('a').contents[0], news.find('a')['href']])

    return pd.DataFrame(links_in_url, columns=['title', 'url'])


# This method visits each news URL and return its text content
def get_article_content(url):
    soup = get_soup(url)

    # If page is an interactive page
    if '/interactive/' in url:
        # return all_urls[all_urls.url == url]['title'].tolist()[0]
        return ' '

    # If page is a video page
    elif 'video.vnexpress.net' in url:
        title = soup.find('h1', {'class': 'title_detail_video'}).contents[0]
        summary = soup.find('div', {'class': 'lead_detail_video'}).contents[0]
        return title + ' ' + summary

    # If page is a live page
    elif soup.find('div', {'class': 'text_live'}):
        contents = []
        content_blocks = soup.find_all('div', {'class': 'text_live'})
        for block in content_blocks:
            all_p_tags = block.find_all('p')
            contents.extend([p_tag.text for p_tag in all_p_tags])
        return ' '.join(contents)

    # If page is just a normal page
    else:
        content_block = soup.find('div', {'class': 'fck_detail'})
        if content_block:
            all_p_tags = content_block.find_all('p')[:-1]
            return ' '.join([p_tag.text for p_tag in all_p_tags])
        elif soup.find('div', {'id': 'article_content'}):
            article_content = soup.find('div', {'id': 'article_content'})
            all_p_tags = article_content.find_all('p')
            return ' '.join([p_tag.text for p_tag in all_p_tags])
        else:
            return ' '


# Get URL for pages in a single category.
# No of pages returned will be depended on number of news that user wants to get
def get_page_urls(base_url, quantity=25):
    news_per_page = 25
    if quantity % news_per_page == 0:
        no_of_pages = quantity / news_per_page
    else:
        no_of_pages = quantity / news_per_page + 1

    extend_url = ['page/{}.html'.format(page) for page in xrange(2, no_of_pages + 1)]
    url_list = [base_url + extend_part for extend_part in extend_url]
    url_list.insert(0, base_url)
    return url_list


# Get news for Thoi Su category
def thoisu(quantity=25):
    page_urls = get_page_urls(const.VNEXPRESS_THOISU, quantity)
    all_urls = pd.DataFrame(columns=['title', 'url'])
    for page in page_urls:
        all_urls = all_urls.append(get_links_in_url(page), ignore_index=True)

    all_urls = all_urls[:quantity]
    content = []
    for url in all_urls.url:
        print 'Crawling URL ---- {}'.format(url)
        content.append(get_article_content(url))

    all_urls['content'] = content
    all_urls['category'] = 'thoisu'
    return all_urls


# Get news for Thoi Su category and convert to csv
def thoisu_csv(quantity=25):
    data = thoisu(quantity)
    data.to_csv('./thoisu_vnexpress.csv', index=False, encoding='utf-8', escapechar='\\')


# Get news for The Thao category
def thethao(quantity=25):
    page_urls = get_page_urls(const.VNEXPRESS_THETHAO, quantity)
    all_urls = pd.DataFrame(columns=['title', 'url'])
    for page in page_urls:
        all_urls = all_urls.append(get_links_in_url(page), ignore_index=True)

    all_urls = all_urls[:quantity]
    content = []
    for url in all_urls.url:
        print 'Crawling URL ---- {}'.format(url)
        content.append(get_article_content(url))

    all_urls['content'] = content
    all_urls['category'] = 'thethao'
    return all_urls


def thethao_csv(quantity=25):
    data = thethao(quantity)
    data.to_csv('./thethao_vnexpress.csv', index=False, encoding='utf-8', escapechar='\\')


def giaitri(quantity=25):
    page_urls = get_page_urls(const.VNEXPRESS_GIAITRI, quantity)
    all_urls = pd.DataFrame(columns=['title', 'url'])
    for page in page_urls:
        all_urls = all_urls.append(get_links_in_url(page), ignore_index=True)

    all_urls = all_urls[:quantity]
    content = []
    for url in all_urls.url:
        print 'Crawling URL ---- {}'.format(url)
        content.append(get_article_content(url))

    all_urls['content'] = content
    all_urls['category'] = 'giaitri'
    return all_urls


def giaitri_csv(quantity=25):
    data = giaitri(quantity)
    data.to_csv('./giaitri_vnexpress.csv', index=False, encoding='utf-8', escapechar='\\')