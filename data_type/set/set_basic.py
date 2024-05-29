'''
* 집합 (set)
- 집합은 여러 값들의 모임이며, 인덱스가 없기 때문에 저장 순서가 보장되지 않고
 중복값의 저장을 허용하지 않습니다. (Java의 set과 유사)

- 저장 순서가 보장되지 않기 때문에 순서가 중요하지 않은 데이터 저장용으로 사용합니다.
- 집합은 사전과 마찬가지로 {}로 표현하지만, key:value
쌍이 아닌, 데이터가 하나씩 들어간다는 점이 사전과는 다릅니다.
- set()함수는 공집합을 만들기도 하며, 다른 컬렉션 자료형을
집합 형태로 변환할 수도 있습니다.
# 빈 자료형 만들기 
[]-list(), {}-dict(), set(), tuple() -> set()과 tuple()은 괄호로 빈 자료형 만들기 없음
'''

# 중괄호를 사용하지만 key: value 형태가 아니기 때문에 set이다.
names = {'홍길동', '김철수', '박영희', '고길동', '홍길동'}
print(type(names)) # <class 'set'>
print(names) # {'홍길동', '고길동', '김철수', '박영희'}
# 중복값을 허용하지 않고 저장 순서를 보장하지 않는다.

for x in names:
    if x == '김철수':
        print(x)
        break
    
# 내장함수 set()
s = set()
print(type(s)) # <class 'set'>
print(s) # set()

s1 = 'programming'
print(set(s1)) # {'a', 'm', 'g', 'n', 'p', 'i', 'r', 'o'}
print(list(s1)) # ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
print(tuple(s1)) # ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g')

# list나 tuple은 순서를 보장하지만 
# set은 순서 보장이 안 되고 중복을 허용하지 않는다.

'''
집합(set)은 변경이 가능한 자료형이어서
언제든지 데이터를 편집할 수 있습니다.

집합에 요소를 추가할 때는 add() 메서드를 사용하고
제거할 때는 remove()를 사용합니다.
'''

asia = {'korea', 'china', 'japan'}
print(asia) # {'japan', 'china', 'korea'}

asia.add('thailand')
asia.add('china')
asia.remove('japan')
print(asia) # {'thailand', 'china', 'korea'}

# 집합의 결합
'''
집합의 결합은 list, tuple과 달리 덧셈 연산 사용이 불가합니다.
print(asia + asia2)
집합은 결합 연산이 따로 있습니다. update() 메서드를 사용합니다.
'''
asia2 = {'singapore', 'indonesia', 'korea'}
asia.update(asia2)
print(asia) # {'korea', 'singapore', 'indonesia', 'thailand', 'china'}
# korea는 중복이기 때문에 하나만 적용