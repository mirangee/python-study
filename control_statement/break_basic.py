'''
* 탈출문 (흐름 제어문) - break, continue, return

- 반복문은 조건을 만족하는 동안 계속 반복 실행하기 때문에
한 번 반복이 시작되면 반복 횟수가 끝날 때 까지
멈추지 않고 반복을 실행합니다.

- 하지만 중간에 어떠한 이유로 반복을 중지해야 한다거나
현재 반복을 건너 뛰어야 할 경우에 탈출문을 사용합니다.

* break
- break는 현재 반복문을 즉시 종료시키고 반복문을 탈출합니다.
- 일반적으로 특정 조건 하에서 반복문을 종료시키기 때문에
if문과 함께 사용합니다.
'''

for n in range(1, 11):
    if n == 7:
        break
    print(n, end=' ')

print('\n반복문 종료!')

'''
* 무한 루프
- 무한 루프는 반복 횟수를 정하지 않고 무한하게 반복문을
실행하는 구조입니다.
- 사전에 정확한 반복 횟수를 알 수 없을 때 구현합니다.
탈출문을 통해 종료할 수 있도록 설계하면 됩니다.
- 파이썬의 무한 루프는 while문으로만 작성하며
for문으로는 구현이 불가능합니다.
'''
print('# 먹고 싶은 음식을 입력하세요.')
print('입력을 중지하려면 "그만"이라고 입력하세요.')

while True:
    food = input('>')
    if food == '그만':
        break
    print('먹고싶은 음식', food)

print('프로그램 정상 종료!')


'''
* continue
- break가 반복문을 강제로 종료시켰다면, continue는
이번 반복 1회차만 건너뛰고, 다음 반복부터는 정상적으로
실행을 계속하게 하는 탈출문 입니다.
'''
for n in range(1, 21):
    if n % 3 == 0:
        continue
    print(n, end=' ')