import json
from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
url='https://inkmesilly.com/printed-phone-cases/'
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
r = s.get(url)
soup=bs(r.content,'html.parser')


a = soup.find_all('div','img-inner dark')
image = []
for i in a:
    x = i.find('img').get('data-src')
    image.append(x)


b = soup.find_all('option')
data = []
for i in b:
    dt = i.text
    data.append(dt)



