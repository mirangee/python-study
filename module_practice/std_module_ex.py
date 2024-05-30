# 데이터 크롤링에 유용한 모듈들
'''
* 표준 모듈 time
- time 모듈은 시간 관련 기능들을 제공합니다.
- 대표적인 함수는 time()인데, 이 함수는 현재 시간을
1970년 1월 1일 자정을 기준으로 현재까지 경과한
시간을 초단위로 표현한 유닉스 시간을 반환합니다.
(Java는 System.currentTimeMillis()로, 밀리초 단위 반환, 파이썬은 초 단위 반환)
'''

import time as t
print(t.time())

# time 함수를 이용한 프로그램 속도 측정 테스트
start = t.time()

sum = 0 
for n in range(50000):
    sum += n

end = t.time()
print(sum)
print(f'프로그램 실행 소요시간: {end - start:0.4f}초')


'''
time 모듈의 sleep() 함수는 cpu를 지정한 시간만큼
잠재워 아무것도 하지 않고 시간을 끌게 합니다.
데이터 크롤링 시 사이트에 자동 접속 후 
시간 텀을 두고 크롤링을 시작하도록 유도할 때 사용 가능합니다.
'''

print('암산 게임! 3초 후에 문제를 보여주고 맞출 시간은 3초를 주겠다.')
t.sleep(3)
print('20 + 30 + 50 + 100 = ?')
t.sleep(3)
print('3초가 지났다! 정답은 200이다!')


'''
# 표준 모듈 datetime
운영체제의 현재 시간과 날짜 정보를
파이썬 내부로 읽어오는 기능을 제공하는 모듈입니다.
'''
from datetime import datetime

# 오늘 날짜와 현재 시간 정보를 가지고 있는 객체 리턴
d = datetime.today()
print(d)
print(f'지금은 {d.year}년 {d.month}월 {d.day}일 {d.hour}시 {d.minute}분 {d.second}초입니다.')