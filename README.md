godi-catalog-scraper
====================

Ghana Open Data Initiative (NITA) Catalog Scraper

This scraper collects the description and download links for documents (XLS sheets)
provided on the GODI portal.

I created this so I could easily download, categorize and analyze data provided on 
the GODI portal.


Steps
-----

1. Download the resource at http://data.gov.gh/catalogs/?filter=catalog_type%3Acatalog_type_raw_data%2Bfile%3Aapplication/vnd.ms-excel&results=1000, and save to catalog.html
2. Change to folder containing catalog.html file and start python SimpleHTTPServer

python -m SimpleHTTPServer 8088

If you decide to use a different port from 8088, please update in scraper.py


3. Run scraper.py to extract data (and persist to catalog.json)

i. mkvirtualenv godi-catalog-scraper
ii. pip install -r requirements.txt
iii. python scraper.py
