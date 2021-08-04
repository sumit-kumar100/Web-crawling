from requests import Session 
from bs4 import BeautifulSoup as bs
s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"


start = 1
while True:
    url='https://www.fnac.com/SearchResult/ResultList.aspx?PageIndex={}&Search=laptop&sft=1&sl'.format(start)
    r = s.get(url,proxies={"https":"http://scraperapi.country_code=fr:a6438ab03fee3e0af7053fbbcaa5c20c@proxy-server.scraperapi.com:8001"},verify=False)
    soup=bs(r.content,'html.parser')
    try:
        data = soup.find_all('a','Article-title')
        print(data)
        print(url)
    except:
        print("this time not found")
    start+=1


# print(soup)
# '''for i in a:
#     b = i.find('font')
#     c = b.text
#     print(a)'''