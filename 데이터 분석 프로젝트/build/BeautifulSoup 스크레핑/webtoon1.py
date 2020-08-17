import os
from bs4 import BeautifulSoup
from selenium import webdriver
#import requests #request+bs4 조합만으로도 crawling가능
import time
base_url = 'https://comic.naver.com/webtoon/weekday.nhn'

#chrome_dirver가 있는 위치
os.chdir('C:/Users/jgj98/Downloads/chromedriver_win32') #크롬드라이버.exe가 있는 폴더
#driver 실행
def drive(url):
    driver = webdriver.Chrome('./chromedriver') #driver 객체 불러옴
    driver.implicitly_wait(3) # 3초 후에 작동하도록
    driver.get(url) #url에 접속
    html = driver.page_source #현재 driver에 나타난 창의 page_source(html) 가져오기
    soup = BeautifulSoup(html, 'html.parser') #html 파싱(parsing)을 위해 BeautifulSoup에 넘겨주기
    return driver, soup

#웹툰 기본 페이지에서 데이터 가져오기
driver, soup = drive(base_url)
driver.close()

#가져온 데이터 파싱, id, 요일, 이름
title = soup.select('.title')
t_IDs=list(map(lambda x: x.get('href').split('titleId=')[1].split('&')[0], title))
t_weekdays = list(map(lambda x: x.get('href').split('weekday=')[1], title))
t_names = list(map(lambda x: x.text ,title))

#크롤링이 잘 되었나 확인하기 위함, 총 웹툰 수
print('t_IDs: ',len(t_IDs))
print('t_weekdays: ',len(t_weekdays))
print('t_names: ',len(t_names))
print(t_IDs[0],t_weekdays[0], t_names[0])

def find_id_weekday(name,t_names,t_IDs,t_weekdays,start_idx = 0):
    try:
        idx = t_names.index(name)
    except:
        print('찾는 웹툰이 없습니다.')
        return
    return t_IDs[idx], t_weekdays[idx]

def episode_count(ID, weekday):
    url = base_url.split('weekday')[0] + 'list.nhn?titleId={0}&weekday={1}'.format(ID, weekday)
    # print(url)
    driver, soup = drive(url)
    driver.close()
    res = soup.select('.title')[0].select('a')[0].get('href').split('no=')[1].split('&')[0]

    return res


res = episode_count(183559, 'mon')  # 신의 탑
print(res)

def comment_crawler(name, start_idx=0):
    id_num, weekday = find_id_weekday(name, t_names, t_IDs, t_weekdays, start_idx=start_idx)
    cnt = int(episode_count(id_num, weekday))

    comments = []
    proceed = -1  # 진행 상태 표시 위함, 처음에 0보다 작아야 0%가 표시 됨

    driver, _ = drive(base_url)  # driver만 먼저 열어 놓음. for문 돌면서 url만 바꿔줄 것임
    print('진행중...')
    for i in range(1, cnt + 1):
        percentage = int((i / cnt) * 100)
        if percentage % 10 == 0 and percentage > proceed:  # 진행상황 표시
            proceed = percentage
            print(proceed, '% 완료')
        url = 'https://comic.naver.com/comment/comment.nhn?titleId={0}&no={1}#'.format(id_num, str(i))
        # driver.implicitly_wait(3)
        time.sleep(1.5)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        comments += list(map(lambda x: x.text, soup.select('.u_cbox_contents')))

    driver.close()
    print('crawling finished')
    return comments