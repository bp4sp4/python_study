# ifMission1.py
# if 문 실습 문제

'''
키보드로 정수 2개를 입력받아서, 두 정수가 모두 양수일때만
합, 차 , 곱, 몫(int), 나머지를 계산해서 출력하시오

입력 내용 :
    첫번째 정수 : 12 (num1 : int)
    두번째 정수 : 5 (num2 : int)
처리 내용 :
    조건 : 두 수 모두 양수이냐? ( 양수의 조건 : 값 > 0)
    양수가 맞을때만 사칙연산 계산해서 출력함
    둘 다  또는 하나만 0, 음수이면 처리할 내용이 없음
'''

def practice1():
    num1 = int(input('첫번째 정수:'))
    num2 = int(input('두번째 정수:'))
    if (num1 > 0 and num2 >0):
        sum = num1 +num2
        sub = num1 - num2
        mul = num1 * num2
        div = num1 // num2
        mod = num1 % num2

        print('{} + {}='.format(num1, num2, sum))
        print('{} - {}'.format(num1, num2, sub))
        print('{} * {}'.format(num1, num2, mul))
        print('{} // {}'.format(num1, num2, div))
        print('{} % {}'.format(num1, num2, mod))
