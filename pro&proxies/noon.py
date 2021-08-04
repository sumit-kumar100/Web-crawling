from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import random
s = Session()
links=[]
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
for i in range(1,40):
    time.sleep(random.randint(1,5))
    url='https://www.noon.com/uae-en/fashion/sneakers-40-80-off?page={}'.format(i)
    r = s.get(url)
    time.sleep(random.randint(1,10))
    soup = bs(r.content,'html.parser')
    data = soup.find_all('a','jsx-564649128 product')
    for i in data:
        href = i.get('href')
        final_link = "https://www.noon.com"+href
        print(final_link)
        links.append(final_link)



dict1 = {'links':links}
f = open('noon.csv',mode='a',encoding='utf-8')
df = pd.DataFrame(dict1)
df.to_csv(f)