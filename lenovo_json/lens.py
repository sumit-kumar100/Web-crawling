from requests import Session 
import json
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
s.headers["Content-Type"]="application/json;charset=utf-8"

a = []
for i in range(1,7):
    url = 'https://www.lenovo.com/ch/en/search/facet/query/v3?categories=LAPTOPS&page={}&pageSize=20&sort=sortBy&currency=CHF'.format(i)
    r = s.get(url)
    print(r)
    tree = json.loads(r.content)
    for i in tree['results']:
        print(i['url'])
