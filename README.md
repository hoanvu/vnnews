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

1. vnnews.vnexpress.get_soup(url)

    | Meta | Explanation |
    | :---- | :----------- |
    | *Usage* | Returns the DOM for a particular URL |
    | *Parameters* | **url**: URL of the page to get DOM |
    | *Returns* | DOM representation for the input URL |

2. vnnews.vnexpress.get_links_in_url(url)

    | Meta | Explanation |
    | :---- | :----------- |
    | *Usage* | Returns a list containing all news titles and URLs for one page |
    | *Parameters* | **url**: URL of the page to get DOM |
    | *Returns* | a pandas DataFrame containing 2 columns: title & url |

#### vnnews.vnexpress.get_article_content(url):

| Meta | Explanation |
| :---- | :----------- |
| *Usage* | Visits a news URL and return its text content |
| *Parameters* | **url**: URL of the page to get DOM |
| *Returns* | article content |