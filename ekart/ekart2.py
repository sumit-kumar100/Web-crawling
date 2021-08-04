from ekart import links
import json
from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
image = []
nme = []
pri = []
details_key = []
details_value = []
final_details = []


def image_links():
    for i in links:
        r = s.get(i)
        soup = bs (r.content,'html.parser')
        local_image = []
    
        for j in soup.find_all("div","_2_AcLJ _3_yGjX"):
            img = j.get('style').replace("background-image:url(","").replace(")","")
            print(img)
            local_image.append(img)
        image.append(local_image)
    

def name():
    for i in links:
        r = s.get(i)
        soup = bs (r.content,'html.parser')

        a = soup.find_all('span','_35KyD6')
        for k in a:
            nm = k.text
            nme.append(nm)


def price():
    for i in links:
        r = s.get(i)
        soup = bs (r.content,'html.parser')

        b = soup.find_all('div','_1vC4OE _3qQ9m1')
        for k in b:
            pr = k.text
            pri.append(pr)


def detail_key():
    for i in links:
        r = s.get(i)
        soup = bs(r.content,'html.parser')
        local_key = []

        c = soup.find_all('div','col col-3-12 _1kyh2f')
        for i in c:
            key = i.text
            local_key.append(key)
        
        details_key.append(local_key)


def detail_value():
    for i in links:
        r = s.get(i)
        soup = bs(r.content,'html.parser')
        local_value = []

        d = soup.find_all('div','col col-9-12 _1BMpvA')
        for i in d:
            value = i.text
            local_value.append(value)

        details_value.append(local_value)
        

def final_detail():
    for i in range(len(details_key)):
        x = []
        for j in range(len(details_key[i])):
            a = details_key[i][j]
            b = ':-'
            c = details_value[i][j]
            sum = a+b+c
            x.append(sum)
        final_details.append(x)

        
detail_key()
detail_value()
image_links()
name()
price()
final_detail()
print(len(image),len(nme),len(pri),len(final_details))


dict1 = {'product_links':image,'product_name':nme,'product_price':pri,'details':final_details}
df = pd.DataFrame(dict1)
f = open('main_kart.csv',mode='w',encoding='utf-8')
df.to_csv(f)