# A Python package for crawling news
The package is currently maintaining APIs for crawling VNExpress. Documentation will be updated here until I find a better place.

To read more about the challenges that we need to tackle when implement code to crawl a website, [please visit my blog](http://hoanvu.github.io/2016/06/introducing-vnnews-package).

## Version logs

| Release date | Version number | Comments |
| -------------| -------------- | -------- |
| 2016 / 06 / 23 | 1.0.2 | Update APIs for Số Hóa & Xe news and update documentation | 
| 2016 / 06 / 17 | 1.0.1 | Update APIs for Tin Nóng & Tâm Sự news | 
| 2016 / 06 / 17 | 1.0.0 | First release |

## Supported Sites & Categories

- VNExpress
    - Thời Sự
    - Thể Thao
    - Giải Trí
    - Khoa Học
    - Tâm Sự
    - Số Hóa
    - Xe
    - Tin Nóng

## Usage

1. Download or clone the repository

2. Import & Use

    ```python
    from vnnews import vnexpress
    
    # Get first 20 'Thời Sự' article from VNExpress, print them out
    vnexpress.thoisu(20) 
    
    # Get first 1000 'Thể Thao' article from VNExpress, print them out
    vnexpress.thethao(1000) 
    
    # Get first 1000 'Thể Thao' article from VNExpress, and save to CSV thethao_vnexpress.csv in local directory
    vnexpress.thethao(1000, to_csv=True)     
    ```
    
## Documentation

#### - vnnews.vnexpress.get_soup(url)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Returns the DOM for a particular URL |
| *Parameters* | **url**: URL of the page to get DOM |
| *Returns* | DOM representation for the input URL |

#### - vnnews.vnexpress.get_links_in_url(url)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Returns a list containing all news titles and URLs for one page |
| *Parameters* | **url**: URL of the page to get DOM |
| *Returns* | A pandas DataFrame containing 2 columns: title & url |

#### - vnnews.vnexpress.get_article_content(url):

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Visits a news URL and return its text content |
| *Parameters* | **url**: URL of the page to get DOM |
| *Returns* | Article content |

#### - vnnews.vnexpress.get_page_urls(base_url, quantity=25)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | VNExpress display 25 news article per page. This method returns number of pages and their URL based on the quantity of articles that user wants. For example: <br> - if user wants 30 articles, first 2 page URLs will be returned <br> - if user wants 52 articles, first 3 page URLs will be returned |
| *Parameters* | **url**: URL of the page to get DOM <br> **quantity**: number of articles to get, default is 25|
| *Returns* | list of URLs based on `quantity` |

#### - vnnews.vnexpress.get_category_news(base_url, quantity, category)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Returns news for a category. Each category only need to call this method in order to get the news |
| *Parameters* | **base_url**: base URL for the category <br> **quantity**: number of articles user wants to get <br> **category**: category number, defined in const.py |
| *Returns* | a pandas DataFrame containing news: its title, URL, content and its category number |

#### - vnnews.vnexpress.thoisu(quantity=25, to_csv=False)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Thời Sự |
| *Parameters* | **quantity**: number of news article for Thời Sự to get, default is 25 <br> **to_csv**: if True, save data to file in local directory named *thoisu_vnexpress.csv*, default is False|
| *Returns* | a pandas DataFrame containing Thời Sự news defined by `quantity` |

#### - vnnews.vnexpress.thethao(quantity=25, to_csv=False)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Thể Thao |
| *Parameters* | **quantity**: number of news article for Thể Thao to get, default is 25 <br> **to_csv**: if True, save data to file in local directory named *thethao_vnexpress.csv*, default is False |
| *Returns* | a pandas DataFrame containing Thể Thao news defined by `quantity` |

#### - vnnews.vnexpress.giaitri(quantity=25, to_csv=False)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Giải Trí |
| *Parameters* | **quantity**: number of news article for Giải Trí to get, default is 25 <br> **to_csv**: if True, save data to file in local directory named *giaitri_vnexpress.csv*, default is False |
| *Returns* | a pandas DataFrame containing Giải Trí news defined by `quantity` |

#### - vnnews.vnexpress.khoahoc(quantity=25, to_csv=False)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Khoa Học |
| *Parameters* | **quantity**: number of news article for Khoa Học to get, default is 25 <br> **to_csv**: if True, save data to file in local directory named *khoahoc_vnexpress.csv*, default is False|
| *Returns* | a pandas DataFrame containing Khoa Học news defined by `quantity` |

#### - vnnews.vnexpress.tamsu(quantity=25, to_csv=False)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Tâm Sự |
| *Parameters* | **quantity**: number of news article for Tâm Sự to get, default is 25  <br> **to_csv**: if True, save data to file in local directory named *tamsu_vnexpress.csv*, default is False|
| *Returns* | a pandas DataFrame containing Tâm Sự news defined by `quantity` |

#### - vnnews.vnexpress.sohoa(quantity=25, to_csv=False)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Số Hóa |
| *Parameters* | **quantity**: number of news article for Số Hóa to get, default is 25  <br> **to_csv**: if True, save data to file in local directory named *sohoa_vnexpress.csv*, default is False|
| *Returns* | a pandas DataFrame containing Tâm Sự news defined by `quantity` |

#### - vnnews.vnexpress.xe(quantity=25, to_csv=False)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Xe |
| *Parameters* | **quantity**: number of news article for Xe to get, default is 25  <br> **to_csv**: if True, save data to file in local directory named *xe_vnexpress.csv*, default is False|
| *Returns* | a pandas DataFrame containing Xe news defined by `quantity` |

#### - vnnews.vnexpress.tinnong(quantity=25, to_csv=False)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get all Tin Nóng news |
| *Parameters* | **quantity**: number of news article for Tin Nóng to get, default is 25 <br> **to_csv**: if True, save data to file in local directory named *tinnong_vnexpress.csv*, default is False|
| *Returns* | a pandas DataFrame containing Tin Nóng news defined by `quantity` |