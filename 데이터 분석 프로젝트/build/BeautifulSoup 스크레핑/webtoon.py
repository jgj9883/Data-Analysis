import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=mon'
html_src = requests.get(url).text

soup = BeautifulSoup(html_src, 'html.parser') #html.parser를 써도 괜찮다
list1 = soup.find_all('div',class_="list_area daily_img")
list2 = list1[0].find_all('ul',class_="img_list")
list3 = list2[0].find_all("li")

for item in list3:
    link = item.dl.dt.a.attrs['href']
    name = item.dl.dt.a.string
    print(name, "----->", link)





