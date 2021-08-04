from requests import Session
from bs4 import BeautifulSoup as bs

s = Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"


final_links = []
    for i in range(1,24):
    url = 'https://www.ebuyer.com/store/Computer/cat/Laptops?page={}'.format(i)
    r = s.get(url)
    soup = bs(r.content,'html.parser')
    a = soup.find_all('div','grid-item js-listing-product')
    for j in a:
        data = j.find('a').get('href')
        final_data = 'https://www.ebuyer.com'+data
        print(data)
        final_links.append(final_data)

    f = open('data.txt','w',encoding='utf-8')
    for x in final_links:
        f.write(x+'\n')
    f.close()