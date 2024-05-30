# 셀레늄: 웹 자동화 및 웹의 소스코드를 수집하는 모듈
# cmd -> pip install selenium (셀레늄 라이브러리 다운로드)

# 2021년 글 보면 크롬 드라이버 다운받으라고 하는데
# 요즘에는 세레늄이 자동으로 드라이버 사용하기 때문에 그럴 필요가 없다.
# 웹 드라이버 매니저 설치
# cmd -> pip install webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# XPath 등을 통해 요소를 지목하기 위한 클래스
from selenium.webdriver.common.by import By
import time as t

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options= option, service=service) # driver를 통해 브라우저를 제어할 것임

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')

t.sleep(1.5) # 로딩 될 때까지 시간 끌기

# 자동으로 버튼이나 링크 클릭 제어하기
'''
XPath -> XML Path Language
문서의 특정 요소나 속성에 접근하기 위한 경로로 사용되는 언어
요소를 중복 없이 정확하게 표현하기 쉬운 언어
개발자 모드에서 커서로 지목한 후 우클릭 -> copy -> copy XPath
XPath를 이용해 요소를 지목하려면 By 모듈 import 필요
'''
login_btn = driver.find_element(By.XPATH, '//*[@id="account"]/div/a')
login_btn.click()

t.sleep(1)

# 자동으로 텍스트 입력하기
# 아이디 입력
id_input = driver.find_element(By.XPATH, '//*[@id="id"]')
id_input.send_keys('pmrang18') # send_keys() 메서드: 해당 요소에 입력하게 하는 메서드

t.sleep(1)

# 비밀번호 입력
driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys('aaa1111!')

t.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
