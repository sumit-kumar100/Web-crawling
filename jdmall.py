from requests import Session
import json
s = Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=28694162119&score=0&sortType=6&page=2&pageSize=10&isShadowSku=0&rid=0&fold=1'
r = s.get(url)
tree = json.loads(r.content)
print(tree)