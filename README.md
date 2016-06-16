# A Python package for crawling news
The package is currently maintaining APIs for crawling VNExpress. Documentation will be updated here until I find a better place.

## Usage

1. Download or clone the repository

2. Import & Use

```
from vnnews import vnexpress
vnexpress.thoisu(20) # Get first 20 'Thời Sự' article from VNExpress
vnexpress.thethao(1000) # Get first 1000 'Thể Thao' article from VNExpress
```