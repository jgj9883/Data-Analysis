# coding: UTF-8
import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/point.nhn?code=185917#tab"
req = requests.get(url)

html= req.text
soup = BeautifulSoup(html, "html.parser")

for item,i in zip(soup.select(".score_result .score_reple"),range(1,6)):
    result = item.text
    result = result.replace('\t',"")
    result = result.replace('\r', "")
    result = result.replace('\n',"")
    print(result)





