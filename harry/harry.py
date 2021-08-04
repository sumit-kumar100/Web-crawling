'''from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
#import wget
l = []
url = 'https://wallpapercave.com/harry-potter-hd-wallpapers'
r = requests.get(url)
soup = bs(r.content,'html.parser')
a = soup.findAll('a','wpimg')
for i in a:
    img = i.find('img')
    if(img.get('src')):
        l.append("https://wallpapercave.com/"+img.get('src'))
    else:
        pass
#for j  in l:
#   wget.download(j)

# writing to a file
f = open('harry.txt','w')
for i in l:
    f.write(i+'\n')
f.close()
'''
#reading from a file
fr = open('harry.txt','r')
l = fr.readlines()
for i in l:
    print(i)
fr.close()

