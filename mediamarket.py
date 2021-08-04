import json
from requests import Session
s = Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
s.headers['Accept'] = '*/*'
s.headers['Accept-Encoding'] = 'gzip, deflate, br'
s.headers['Accept-Language'] = 'en-US,en;q=0.5' 
s.headers['apollographql-client-name'] = 'pwa-client'
s.headers['apollographql-client-version'] = '6.101.0' 
s.headers['x-cacheable'] = 'true'
s.headers['x-flow-id'] = '516a1d44-bb56-4033-89d1-7997e900d650'
s.headers['X-MMS-Country'] = 'DE'
s.headers['X-MMS-Language'] = 'de'
s.headers['X-MMS-Salesline'] = 'Media'
s.headers['x-operation'] = 'GetAccessories'
s.headers['content-type'] = 'application/json'
url = 'https://www.mediamarkt.de/api/v1/graphql?operationName=GetSelectProducts&variables={%22ids%22:[%222652193%22,%222647872%22]}&extensions={%22pwa%22:{%22salesLine%22:%22Media%22,%22country%22:%22DE%22,%22language%22:%22de%22},%22persistedQuery%22:{%22version%22:1,%22sha256Hash%22:%221428b6101a8396ca1edcab27852bfa7262b01f451edf91d005b249368a061494%22}}'
r = s.get(url)#,proxies={"https":"http://scraperapi.country_code=de:a6438ab03fee3e0af7053fbbcaa5c20c@proxy-server.scraperapi.com:8001"},verify=False)
print(r.content)
#tree = json.loads(r.content)
print(r.status_code)

