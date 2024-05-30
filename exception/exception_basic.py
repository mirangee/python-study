'''
* 예외 처리
- 프로그램은 실행 중에 사용자와 끊임없는 상호 작용을 합니다.
(입력 | 출력, 선언 | 호출, 요청 | 응답.....)

- 프로그램의 사용자는 예측 불가의 행동을 할 수도 있으며
잘못된 사용으로 인해 에러를 유발할 수도 있습니다.

- 에러의 종류에는 심각한 에러(Serious Error)와 
덜 심각한 에러 (Mild Error)가 있습니다.

- 심각한 에러는 개발자가 해결할 수 없는 에러(천재지변, 시스템 상 문제)
등을 말합니다.
Mild Error는 문법 오류나 오타 등 해결이 가능한 에러들을 말하며
이를 예외(Exception)라고 칭합니다.

- 아무리 프로그램을 정교하게 구성해도, 예외 발생 시 프로그램의
비정상 종료를 막을 수가 없기 때문에 예외 처리 문법을 통해
프로그램의 비정상 종료를 막아야 합니다.

- 예외처리 키워드는 try와 except를 사용합니다.

- try에는 예외 발생 가능성이 있는 코드를 작성합니다.
except에는 try에서 예외가 발생했을 때 실행할 코드를 작성합니다.

- try 내부에서 예외가 발생했다면 즉시 try의 실행을 중지하고
except의 코드가 실행되면서 프로그램의 비정상 종료를 방지합니다.
'''

try:
    n1 = int(input('정수1:'))
    n2 = int(input('정수2:'))

    print(f'입력한 정수: {n1}, {n2}')

    result = n1 / n2 # n2에 0을 입력하면 error가 발생!
    print(f'{n1} / {n2} = {result}')
except:
    print('0을 입력하지 마세요~!')

print('프로그램 정상 종료!')