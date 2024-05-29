'''
- 서로 다른 정수가 담긴 두 개의 리스트를 비교하여
서로 겹치지 않는 정수만 담긴 새로운 리스트를 생성해 보세요.
'''
li = [1, 2, 3, 4, 5, 6, 7]
li2 = [1, 3, 8, 4, 5, 7, 101]

# 집합 연산자를 사용하지 않는 경우
li3 = [] # 새로운 집합을 넣을 리스트

for n in li:
    if n not in li2:
        li3.append(n)

for n in li2:
    if n not in li:
        li3.append(n)

print(li3)

# 집합 연산자를 사용하는 경우
li3 = list(set(li) ^ set(li2))
li3.sort()
print(li3)