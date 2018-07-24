from bs4 import BeautifulSoup
import requests

def getdata(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.select('.lister-item.mode-advanced')
    for item in items:
        name = item.select('h3')[0]
        name2 = name.select('a')[0].text
        num = item.select(".sort-num_votes-visible")[0]
        num2 = num.select('span')[1]['data-value']
        year = item.select('.lister-item-year')[0].text
        year2 = year.lstrip('(I) (').rstrip(')')
        year2 = year2.lstrip('X) (')
        year2 = year2.lstrip('VI) (')
        year3 = 2019 - int(year2)
        avg = round((int(num2) / year3),2)
        print(name2,',',num2,',',year3,',',avg)

num_total = []
url = 'https://www.imdb.com/search/title?title_type=feature&my_ratings=exclude&count=250&sort=num_votes,desc&page={}&ref_=adv_nxt'
for i in range(1,20):
    newurl = url.format(i)
    getdata(newurl)
#    num_total.extend(newnum)
#df = pandas.DataFrame(news_total)
#df.head()
