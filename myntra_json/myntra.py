import json
import wget
from requests import Session
import pandas as pd
s = Session()
url = "https://www.myntra.com/web/v2/search/mens-shirt?p=4&rows=50&o=149"
page2_url = "https://www.myntra.com/web/v2/search/myntra-fashion-store?f=Brand:U.S.%20Polo%20Assn.,U.S.%20Polo%20Assn.%20Denim%20Co.,U.S.%20Polo%20Assn.%20Kids,U.S.%20Polo%20Assn.%20Tailored,U.S.%20Polo%20Assn.%20Women::Gender:men,men%20women&p=2&rf=Discount%20Range:30.0_100.0_30.0%20TO%20100.0&rows=50&o=49"
page3_url = "https://www.myntra.com/web/v2/search/myntra-fashion-store?f=Brand:U.S.__ Polo Assn.,U.S. Polo Assn. Denim Co.,U.S. Polo Assn. Kids,U.S. Polo Assn. Tailored,U.S. Polo Assn. ___Women::Gender:men,men women&p=3&rf=Discount Range:30.0_100.0_30.0 TO 100.0&rows=50&o=99"
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
r = s.get(page2_url)
#print(r.content)
tree = json.loads(r.text)
#print(tree.keys())
#print(tree["products"][0]["productName"])
#tree["products"][0].keys()
#tree["products"][0]["productName"]
image = []
name = []
price = []
for i in range(0,50):
    images = tree['products'][i]['searchImage']
    image.append(images)
    names = tree['products'][i]['productName']
    name.append(names)
    price = tree['products'][i]['price']
    dict1 = {"product_name":name,"product_price":price,"product_url":image}


#df = pd.DataFrame(dict1)
#print(df)
#for i in image:
#   wget.download(i)



dict1 = {'products':[{'name':"sumit"},3,4,5,6]}
#print(type(dict1['products'][0]['name'])

