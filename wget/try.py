from bs4 import BeautifulSoup as bs
import json
from requests import Session
s = Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
s.headers['Content-Type'] = 'text/html; charset=UTF-8'
url = 'https://www.kooding.com/getProducts?idCategory=9&idProductsListingLink=&currentWebpageKey_caller=product-browse&curpagenum=2&sortBy=&priceRange_min=&priceRange_max='
r = s.get(url,proxies={"https":"http://scraperapi.country_code=fr:a6438ab03fee3e0af7053fbbcaa5c20c@proxy-server.scraperapi.com:8001"},verify=False)
print(r.text)