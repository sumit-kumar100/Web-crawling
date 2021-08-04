from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
l = []
f = open('cricbuzz2.csv',mode='w',encoding='utf-8')
url = 'https://www.cricbuzz.com/'
r = requests.get(url)
soup = bs(r.content,'html.parser')
a = soup.find_all('img')
#print(a)
for i in a:
    # print(i.get('src'))
    if(i.get('src')):
        l.append(i.get('src'))
    else:
        pass
df = pd.DataFrame({'links':l})
df.to_csv(f)

