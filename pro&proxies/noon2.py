import pandas as pd
im_lks = pd.read_csv('noon.csv')
final_links = list(im_lks['links'])
from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
product_names = []
product_price = []
for i in final_links:
    r = s.get(i)
    soup = bs(r.content,'html.parser')

    nm = soup.find_all('h1','jsx-2771165322')
    for j in nm:
        name = j.text
        print(name)
        product_names.append(name)

    pr = soup.find_all('span','jsx-4251264678 sellingPrice')
    for k in pr:
        price  = k.find('span','value')
        price2 = price.text
        print(price2)
        product_price.append(price2)

print(len(product_names))
print(len(product_price))