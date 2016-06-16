# A Python package for crawling news
The package is currently maintaining APIs for crawling VNExpress. Documentation will be updated here until I find a better place.

## Usage

1. Download or clone the repository

2. Import & Use

    ```python
    from vnnews import vnexpress
    
    # Get first 20 'Thời Sự' article from VNExpress
    vnexpress.thoisu(20) 
    
    # Get first 1000 'Thể Thao' article from VNExpress
    vnexpress.thethao(1000) 
    ```
    
## Documentation

#### vnnews.vnexpress.get_soup(url)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Returns the DOM for a particular URL |
| *Parameters* | **url**: URL of the page to get DOM |
| *Returns* | DOM representation for the input URL |

#### vnnews.vnexpress.get_links_in_url(url)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Returns a list containing all news titles and URLs for one page |
| *Parameters* | **url**: URL of the page to get DOM |
| *Returns* | A pandas DataFrame containing 2 columns: title & url |

#### vnnews.vnexpress.get_article_content(url):

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Visits a news URL and return its text content |
| *Parameters* | **url**: URL of the page to get DOM |
| *Returns* | Article content |

#### get_page_urls(base_url, quantity=25)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | VNExpress display 25 news article per page. This method returns number of pages and their URL based on the quantity of articles that user wants. For example: <br> - if user wants 30 articles, first 2 page URLs will be returned <br> - if user wants 52 articles, first 3 page URLs will be returned |
| *Parameters* | **url**: URL of the page to get DOM <br> **quantity**: number of articles to get, default is 25|
| *Returns* | list of URLs based on `quantity` |

#### get_category_news(base_url, quantity, category)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Returns news for a category. Each category only need to call this method in order to get the news |
| *Parameters* | **base_url**: base URL for the category <br> **quantity**: number of articles user wants to get <br> **category**: category number, defined in const.py |
| *Returns* | a pandas DataFrame containing news: its title, URL, content and its category number |

#### thoisu(quantity=25)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Thời Sự |
| *Parameters* | **quantity**: number of news article for Thời Sự to return |
| *Returns* | a pandas DataFrame containing Thời Sự news defined by `quantity` |

#### thoisu_csv(quantity=25)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Thời Sự and save to CSV file |
| *Parameters* | **quantity**: number of news article for Thời Sự to return |
| *Returns* | None |

#### thethao(quantity=25)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Thể Thao |
| *Parameters* | **quantity**: number of news article for Thể Thao to return |
| *Returns* | a pandas DataFrame containing Thời Sự news defined by `quantity` |

#### thethao_csv(quantity=25)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Thể Thao and save to CSV file |
| *Parameters* | **quantity**: number of news article for Thể Thao to return |
| *Returns* | None |

#### giaitri(quantity=25)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Giải Trí |
| *Parameters* | **quantity**: number of news article for Giải Trí to return |
| *Returns* | a pandas DataFrame containing Thời Sự news defined by `quantity` |

#### giaitri_csv(quantity=25)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Giải Trí and save to CSV file |
| *Parameters* | **quantity**: number of news article for Giải Trí to return |
| *Returns* | None |

#### khoahoc(quantity=25)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Khoa Học |
| *Parameters* | **quantity**: number of news article for Khoa Học to return |
| *Returns* | a pandas DataFrame containing Thời Sự news defined by `quantity` |

#### khoahoc_csv(quantity=25)

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Get news for Khoa Học and save to CSV file |
| *Parameters* | **quantity**: number of news article for Khoa Học to return |
| *Returns* | None |