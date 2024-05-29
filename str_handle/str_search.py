'''
* 문자열 관리 함수, 메서드
- 함수: 모듈 내부에서 공용적으로 사용할 수 있는 기능의 집합.(단독 호출)
        특정 타입 하나에 종속되지 않고 범용적으로 사용 가능
- 메서드: 클래스에 소속된 함수, 특정 자료형 전용 함수.
'''

# 내장 함수 len() : 순차형 자료(sequence)의 내부 데이터 갯수를 구함
# len()은 문자열에서만 쓸 수 있는 게 아닌 '함수'입니다.
s = 'python programming'

count = 0
for c in s:
    count += 1
print('s의 글자 수:', count)

# 굳이 for문 돌릴 필요 없이 함수 사용하면 바로 갯수 구해줌
print('s의 글자수:', len(s))

'''
# 문자열 메서드 find(), rfind()
- 문자열 내부에 특정 문자를 검색하여 해당 문자의
인덱스 번호를 알려줍니다.
- find()는 앞에서부터, rfind()는 뒤에서부터 탐색(r은 rear)
'''
s = 'python programming'
print(s.find('o'))
print(s.rfind('o'))

# program이라는 단어가 s라는 문자열 변수에 있다면 
# 해당 단어의 시작 인덱스를 알려줌
print(s.find('program')) 
# 해당 단어가 s라는 문자열 변수에 없다면 -1 반환됨
print(s.find('메롱'))

# 메서드 count(): 문자열 내부에 찾는 단어의 출현 횟수 반환
message = """
    내가 그린 기린 그림은 목이 긴 기린 그림이고
    니가 그린 기린 그림은 목이 안 긴 기린 그림이다.
"""
print('"기린" 단어의 출현 횟수:', message.count('기린'))

'''
  특정 문자가 있는 인덱스나 횟수는 관심 없고
  단순히 포함 여부만 확인하고 싶다면 in 키워드를 사용합니다.
  True 혹은 False를 반환합니다.
'''
s = 'python programming'
print('a' in s) # True
print('q' in s) # False
print('z' not in s) # True
print('pro' in s) # True


'''
- 문자의 형태 검사하는 메서드
1. isdecimal(): 모든 문자가 숫자 형태인지를 검사.
2. isalpha(): 모든 문자가 영문 알파벳인지를 검사.
3. islower(): 모든 문자가 영문 소문자인지를 검사.
4. isupper(): 모든 문자가 영문 대문자인지를 검사.
'''
print('15+8 = ???')

while True:
    answer = input('>> ')
    if answer.isdecimal():
        answer = int(answer)
    else:
        print('정답은 정수로만 입력하세요!')
        continue
    
    if answer == 23:
        print('정답입니다!')
        break
    else:
        print('틀렸습니다!')