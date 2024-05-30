from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs

# 뷰티풀스프 임포트
from bs4 import BeautifulSoup

d = datetime.today()

file_path = f'c:/MyWorkspace/upload/알라딘 베스트셀러 1~400위_{d.year}{d.month}{d.day}.txt'

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

# '//*[@id="newbg_body"]/div[3]/ul/li[3]/a' 에서 마지막 대괄호 숫자가 올라가면 되겠다. 3부터 9까지 올라가면 1위부터 400위임

rank = 1
for n in range(2, 10):

    if n in range(3, 10):
        link = f'//*[@id="newbg_body"]/div[3]/ul/li[{n}]/a'
        driver.find_element(By.XPATH, link).click()        

    with codecs.open(file_path, mode= 'a', encoding='utf-8') as f:

        # selenium으로 현재 페이지의 html 소스 코드 전부 불러오기 (이것이 selenium의 마지막 임무)
        src = driver.page_source

        soup = BeautifulSoup(src, 'html.parser')

        div_list = soup.find_all('div', class_='ss_book_box')

        # 반복문을 돌려서 400권의 책에 대한 정보를 다 가져오기        
        for div in div_list:
            book_info =div.find_all('li')

            # 245위 같이 제목과 가격 정보만 있는 경우  
            if len(book_info) < 5:
                book_title = book_info[0].text 
                book_price = book_info[1].text

                f.write(f'# 순위: {rank}위\n')
                f.write(f'# 제목: {book_title}\n')
                f.write(f'# 가격: {book_price.split(", ")[0]}\n')
                f.write('-'*40 + '\n')
                

            elif book_info[0].find('span', class_= 'ss_ht1') == None:
                # 첫번째 li에 span class="ss_ht1"이 없다면 사은품이 없는 책
                book_title = book_info[0].text 
                book_author = book_info[1].text
                book_price = book_info[2].text

                auth_info = book_author.split('|')

                f.write(f'# 순위: {rank}위\n')
                f.write(f'# 제목: {book_title}\n')
                f.write(f'# 지은이: {auth_info[0]}\n')
                f.write(f'# 출판사: {auth_info[1]}\n')
                f.write(f'# 출판연월: {auth_info[2]}\n')
                f.write(f'# 가격: {book_price.split(", ")[0]}\n')
                f.write('-'*40 + '\n')

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

print('파일 저장 완료!')