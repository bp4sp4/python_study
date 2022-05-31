# 경로 표시(백슬러시 \) : test_logic\\chap07_conditional.py
# 경로 표시(슬러시 /)test_logic/chap07_conditional
# 모듈 표현 : test_logic.chap07_conditional

# bool 자료형 확인
def func_bool():
    flag = True
    print('flag : ', flag, type(flag))

    flag = False
    print('flag : ', flag, type(flag))

    # 파이선에서는 대소문자 구분함
    # flag = true # NameError

# bool() 함수 사용 : bool 형으로 자료의 논리상태를 확인할 때 사용함
# 리턴되는 결과값은 True | False
def func_bool2():
    print("결과 :", bool('abcd')) # True
    print('결과 :', bool('')) # False
    # 값이 저장되어 있는지 , 비어 있는지 확인하는 용도로 사용할 수 있음
    # print(bool({'a':1, 'b':2})) # True
    # print(bool({})) # False

    # print(bool)([1,2,3,4,]) # True
    # print(bool([])) #False
    #
    # print(bool)([1, 2, 3, 4, ])  # True
    # print(bool([]))  # False

    print(bool(23)) # 0을 제외한 모든 값은 True 임
    print(bool(0)) # False

# 비교(관계) 연산자 확인
# 2개의 값을 가지고 크냐(>,초과)/작으냐(<,미만)
# 같으냐(==)/같지않느냐(!=)크거나같으냐(>=)/작거나같으냐(<=,이하)
# 이항 연산자에 해당됨 : 값1 연산자 값2

def func_compare():
    print('1 == 1 :', 1 == 1) # True
    print('1 == 2 :', 1 == 2) # False

    print('1 > 0 :', 1 > 0) # True
    print('1 < 2 :', 1 < 2) # True

    print('1 >= 1 :', 1 >= 1) # True
    print('1 != 0 :', 1 != 0) # True

# 논리 연산자 : 논리값(True, False)을 계산에 사용하는 연산자
# and, or ,not
def func_logical():
    a = 1
    b = 2

    print(a > 0 and b > 1) # True and True --> True
    print(a ==0 or b != 1) # False or True --> True

    # and 연산자의 특징 :
    # 앞 and 뒤 : 앞이 False 이면 뒤를 실행 안 함
    # 앞이 True 이면 
