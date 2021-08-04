from requests import Session 
from bs4 import BeautifulSoup as bs
from t_links import title,val
import pandas as pd

s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"

rest_page_20 = []

for i in range(len(title)):
    start = 1
    empty = []    
    while True:
        url = 'https://www.automobile.fr/voiture/{}/vhc:car,pgn:{},pgs:20,ms1:{}__,dmg:false'.format(title[i],start,val[i])
        r = s.get(url)
        soup=bs(r.content,'html.parser')
        a = soup.find_all('div','g-row js-ad-entry')
        if a:
            for j in a:
                data = j.find('a','vehicle-data track-event u-block js-track-event js-track-dealer-ratings').get('href')
                empty.append('https://www.automobile.fr/'+data)
                print('https://www.automobile.fr/'+data)
        else:
            break
        start+=1
        
    rest_page_20.append(empty)

for j in range(len(title)):
    dict1 = {title[j]: rest_page_20[0]}
    df = pd.DataFrame(dict1)
    f = open('lux20.csv',mode='a',encoding='utf-8')
    df.to_csv(f)