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

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.melon.com/chart/index.htm')

t.sleep(2)

src = driver.page_source

soup = BeautifulSoup(src, 'html.parser')

with codecs.open(file_path, mode= 'a', encoding='utf-8') as f:
    
    rank = 1 # 순위    

    for n in range(0, 100):  
        if (rank <= 50):
            div_list = soup.select('tr.lst50')
        else: 
            div_list = soup.select('tr.lst100')
            n = n - 50
        
        # ellipsis_list= div_list[n].select('div.ellipsis')

        # title = ellipsis_list[0].find_all('a')
        # singer = ellipsis_list[1].find_all('a')
        # album = ellipsis_list[2].find_all('a')

        # f.write(f'# 순위: {rank}위\n')
        # f.write(f'# 가수명: {singer[0].text}\n')
        # f.write(f'# 앨범명: {album[0].text}\n')
        # f.write(f'# 노래 제목: {title[0].text}\n')
        # f.write('-'*50+'\n')

        ellipsis_list= div_list[n].select('div.ellipsis a')

        title = ellipsis_list[0].text
        singer = ellipsis_list[1].text
        album = ellipsis_list[3].text

        f.write(f'# 순위: {rank}위\n')
        f.write(f'# 가수명: {singer}\n')
        f.write(f'# 앨범명: {album}\n')
        f.write(f'# 노래 제목: {title}\n')
        f.write('-'*50+'\n')
        

        rank += 1
    
    print('파일 저장 완료!')