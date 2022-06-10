# func_sample.py
# 파이선 함수 만들기(정의)와 함수 사용(호출) 연습

# 매개변수(parameter)와 전달인자(argument) 관계
# 매개변수 : 함수 실행(호출)시 전달값을 받는 변수
#           함수 실행시 전달값에 따라 자료형이 결정됨
# 전달인자 : 함수쪽으로 전달되는 값 또는 주소
#           함수명(전달값, 전달값, 전달객체, ....)
# 주의 : 함수 사용시 매개변수 갯수와 전달인자의 갯수가 반드시 일치해야 함
def tmax(a, b):
    '두 개의 값을 전달받아서, 둘 중 큰 값을 알아내서 리턴 처리함'
    print(f'a : {a}, b : {b}, type : {type(a)}, {type(b)}')
    if a > b:
        return a
    else:
        return b
#----------------------------------------------

def tmax2(a, b):
    '두 개의 값을 전달받아서, 둘 중 큰 값을 알아내서 리턴 처리함'
    print(f'a : {a}, b : {b}, type : {type(a)}, {type(b)}')
    max_value = 0
    if a > b:
        max_value = a
    else:
        max_value = b
    a = 100   # 매개변수가 받은 값 변경
    b = 200   # 매개변수가 받은 값 변경
    print(f'a : {a}, b : {b}, type : {type(a)}, {type(b)}') # 변경확인
    return max_value # return 은 맨마지막에 딱 한번 실행되게 해야 됨
# ----------------------------------------------

def func_param_args():
    '매개변수와 전달인자 갯수 맞추기 테스트용 함수'
    result = tmax(10, 20)
    print(f'큰값 : {result}')
    print(f'큰값 : {tmax(44.5,12.3)}')
    print(f'큰값 : {tmax("M","m")}')
    # result = tmax(123) # 에러 발생 : 전달값과 매개변수 갯수가 다름
    # result = tmax(10, 20, 30)
#----------------------------------------------

def func_call_value():
    '함수로 값 전달 확인용 함수'
    num1 = 10
    num2 = 20
    print(f'num1 : {num1}, num2 : {num2}') # 함수 실행전 값 확인
    result = tmax2(num1, num2)
    print(f'큰값 : {result}')
    # 함수쪽에서 변경한 값이 호출부의 변수에 영향을 줬는지 확인
    print(f'num1 : {num1}, num2 : {num2}') # 함수 실행후 값 확인
#----------------------------------------------

# 파이선에서는 군집자료형을 전달받는 매개변수는 기본으로
def list_in_max(plist):
    '리스트 객체를 전달받아서, 저장된 값중에 가장 큰 값을 찾아내서 반환'
    print(f'plist : {plist}, 주소 : {id(plist)}')
    max = plist[0] # 첫번째 값을 변수에 저장
    for value in plist:
        if max < value:
            max = value
    # 파이선에서는 전달 받은 객체의 요소는 변경할 수 있음
    plist[0] = 100
    print(f'plist : {plist}, 주소 : {id(plist)}') # 요소값 변경 확인
    return max
#-----------------------------------------------

def fun_call_reference():
    nlist = [15, 24, 31, 38, 46, 67, 123]
    print(f'nlist : {nlist}, 주소 : {id(nlist)}') # 함수 실행전 확인
    result = list_in_max(nlist)
    print(f'가장 큰 값 : {result}') # 함수 실행후 확인
    print(f'nlist : {nlist}')# 함수 실행후 확인 (함수쪽에서 바뀐값)
#-----------------------------------------------

# 기본 매개변수 : 기본값(default)을 가진 매개변수
# 함수 만들때 매개변수에 기본값을 지정할 수 있음:
# def 함수명(매개변수=기본값, 매개변수=기본값):
# 뒤쪽 매개변수부터 기본값을 지정해야 함:
# def 함수명(매개변수, 매개변수, 매개변수=기본값):
# 에러주의 : def 함수명(매개변수=기본값, 매개변수)
# 에러주의 : def 함수명(매개변수, 매개변수=기본값, 매개변수):

# 함수 실행시 기본 매개변수에 전달값 생략할 수 있음
# 전달값이 없으면 준비된 기본값을 사용하게 됨
# def tmin(a, b, c=0):
# def tmin(a, b=0, c=0):
def tmin(a=0, b=0, c=0):
    '세 개의 값을 전달받아서, 가장 작은값을 찾아서 리턴하는 함수'
    print(f'a : {a}, b : {b}, c : {c}')
    min_value = 0
    if  a < b and a < c:
        min_value = a
    elif b < c:
        min_value = b
    else:
        min_value = c
    return min_value
#-------------------------------------------------------

def func_default_param():
    # 사용할 함수가 기본값이 없는 매개변수이면, 갯수 맞춰야함
    print(f'가장 작은 값 : {tmin(12, 3, 90)}') #전달값 3개
    # 전달 값 갯수 맞지 않으면 에러 발생
    print(f'가장 작은 값 : {tmin(12,3)}') #전달값 2개
    print(f'가장 작은 값 : {tmin(12)}') #전달값 1개
    print(f'가장 작은 값 : {tmin()}')  # 전달값 0개
# -------------------------------------------------------

# 키워드 매개변수
# 함수 사용할 떄(함수 호출시) 매개변수=전달값 의 형태를 사용할 수 있음
# 함수명(매개변수명=전달값)
# 매개변수 순서는 상관없음
def num_calc(a, b, c, d, e):
    return (a + b - c * d / e)

def func_keyword_call():
    result = num_calc(10, 9 , 8, 7, 6) # 10 + 9 - 8 * 7 / # 6
    print(f'result : ',result)
    result = num_calc(c=8, b=9, e=6, a=10, d=7) # 키워드 매개변수 표기
    print(f'result : ',result)

# 가변 매개변수 : 전달받을 값의 갯수를 정하지 않는 매개변수임
# 함수 만들 때 매개변수 이름 앞에 * 표시함
# def 함수명(*매개변수) : 전달값은 0 개 ~ N 개임
# 가변 매개변수의 자료형은 tuple 임
def dynamic_param(*args):
        '가변 매개변수가 받은 값들을 확인하는 함수'
        print(f'args: {args}, 자로형 : {type(args)}')
        for idx in range(len(args)):
            print(f'{idx}번째 전달값 : {args[idx]}')
#-----------------------------------------------------------------------

def func_daynamic():
    '가변 매개변수를 가진 함수 사용 테스트'
    dynamic_param() #전달값 0개
    dynamic_param(10) #전달값 1개
    dynamic_param(2, 3)
    dynamic_param(4, 3, 23, 6, 5, 8, 67, 10)
#----------------------------------------------------------

# 전역변수(Global Variable) : 함수 밖에 선언한 변수
# 선언한 위치 아래쪽 코드 어디서나 사용할 수 있는 변수임
message = '전역변수'
print('message :', message)

def func_variable():
    print('함수 안 :', message) # 전역변수 사용
    # 지역변수(Local Variable) :  함수 안에서 선언한 변수
    # 매개변수도 지역변수임
    value = '지역변수'
    print('value :', value)
    # 함수 안에서 전역변수 값 변경하려면
    # 먼저, 전역변수 사용을 선언해야 함
    # global 전역변수명 => 주의 : 전역변수 사용 전에 선언해야 함
    message = '함수 안에서 값 변경'
    # 전역변수 값 변경확인
    print('message :', message)

#------------------------------------------------------
# 지역변수는 함수 밖에서 사용 못함
# print('value :', value)


#작성된 함수 실행 테 스트용 함수 정의
def test_function():
    prompt = '''
    ******* 파이선 함수 정의와 사용 테스트 *********
    1. 매개변수와 전달인자의 관계 확인
    2. call by value (값 전달 방식) 확인
    3. call by reference (주소 전달 방식) 확인
    4. 기본 매개변수
    5. 키워드 매개변수
    6. 가변 매개변수
    7. 지역변수와 전역변수
    0. 끝내기
    '''
    while True:
        try:
            print(prompt)
            no = int(input('번호 선택 : '))
        except:
            print('숫자만 입력하세요')
            pass
        else:
            if no == 1:
                func_param_args()
            elif no == 2:
                func_call_value()
            elif no == 3:
                fun_call_reference()
            elif no == 4:
                func_default_param()
            elif no == 5:
                func_keyword_call()
            elif no == 6:
                func_daynamic()
            elif no == 7:
                func_variable()
                # 전역변수 값 변경확인
                print('어디서나 사용 가능 - message :', message)
            elif no == 0:
                print('함수 테스트 종료')
                break
            else:
                print('다른 숫자 입력 확인! 0~7번까지 번호 입력해주세요')



 #   프로그램 구동 ------------------------------------
if __name__=='__main__':
    test_function()