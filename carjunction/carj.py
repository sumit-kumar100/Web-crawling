from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import random
s = Session()
links=[]
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"

for i in range(1,300,25):
    #time.sleep(random.randint(1,5))
    url='https://www.carjunction.com/make/toyota.html?&page={}'.format(i)
    r = s.get(url)
    #time.sleep(random.randint(1,10))
    soup = bs(r.content,'html.parser')
    data = soup.find_all('a',attrs={'style':'font-size:18px;'})
    if data:
        for i in data:
            href = i.get('href')
            final_link = "https://www.carjunction.com"+href
            print(final_link)
            links.append(final_link)



dict1 = {'FORD':links}
f = open('carjuction.csv',mode='a',encoding='utf-8')
df = pd.DataFrame(dict1)
df.to_csv(f)