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

- Usage: Get the DOM for a particular URL
- Parameters: 
    - **url**: URL of the page to get DOM
- Returns: DOM representation for the input URL

| Parameters |                            |
| ---------- | ---------------------------|
| **url** |  URL of the page to get DOM |

| Returns | DOM representation for the input URL |