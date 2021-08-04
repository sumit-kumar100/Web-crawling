from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
final_links = []
for i in range(1,51):
    url = 'https://www.noon.com/uae-en/p-20253?limit=200&page={}'.format(i)
    r = s.get(url)
    soup = bs(r.content,'html.parser')
    noon_herf = soup.find_all('a','jsx-564649128 product')
    for j in noon_herf:
        links = "https://www.noon.com"+j.get('href')
        final_links.append(links)
        print(links)

f = open('f_noon.txt','w')
for x in final_links:
    f.write(x+'\n')
f.close()
