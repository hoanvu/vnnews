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
| *Usage* | VNExpress display 25 news article per page. This method returns number of pages and their URL based on the quantity of articles that user wants <br> For example: <br> - if user wants 30 articles, first 2 page URLs will be returned <br> - if user wants 52 articles, first 3 page URLs will be returned |
| *Parameters* | **url**: URL of the page to get DOM <br> **quantity**: number of articles to get, default is 25|
| *Returns* | list of URLs based on `quantity` |

#### get_category_news(base_url, quantity, category)


#### thoisu(quantity=25)


#### thoisu_csv(quantity=25)


#### thethao(quantity=25)


#### thethao_csv(quantity=25)


#### giaitri(quantity=25)


#### giaitri_csv(quantity=25)


#### khoahoc(quantity=25)


#### khoahoc_csv(quantity=25)