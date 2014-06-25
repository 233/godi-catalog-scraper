#! /usr/bin/env python

import json
import logging
import re

import helper

# http://data.gov.gh/agency-publications/agency-wise/catalog_type_raw_data

BASE_URI = 'http://localhost:8088'

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

def main():
    scrape()

def scrape():
    parser = Catalog(BASE_URI)
    url = parser.start_url    
    log.info('>>> Retrieving items from: %s' % url)

    items = parser.items(url)

    log.info('>>>> First item: \n%s' % json.dumps(items[0], indent=4))

    fl = open('catalog.json', 'w')
    json.dump(items, fl, indent=4)
    fl.close()


class Catalog(helper.Scraper):
    @property
    def start_url(self):
        return self.resolve('/catalog.html')

    def items(self, url):
        """Extracts list of catalog items.
        """
        html = self.get(url)
        return [self.item(tr) for tr in html.findAll('tr', attrs={'class': 'ds-list-item'})]

    def item(self, tr):
        """Extract catalog item.
        """
        td = tr.find('td', attrs={'class': 'views-field-title'})
        title = td.a['title'].strip()

        return {'title': title, 
                'description': self.clean(td.text)[len(title) - 1:].strip(), 
                'detail_url': td.a['href'], 
                'download_url': tr.find('td', attrs={'class': 'views-field-phpcode-1'}).a['href'] }

    def clean(self, text):
        """Cleanup (description) text.
        """
        return text.strip().replace('\r', '').replace('\\n', ' ').replace('\n', ' ').strip()

  
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='[gh-docs scraper | %(levelname)s] %(message)s')
    main()
