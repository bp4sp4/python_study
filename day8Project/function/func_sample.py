# func_sample.py
# 파이선에서 함수 만들어 사용하기

'''
함수의 정의 : 반복 사용되는 소스 코드를 별도로 작성해서 이름 붙인 것

파이선에서 함수 만들기
def 함수명(매개변수):  => 매개변수(parameter) : 0 ~ n개까지 정의 가능
    함수가 수행할 코드 구문
    .........
    return 값 또는 변수 또는 값,값,...,값 => 반환값 없을 때는 return 생략

함수의 사용 : 함수 호출(function call) 이라고 함
    함수는 만들어진 형태에 맞춰서 사용해야 함
    => 함수이름 틀리지 않아야 함 (대소문자 주의, _ 갯수 확인)
    => 매개변수와 갯수를 일치되게 사용해야 함 : 전달인자(argument)
        함수명(전달할값)
        매개변수와 전달값의 갯수는 반드시 같아야 함
    => 전달값의 의미도 확인이 필요함
    => 반환값 여부도 확인해야 함
        함수명(전달값)  => 반환값 없는 함수의 사용임
        반환값 받는 변수 = 함수명(전달값) => 반환값 있는 함수의 사용임
        다른함수(함수명(전달값)) => 반환값 있는 함수만 중첩사용 가능함
'''
# 함수 정의(함수 만들기)
def sayHello():
    # 반환값 없고 매개변수도 없는 함수임
    print('안녕하세요.')
    print('파이선에서 함수 만들기 확인')
    return   # 반환값 없을때는 생략함

# 함수 사용(함수 호출)
# 함수명(전달값)

# 아무런 기능도 없는 (처리 코드가 없는) 빈 함수를 만들때는 pass 사용
def func():
    pass

# 함수 이름 아래에 함수 설명(description)을 적어둘 수 있음
# 따옴표 사용함
def hello():
    '이 함수는 함수 작성 연습용입니다.'
    print('Welcome!')
    print('함수명에 공백, 예약어 사용 못 함')
    return  # 반환값 없는 리턴은 생략해도 됨

# 매개변수가 있고, 반환값도 있는 함수 작성
def add(x, y):
    print(f'x : {x}, y : {y}')
    return x + y

# if __name__ == '__main__':
    # sayHello()
    # 함수 호출(call)
    # hello()
    # 함수의 설명(description)을 확인할 때 help(함수명) 사용
    # help(hello)
    # help(input)
    # help(print)

    # 매개변수 있고, 반환값 있는 함수의 사용(call)
    # 매개변수 갯수가 동일하게, 전달값을 함수 () 안에 사용해야 함
    # 반환값 받는 변수가 필요함
    result1 = add(10, 20)
    print(result1)
    result2 = add(1.3, 4.5)
    print(result2)

    # 코드의 줄수를 줄이기 위해 함수 중첩 사용할 수도 있음
    # 함수(반환값있는함수(전달값))
    # 안쪽함수의 반환값을 바깥함수가 사용하게 됨
    print(add(11, 22))
    print(add(3.3, 4.4))

# 파이선에서는 여러 개의 값을 리턴할 수 있음
# 자동 tuple 로 처리됨
def func2(a, b):
    print(f'a : {a}, b : {b}')
    return a * 2, b * 2

# 변수의 사용 영역(지역, 스코프 scope)
# 지역변수(Local Variable)와 전역변수(Global Variable)
# 지역변수 : 함수 안에서 만들어진 변수
def func1():
    num = 10  # 지역변수임
    print('num : ', num)

# 함수 밖 영역
# print('num : ', num)  # 지역변수는 함수 밖에서 사용 못 함

# 파이선에서의 전역변수 : 함수 밖에서 만든 변수
# 소스 파일 안에서 어디서나 사용 가능함
ga = 100  # 전역변수임
print('ga : ', ga)

def func_global():
    # print('전역변수 ga : ', ga)  # 아래쪽의 지역변수 ga 때문에 에러임
    ga = 200  # 파이선에서 변수의 값 기록은 새로운 생성(할당)임
    # 지역변수 ga 가 새로 만들어짐
    print('지역변수 ga : ', ga)  # 지역변수 ga 값 출력임

# 함수 안에서 전역변수의 값을 변경하려면
# global 전역변수명 선언하고 사용하면 됨
# 전역변수 사용을 선언하는 것임
def func_global2():
    global ga  # 전역변수 사용을 선언함 (먼저 선언하고 사용해야 함)
    print('전역변수 ga : ', ga)
    ga = 200   # 전역변수 값 변경임
    print('전역변수 ga : ', ga)





if __name__ == '__main__':
    # print(func2(2, 4), type(func2(2, 4)))
    #
    # tp = func2(3, 2)
    # print(tp, type(tp))

    # func_global()
    func_global2()