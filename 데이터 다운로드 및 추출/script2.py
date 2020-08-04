# 실제 지역 번호를 사용한 기상 정보를 가져오는 프로그램
import urllib.request
import urllib.parse
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId' : '108'
}

params = urllib.parse.urlencode(values)

url = API + "?" + params
print("url = ",url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)




