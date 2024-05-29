'''
인수의 기본값

파이썬에서는 인수의 기본값을 설정하여,
자주 바뀌지 않는 매개값은 기본값으로 처리할 수 있게 합니다. 
'''

def calc_stepsum(begin, end, step=1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

# 함수를 정의할 때 기본값을 1로 설정해 놨기에 인수를 넣지 않아도 자동으로 1 적용
print(calc_stepsum(1, 10)) 
# 기본 정의되었다 하더라도 인수값을 넣으면 그것이 우선 적용 됨
print(calc_stepsum(1, 10, 2)) 


# 기본값을 설정했다고 해서 하나의 매개값만 전달하면 에러가 납니다.
# 왜냐면 하나의 값은 첫번째 매개값으로 인식되어 begin 값으로 적용되기 때문입니다.
'''
def calc_sum(begin=0, end, step=1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

print(calc_sum(100))
'''

# 해결 방법: 기본값이 지정된 매개변수를 오른쪽으로 몰아서 작성합니다.
def calc_sum(end, begin=0, step=1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

print(calc_sum(10))