
'''
모듈 내에 존재하는 변수, 함수, 클래스 등을 직접 임포트하는 방법
'''
from math import factorial, gcd, sqrt
import statistics as st

# math.factorial()이라고 작성하지 않아도 호출 가능
print(factorial(5)) #120

# 최대공약수 구하는 함수 바로 호출
print(gcd(12, 18)) # 6


# 통계에 사용할 수 있는 statistics 모듈
li = [100, 55, 75, 50, 55]
'''
print(f'평균: {statistics.mean(li)}') # 평균: 67
print(f'분산: {statistics.variance(li)}') # 분산: 432.5
print(f'표준편차: {statistics.stdev(li)}') # 표준편차: 20.796634343085422


import하는 모듈에 별칭을 지정하여 사용하기
import statistics as st
'''
print(f'평균: {st.mean(li)}') # 평균: 67
print(f'분산: {st.variance(li)}') # 분산: 432.5
print(f'표준편차: {st.stdev(li)}') # 표준편차: 20.796634343085422


# 위 두 가지 방법을 합쳐서도 사용 가능
from math import factorial as fac
print(fac(5))