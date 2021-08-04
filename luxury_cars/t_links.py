import json
from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"


title = []

val =[]

for i in range(5):
    url = 'https://www.automobile.fr/'
    r = s.get(url)
    soup=bs(r.content,'html.parser')
    a = soup.find('select','form-control form-control--dropdown js-make-dropdown js-track-event')
    for i in a:
        titles  = i.text
        vals = i.get('value')
        title.append(titles)
        val.append(vals)

del title[7]
del val[7]
del title[130]
del val[130]
del title[253]
del val[253]
del title[376]
del val[376]
del title[499]
del val[499]

del title[0]
del val[0]


del title[122:]
del val[122:]


print(title)
print(val)
