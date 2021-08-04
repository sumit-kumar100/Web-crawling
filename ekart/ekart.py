from bs4 import BeautifulSoup as bs 
import pandas as pd
from requests import Session
s = Session()
s.headers["User-agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
url='https://www.flipkart.com/search?q=shoes&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=TRENDING&suggestionId=shoes&requestId=d1718a4a-d602-44b2-9edd-a3b175c558a9'
r = s.get(url)
soup = bs(r.content,'html.parser')
links = []
data = soup.find_all('a','_3dqZjq')
for i in data:
    href = i.get('href')
    final_link = "https://www.flipkart.com"+href
    links.append(final_link)


dict1 = {'links':links}
f = open('ekart.csv',mode='w',encoding='utf-8')
df = pd.DataFrame(dict1)
df.to_csv(f)