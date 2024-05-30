'''
* 모듈 임포트
- 모듈은 파이썬 코드를 작성해 놓은 스크립트 파일이며
모듈 안에는 변수, 함수, 클래스 등이 정의되어 있습니다.
- 파이썬에서는 주요 기능들을 표준 모듈로 구성하여
표준 라이브러리로 제공하고 있습니다.
- 표준 모듈이나 외부 모듈을 현재 모듈로 불러와서 사용할 때는
import라는 키워드를 사용합니다.
'''

import math
pi = 3.14 # 직접 선언한 pi
print(5*5*pi) # 78.5

# 모듈에서 가져온 원주율값
print(5*5*math.pi) # 78.53981633974483

# 루트 계산
print(math.sqrt(4)) # 2.0

# 팩토리얼 계산
print(math.factorial(5)) # 120

# 로그 계산
print(math.log10(2)) # 0.3010299956639812
