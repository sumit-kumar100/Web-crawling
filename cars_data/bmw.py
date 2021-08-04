from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
url='https://www.tc-v.com/used_car/volkswagen/all/'
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
r = s.get(url)
soup=bs(r.content,'html.parser')
a = soup.find_all('div','vehicle-item-pic-block')
first_page = []
for i in a:
    c = i.find('a').get('href')
    link = 'https://www.tc-v.com'+c
    first_page.append(link)

f = open('volkswagen.txt','w')
for j in first_page:
    f.write(j+'\n')
f.close()
    