# mymodule.py
# 사용자 정의 모듈
# 모듈 표현 : module.mymodule

# 함수(기능)들과 변수(전역변수)들 작성
# 실행 코드는 포함하지 않는다
# 저장해 놓고 사용하려는 목적임


# 변수
# pi = 3.14159
# count = 10


# 함수(기능) ----------------------------

# 두 수를 전달받아서 더하기 결과 리턴
def sum(a,b):
    return a+b


# 두 수를 전달받아서 빼기 결과 리턴
def sub(a,b):
    return a-b

# 두 수를 전달받아서 곱하기 결과 리턴
def mul(a,b):
    return a*b

# 두 수를 전달받아서 나누기한 몫을 리턴
# 단, 나눌 수가 0이면 EXCEPTION 발생시킴 :  '0으로 나눌 수 없음'
def divide(a,b):
    if b == 0:
        raise  Exception('으로 나눌수없다.')
    else:
        return  a / b

# 두 수를 전달받아서 나누기한 나머지를 리턴
# 단, 나눌 수가 0이면 EXCEPTION 발생시킴 :  '0으로 나눌 수 없음'
def mod(a,b):
    if b == 0:
        raise  Exception('으로 나눌수없다.')
    else:
        return  a % b

# 가변매개변수를 사용해서, 전달받은 수들 중 가장 큰 값을 리턴
def max(*args):
    try:
        max_value = args[0]
        for data in args:
            if max_value < data:
                 max_value = data
            return max_value
    except:
        print('처리할 데이터가 없습니다.'),

# 가변매개변수를 사용해서, 전달받은 수들 중 가장 작은 값을 리턴
def min(*args):
    try:
        min_value = args[0]
        for data in args:
            if min_value > data:
                 min_value = data
            return min_value
    except:
        print('처리할 데이터가 없습니다.'),

# 문자열을 전달받아서, 글자 갯수를 리턴
# 기본 매개변수로 지정 : None 지정
# 매개변수가 None이면 0 리턴
def strlen(st = None):
    slen = 0
    if st != None:
        for ch in st:
            slen += 1
            return  slen

if __name__ == '__main__':
    strlen()