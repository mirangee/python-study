'''
* 내장함수 map()
- map()은 첫번째 인수로 함수를 지정하고, 두 번째 인수로
리스트를 지정하면 해당 리스트 내부 요소값을 일괄적으로
첫번째 인수로 지정한 함수에 인수로 전달합니다.
'''

def triple_square(number):
    return number**3 # 제곱은 **로 표현

li = [2, 4, 6, 8, 10]

result = list(map(triple_square, li)) 
# map()의 리턴값으론 map 객체가 오기 때문에 list로 변환한다.

print(result) # [8, 64, 216, 512, 1000]


# 3개의 숫자 중 최대값을 판별하여 리턴하는 함수를 정의
def max_of_three(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
              return n1
        else:
              return n3
    else:
        if n2 > n3:
              return n2
        else: 
              return n3
        
'''
n1 = int(input('정수1:'))
n2 = int(input('정수2:'))
n3 = int(input('정수3:'))
'''
# map을 이용해 일괄처리 하는 방법
n1, n2, n3 = map(int, input('정수 3개를 공백으로 구분해서 각각 입력하세요: ').split())

print(f'최대값: {max_of_three(n1, n2, n3)}')
