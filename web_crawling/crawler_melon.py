from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs
from bs4 import BeautifulSoup

d = datetime.today()

file_path = f'c:/MyWorkspace/upload/멜론일간차트순위_{d.year}년_{d.month}월_{d.day}일_{d.hour}시기준.txt'

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service=service)

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.melon.com/chart/index.htm')

t.sleep(2)

src = driver.page_source

soup = BeautifulSoup(src, 'html.parser')


'''
Quiz: 멜론 Top100 목록에서 1~100위 가져오기
# 순위
# 가수명
# 앨범명
# 노래 제목

파일명: 멜론일간차트순위_2024년_5월_31일_11시기준.txt
'''

with codecs.open(file_path, mode= 'a', encoding='utf-8') as f:
    
    rank = 1 # 순위    

    # 코드를 보면 1~50위는 tr 클래스명이 lst50, 51~100위는 lst100이다.
    # 두 경우의 수로 나누어 처리하자.
    for n in [50,  100]:  
        tr_song_list = soup.select(f'tr.lst{n}')

        for tr_song in tr_song_list:
                song_info = tr_song.select('div.ellipsis a')

                title = song_info[0].text
                singer = song_info[1].text
                album = song_info[3].text

                f.write(f'# 순위: {rank}위\n')
                f.write(f'# 가수명: {singer}\n')
                f.write(f'# 앨범명: {album}\n')
                f.write(f'# 노래 제목: {title}\n')
                f.write('-'*50+'\n')
                

                rank += 1
    
print('파일 저장 완료!')