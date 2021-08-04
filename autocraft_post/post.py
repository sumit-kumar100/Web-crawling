from bs4 import BeautifulSoup as bs 
from requests import Session
import pandas as pd
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'
final_links = []
for i in range(1,50):
    data = {"per_page":"25","page":i}
    url = 'https://www.autocraftjapan.com/stock.php?body_type=Wagon&page=1'
    r = s.post(url,data=data)
    soup = bs(r.content,'html.parser')
    link = soup.find_all('a',"color-sky-blue")
    for j in link:
        f_link = j.get('href')
        final_links.append(f_link)
        print(f_link)


dict1 = {"links":final_links}
df = pd.DataFrame(dict1)
f = open('pst.csv',mode='a',encoding='utf-8')
df.to_csv(f)


    