import json
import  pandas as pd
from requests import Session
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
links = []
for i in range(20,4700,20):   #4700
    url = 'https://www.cardekho.com/api/v1/usedcar/search?=&cityId=49&connectoid=64940498-faf6-3a18-f4f1-79789209525d&sessionid=19bf6c76339ade8c525916e9e26b3b44&lang_code=en&regionId=0&searchstring=used-cars+in+new-delhi&pagefrom={}&sortby=updated_date&sortorder=asc&mink=0&maxk=200000&dealer_id=&regCityNames=&regStateNames='.format(i)
    r = s.get(url)
    tree = json.loads(r.content)
    print(tree.keys())
    for j in range(0,25):
        try:
            final_data = 'https://www.cardekho.com'+tree['data']['cars'][j]['vlink']
            links.append(final_data)
            print(final_data)
        except:
            print("not_found")



f = open('cardeko.csv',mode='w',encoding='utf-8')
df = pd.DataFrame({'delhi':links})
df.to_csv(f)