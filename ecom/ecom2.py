import json
from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
s = Session()

s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
image = []
product_name = []
product_price = []
category = ['mousepad','phone-grips','noteebooks']
for x in category:
    for i in range(1,20):
        url='https://inkmesilly.com/product-category/{}/page/{}'.format(x,i)
        r = s.get(url)
        soup=bs(r.content,'html.parser')


        a = soup.find_all('div','image-none')
        for i in a:
            x = i.find('img').get('data-src')
            image.append(x)


        b = soup.find_all('p',"name product-title")
        for i in b:
            y = i.find('a')
            dt = y.text
            product_name.append(dt)


        c = soup.find_all('span',"price")
        for i in c :
            z = i.find('span',"woocommerce-Price-amount amount").text
            product_price.append(z)



dict1 = {'image':image,'name':product_name,'price':product_price}
f = open('ecom2.csv',mode='w',encoding='utf-8')
df = pd.DataFrame(dict1)
df.to_csv(f)