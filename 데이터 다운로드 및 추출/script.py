
# 웹상의 정보를 추출하는 방법


import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

urllib.request.urlretrieve(url,savename)
print("저장되었습니다....!")

