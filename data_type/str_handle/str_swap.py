'''
* 문자열 알파벳 형태 변경 메서드
Java의 lowerCase(), upperCase()와 유사
1. lower(): 영문 알파벳을 모두 소문자로 변경
2. upper(): 영문 알파벳을 모두 대문자로 변경

3. swapcase(): 영문 대소문자를 각각 반대로 변경
4. capitalize(): 문장의 맨 첫글자만 대문자, 나머지는 소문자.
5. title(): 각 단어의 맨 첫글자만 대문자, 나머지는 소문자 (공백)
'''

s = 'GOOD MORning!!! my name is LEE'

print(s) # GOOD MORning!!! my name is LEE
print(s.lower()) # good morning!!! my name is lee
print(s.upper()) # GOOD MORning!!! my name is LEE
print(s.swapcase()) # good morNING!!! MY NAME IS lee
print(s.capitalize()) # Good morning!!! my name is lee
print(s.title()) # Good Morning!!! My Name Is Lee