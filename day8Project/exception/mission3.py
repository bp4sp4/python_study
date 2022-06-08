# mission3.py
# 사용자 정의 예외 발생 실습문제

'''
함수 작성 : calc score(a,b)
구현 내용 : 전달받은 두수의 합, 차, 곱,몫 ,나머지 계산 출력
단, 전달받은 두 수가 1이상 100이하의 값이 아닌 경우 예오 ㅣ발생시킴
'계산할 데이터는 반드시 1이상 100이하의 값이어야 합니다. 메시지 처리함수 사용
test mission()
두 정수를 키보드로 입력받아서 calc_score() 로 전달 실행함
trt: except : finally: 로 작성하시오
'''


def calc_score(a, b):
    if((a >=1 and a <=100) and (b >= 1 and b<= 100)):
        print(f'{a} + {b} = {a +b}')
        print(f'{a} - {b} = {a - b}')
        print(f'{a} * {b} = {a * b}')
        print(f'{a} / {b} = {a / b}')
        print(f'{a} %% {b} = {a % b}')

    else:
        raise Exception(' 계산할 데이터는 반드시 1이상 100이하이다.')
def test_mission():
    try:
        first = int(input('첫번째 정수 : '))
        second = int(input('두번째 정수 : '))

        calc_score(first,second)
    except Exception as msg:
        print(msg)
    finally:
        print('raise test종료.')


if __name__ == '__main__':
    test_mission()