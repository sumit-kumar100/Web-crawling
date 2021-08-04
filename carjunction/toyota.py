from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import random
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
links = []
url = 'https://www.sbtjapan.com/used-cars/hyundai/'
r = s.get(url)
soup = bs(r.content,'html.parser')
data = soup.find_all('div','grid-item')
for i in data:
    link = i.find('a').get('href')
    links.append(link)
print(links)