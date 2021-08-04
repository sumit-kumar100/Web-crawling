from bs4 import BeautifulSoup as bs
import requests
url="https://www.cricbuzz.com/"
r = requests.get(url)         
soup = bs(r.content,"html.parser")    # r.content or html_doc
view = soup.prettify()
title = soup.title()          # soup.title.string   # soup.title.name   # soup.title.parent.name
href = soup.find_all('div')   # soup.find(id="link3")
for i in href :
    print(i.text )            # print(soup.get_text())