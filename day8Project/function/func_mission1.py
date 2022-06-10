# func_mission1.py
# 함수 만들고 사용하기 실습문제1

'''
파이썬으로 함수를 이용하는 간단 계산기 만들기
함수 만들기 :
tsum() 함수 : 2개의 인자받아서 더하기
tsub() 함수 : 2개의 인자받아서 빼기
tmul() 함수 : 2개의 인자받아서 곱하기
tdiv() 함수 : 2개의 인자받아서 나누기 몫 리턴
'''
# 함수 만들기
def tsum(x, y):
    return x + y

def tsub(x, y):
    return x - y

def tmul(x, y):
    return x * y

def tdiv(x, y):
    return x // y, x % y

# 함수 호출
def simple_caculator():
    try:
        first = int(input('첫번째 정수:'))
        second = int(input('두번째 정수:'))
    except Exception as msg:
        print('에러 발생 :', msg)
    else:
        print(f'{first} + {second} = {tsum(first,second)}')
        print(f'{first} - {second} = {tsub(first,second)}')
        print(f'{first} * {second} = {tmul(first,second)}')
        tresult = tdiv(first,second)
        print(f'{first} // {second} = {tresult[0]}')
        print(f'{first} % {second} = {tresult[1]}')
    finally:
        print('간단 계산기 끝')

if __name__ == '__main__':
    simple_caculator()