'''
* 문자열 대체 메서드 replace()
- 특정 단어를 모두 찾아서 새로운 단어로 일괄 교체하는 메서드
'''
s1 = '파이썬 프로그래밍!!! 파이썬은 문자열을 관리하는 \
수많은 메서드들을 제공합니다!!! 파이썬 짱짱!!!'

print(s1.replace('파이썬', 'python'))
print(s1.replace('!', ''))

s2 = '아침부터 커피를 마셨는데, 점심먹고 커피를 또 마셨어 \
그런데 저녁에 커피를 또 주면 오늘 커피를 몇 잔 마신거지?'

# 파이썬은 replace 갯수를 지정할 있습니다. 
# 다음 예시는 앞에 나오는 2개만 replace하는 결과를 반환합니다.
print(s2.replace('커피', '소주', 2)) 