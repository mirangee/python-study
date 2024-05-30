'''
# 가변 인수
- 함수를 호출할 때는 함수 정의시에 지정한 인수의 개수만큼
값을 전달해야 합니다.
- 하지만 가변 인수를 사용하면 하나의 인수로 여러 개의 값을
받아서 처리할 수 있습니다.

# 위치 가변 인수
- 위치 가변 인수는 함수 정의부에서 인수를 선언할 때
인수 앞에 * 기호를 붙여 선언하며, 이런 경우에 여러 개의 
데이터를 튜플로 묶어서 함수 내부로 전달합니다.
'''

def calc_total(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(calc_total(1,2,3,4,5,6,7,8,9,10)) # 55
print(calc_total(110,414,13,34,25,76)) # 672

'''
단, 위치 가변 인수와 일반 인수를 동시에 사용할 때는
일반 인수를 반드시 키워드 인수 방식으로 전달해야 합니다.
가변 인수는 크기가 변하는 변수이기 때문에 
키워드를 지정해 주지 않으면 그 인수를 가변 인수에 포함해야 하는지,
별개의 인수로 받아야 하는지 판단할 수 없기 때문입니다.
'''

def calc_points(*points, name):
    print(f'{name}님의 성적을 계산합니다...')

    total = 0
    for n in points:
        total += n
    return total / len(points)

# result = calc_points(90, 80, 100, '박미랑') error 발생!
result = calc_points(90, 80, 100, name='박미랑')
print(f'평균 점수: {result}')



'''
# 키워드 가변 인수
함수가 여러개의 키워드 인수를 받을 수 있게 해주는 기능입니다.
키워드 가변 인수는 선언 시에 인수 앞에 * 기호를 2개 붙여 선언합니다.
이를 선언해서 여러 값을 받으면 함수 내부로 사전(dict)이
전달됩니다. 
'''

def print_info(**kwargs):
    print(type(kwargs)) # <class 'dict'>
    for k in kwargs:
        print(f'{k}:{kwargs[k]}')

print_info(name='김철수', age=30, city='서울')