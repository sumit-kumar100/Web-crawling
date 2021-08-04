from toyota import links
from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import random
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"


links2 = []
for link in links:
    f_link = link.replace('#listbox','')
    links2.append(f_link)
print(links2)


names = []
def name():
    url = 'https://www.sbtjapan.com/used-cars/hyundai/'
    r = s.get(url)
    soup = bs(r.content,'html.parser')
    data = soup.find_all('div','grid-item')
    for i in data:
        name  = i.find('a').find('b').text
        names.append(name)
name()
print(names)

final_links = []
for i in links2:
    start = 1
    local_links = []
    while True:
        url = i+"?p_num={}#listbox".format(start)
        r = s.get(url)
        soup = bs(r.content,'html.parser')
        datas = soup.find_all('div','caritem_titlearea')
        print(start)
        print(url)
        if datas:
            for x in datas:
                final_datas = x.find('h2').find('a').get('href')
                local_links.append(final_datas)
                print(final_datas)
        else:
            break
        start+=1
    final_links.append(local_links)


for csv in range(len(final_links)):
    dict1 = {names[csv] : final_links[csv]}
    df = pd.DataFrame(dict1)
    f = open('hyundai.csv',mode='a',encoding='utf-8')
    df.to_csv(f)

