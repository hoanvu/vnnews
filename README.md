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

##### vnnews.vnexpress.get_soup(url)

| vnnews.vnexpress.get_soup(url) |
| -------------------------------|
| Usage | Returns the DOM for a particular URL |
| *Parameters* | **url**: URL of the page to get DOM |
| *Returns* | DOM representation for the input URL |

##### vnnews.vnexpress.get_links_in_url(url)

Returns a list containing all news titles and URLs for one page

- *Parameters*: 
    - **url**: URL of the page to get data
- *Returns*: a pandas DataFrame containing 2 columns: title & url

##### vnnews.vnexpress.get_article_content(url):

Visits each news URL and return its text content

- *Parameters*: 
    - **url**: URL of the article to get content
- *Returns*: article content