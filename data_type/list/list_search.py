'''
* 리스트의 탐색과 정렬 메서드
1. index(): 리스트에서 특정 값이 저장된 인덱스를 반환.
2. count(): 리스트 내부에 저장된 특정 요소의 개수를 반환.
3. sort(): 리스트를 오름차 정렬.
4. reverse(): 리스트 데이터를 역순으로 배치
'''

points = [99, 14, 87, 100, 55, 100, 90, 100 , 22]
perfect = points.count(100)
print(f'100점을 획득한 학생은 {perfect}명입니다.')

print(f'55점을 획득한 학생은 {points.index(55) + 1}번째 학생입니다.')

# 내장함수 len(), max(), min()
print(f'학생 수는 {len(points)}명입니다')
print(f'최고 점수는 {max(points)}점입니다')
print(f'최저 점수는 {min(points)}점입니다')

# 오름차 정렬 sort()
points = [99, 14, 87, 100, 55, 100, 90, 100 , 22]
points.sort() # sort() 메서드는 기존 리스트를 변형한다. 새로운 값을 return하지 않는다. 
print(points) # [14, 22, 55, 87, 90, 99, 100, 100, 100]

# 내림차 정렬 sort(revers=True)
points.sort(reverse=True)
print(points) # [100, 100, 100, 99, 90, 87, 55, 22, 14]

# 정렬이 아니라 단순 역순 배치
points.reverse() 


# 리스트 내의 요소 단순 존재 유무를 확인하려면 in 키워드를 사용합니다.
food_menu = ['김밥', '닭강정', '라면', '김말이']
name = input('음식명을 입력하세요: ')

if name in food_menu:
    print(f'{name} 주문이 완료되었습니다!')
else:
    print('제공하지 않는 메뉴입니다.')
