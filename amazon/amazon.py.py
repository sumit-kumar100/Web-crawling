import json
from requests import Session 
from bs4 import BeautifulSoup as bs
import pandas as pd
url='https://www.amazon.in/s?k=cars+assessories&crid=3BO26GKY1CW3P&sprefix=cars+asses%2Caps%2C364&ref=nb_sb_ss_ts-oa-p_1_10'
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
r = s.get(url)
soup=bs(r.content,'html.parser')
#print(soup)
image = []
name = []
price = []
a = soup.find_all('div','a-section a-spacing-medium')
for i in a:
    image.append(i.find('img','s-image').get('src'))



b = soup.find_all('span','a-size-base-plus a-color-base a-text-normal')
for j in b:
    dt = j.text
    name.append(dt)

c = soup.find_all('span','a-price-whole')
for k in c:
    y = k.text
    price.append(y)
print(name)
print(image)
print(price)
print(len(name))
print(len(image))
print(len(price))


dict1 = {'product_links':image,'product_name':name,'product_price':price}
df = pd.DataFrame(dict1)
f = open('amazon_links.csv','w')
df.to_csv(f)