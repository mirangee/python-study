'''
* 식별자 (identifier)
1. 사용자 정의로 데이터에 이름을 붙인 것.
2. 모듈, 패키지, 변수, 함수, 클래스 등의 이름을 식별자라고 합니다.
3. 식별자 이름은 중복해서 지정할 수 없습니다.
'''

# 식별자 이름을 숫자로 지정하거나 숫자로 시작하면 안 된다.
# 7 = 777 (X)
# 7num = 777 (X)
number = 7
num7ber = 7

# 식별자 이름에 공백 포함 안 된다.
# my birth day = 19921013 (X)
my_birth_day = 19921013 # 파이썬은 snake case를 주로 사용

# 키워드를 식별자로 사용할 수 없습니다. (if, while, for)
# if = '만약에' (X)
If = '만약에' # 별로...

# print()와 같은 내장 함수의 이름을 식별자로 사용할 수는 있지만
# 더 이상 함수의 기능을 사용할 수 없다. -> 사용하지 말란 뜻
# print = '출력하다'
# print(print)

# 한글, 한자 등 영어 이외의 문자도 식별자로 가능하지만
# 사용을 권장하지는 않습니다.
야옹이 = '고양이' # 별로...