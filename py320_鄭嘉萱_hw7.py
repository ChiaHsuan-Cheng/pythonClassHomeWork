import requests
from bs4 import BeautifulSoup
req = requests.get('https://movies.yahoo.com.tw/movieinfo_main/%E9%87%91%E7%BF%85%E9%9B%80-the-goldfinch-10072')
html = req.content.decode('utf8')
soup = BeautifulSoup(html, 'lxml')
print(soup.select('h1')[0].string)
print(soup.select('h3')[0].string)
for i in soup.select(".movie_intro_info_r > span"):
    print(i.text)
    if(i.text == "導演："):
        print(soup.select(".movie_intro_list")[0].string)
for i in soup.select(".movie_intro_list > a"):
    print(i.text)
