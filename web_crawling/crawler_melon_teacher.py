from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs
from bs4 import BeautifulSoup

'''
Quiz: 멜론 Top100 목록에서 1~100위 가져오기
# 순위
# 가수명
# 앨범명
# 노래 제목

파일명: 멜론일간차트순위_2024년_5월_31일_11시기준.txt
'''

d = datetime.today()

file_path = f'c:/MyWorkspace/upload/멜론일간차트순위_{d.year}년_{d.month}월_{d.day}일_{d.hour}시기준.txt'

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service=service)


with codecs.open(file_path, mode= 'a', encoding='utf-8') as f:
    
    # 페이지 이동
    driver.get('https://www.melon.com/chart/index.htm')

    t.sleep(2)

    src = driver.page_source

    soup = BeautifulSoup(src, 'html.parser')
    

    for cnt in [50, 100]:
        # 곡 정보가 있는 tr 리스트를 지목해서 얻어오기(lst50과 lst100으로 나뉘어져 있음)
        song_tr_list = soup.select(f'tr.lst{cnt}')

        for song_tr in song_tr_list:

            # 순위 찾기
            rank = song_tr.select_one('div.wrap.t_center').text.strip()

            # 가수 이름 찾기
            artist_name = song_tr.select_one('div.wrap div.ellipsis.rank02 > a').text.strip()
            
             # 앨범명 찾기
            album_name = song_tr.select_one('div.wrap div.ellipsis.rank03 > a').text.strip()

            # 노래명 찾기
            song_name = song_tr.select_one('div.wrap div.ellipsis.rank01 > span > a').text.strip()

            f.write(f'# 순위: {rank}\n')
            f.write(f'# 가수명: {artist_name}\n')
            f.write(f'# 앨범명: {album_name}\n')
            f.write(f'# 노래 제목: {song_name}\n')
            f.write('-'*50+'\n')
            
    
    print('파일 저장 완료!')

driver.close()