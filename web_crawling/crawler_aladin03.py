from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs

# 뷰티풀스프 임포트
from bs4 import BeautifulSoup

d = datetime.today()

file_path = f'c:/MyWorkspace/upload/알라딘 베스트셀러 1~50위_{d.year}{d.month}{d.day}.txt'

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options= option, service=service) # driver를 통해 브라우저를 제어할 것임

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.aladin.co.kr')

t.sleep(2)

driver.find_element(By.XPATH, '//*[@id="Wa_header1_headerTop"]/div[2]/div[3]/ul[1]/li[3]/a').click()

t.sleep(2)

'''
with 문을 사용하면 with 블록을 벗어나는 순간 객체가 자동으로 해제됩니다.
(자바의 try-with-resources와 유사)
finally에 close를 할 필요가 없습니다.
with를 쓰고 한칸 들여쓰면 됩니다.
with 작성 시 사용할 객체의 이름을 as 뒤에 작성해 줍니다.
이는 f= open(file_path, 'w')와 동일한 의미입니다.
'''
'''
    * 표준 모듈 codecs
    - 웹이나 다른 프로그램의 텍스트 데이터와
    파이썬 내부의 텍스트 데이터의 인코딩 방식이 서로 다를 경우에
    내장함수 open()이 제대로 인코딩을 적용할 수 없어서
    에러가 발생합니다. (UnicodeEncodeError)
    - 파일 입/출력 시 인코딩 코덱을 변경하고 싶다면
    codecs 모듈을 사용합니다. codecs 모듈은 import만 하면 사용 가능합니다.
'''

with codecs.open(file_path, mode= 'w', encoding='utf-8') as f:

    # selenium으로 현재 페이지의 html 소스 코드 전부 불러오기 (이것이 selenium의 마지막 임무)
    src = driver.page_source

    soup = BeautifulSoup(src, 'html.parser')

    div_list = soup.find_all('div', class_='ss_book_box')

    # 반복문을 돌려서 50권의 책에 대한 정보를 다 가져오기

    rank = 1

    for div in div_list:
        book_info =div.find_all('li')

        if book_info[0].find('span', class_= 'ss_ht1') == None:
            # 첫번째 li에 span class="ss_ht1"이 없다면 사은품이 없는 책
            book_title = book_info[0].text 
            book_author = book_info[1].text
            book_price = book_info[2].text

            auth_info = book_author.split('|')
        else:
            # 사은품이 있는 책
            book_title = book_info[1].text # 두 번째 li를 지목하기 위해 1번 인덱스로 지목
            book_author = book_info[2].text
            book_price = book_info[3].text

            auth_info = book_author.split('|')
        
        f.write(f'# 순위: {rank}위\n')
        f.write(f'# 제목: {book_title}\n')
        f.write(f'# 지은이: {auth_info[0]}\n')
        f.write(f'# 출판사: {auth_info[1]}\n')
        f.write(f'# 출판연월: {auth_info[2]}\n')
        f.write(f'# 가격: {book_price.split(", ")[0]}\n')
        f.write('-'*40 + '\n')

        rank += 1
