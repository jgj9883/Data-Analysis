# coding: UTF-8
import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=189069"
req = requests.get(url)

html= req.text
soup = BeautifulSoup(html, "html.parser")
ul = soup.find("ul", class_ = "rvw_list_area")
lis = ul.find_all("li")

count =0
for li in lis :
    count+=1
    print("[",count,"] : ",li.a.text)



