from requests import Session 
from bs4 import BeautifulSoup as bs
from t_links import title,val
import pandas as pd

s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
first_page = []

def cars():
    for i in range(len(title)):
        url = 'https://www.automobile.fr/voiture/{}/vhc:car,ms1:{}__,dmg:false'.format(title[i],val[i])
        empty = []

        r = s.get(url)
        soup=bs(r.content,'html.parser')
        a = soup.find_all('div','g-row js-ad-entry')
        for j in a:
            data = j.find('a','vehicle-data track-event u-block js-track-event js-track-dealer-ratings').get('href')
            empty.append('https://www.automobile.fr/'+data)
            print('https://www.automobile.fr/'+data)
        first_page.append(empty)

cars()

for j in range(len(title)):
    dict1 = {title[j]:first_page[j]}
    df = pd.DataFrame(dict1)
    f = open('lux.csv',mode='a',encoding='utf-8')
    df.to_csv(f)
