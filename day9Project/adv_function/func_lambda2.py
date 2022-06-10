# func_lambda2.py
# 람다함수를 이용하는 내장함수 테스트

# map 내장함수 : 맵객체변수 = map(실행할함수명, 시퀀스객체)
# 시퀀스(sequence) 객체 : 값을 순차적으로 저장한 객체, 리스트, 튜플이 해당
# 시퀀스 객체의 각 요소값을 하나씩 꺼내서 함수로 ㅂ내고
# 처리 결과를 리턴받아서 맵객체에 저장하는 함수
import operator


def func(x):
    return x * x

def test_map():
    lst = [1,2,3,4,5]
    m = map(func, lst)
    print(m, type(m)) # 참조 객체 타입과 16진수 주소(id)가 출력된
    print(list(m))

    # 함수명 대신에 람다함수 작성으로 바꾼다면
    m = map((lambda x: x * x), lst)
    print(list(m))

    # 람다는 코드를 간결하게 표현하는게 목적임
    # 위의 코드를 한줄로 바꾼다면
    print(list(map((lambda x: x * x), [1,2,3,4,5])))

# filter 내장 함수 : 필터결과객체 - filter(실행함ㅅ명, 시퀀스객체)
# 시퀀스 객체의 각 요소값에 대해 함수 처리 결과가 참(True)인
# 요소만 골라내는 함수임

def func1(x):
    return  x > 2

def test_filter():
    nlist = [1, -2 , 4, 7]
    f= filter(func1, nlist)
    print(f, type(f))
    print(list(f))
    #람다로 한줄로 코드를 간결하게 작성
    print(list(filter((lambda x: x > 2), [1, -2, 4,7])))


# sorted() 내장함수
# 시퀀스에 저장된 복잡한 객체를 정렬할 떄 사용하는 함수
# 정렬객체 변수 = sorted(정렬할 시퀀스 객체, key = 정렬에 사용할 키)
# reverse = True | False (기본값)

def test_sorted():
    students = [
        ('김영희', 'A', 95),
        ('홍철수', 'B', 96),
        ('이길동', 'C', 90)
    ]

    print(students)
    print(sorted(students)) # 키 지정 누라식, 각 요소의 [0]번째가 자동 키로 지정됨
    print(sorted(students, key=lambda  x: x[1])) # [1]번째 정렬의 키가 됨
    print(sorted(students, key=lambda  x: x[2])) # [2]번째 정렬의 키가 됨

    # sorted() 에서 키 지정시,
    # sorted() 에서 키 지정시, 파이선이 제공하는 operator 모듈을 이용할 수도 있음
    print(sorted(students, key=operator.itemgetter(2))) # [2]번째가 정렬의 키가 됨
    # 내림차순정렬 : reverse=True 로 지정함
    # 점수 기준 내림차순 정렬한 경우
    print(sorted(students, key=operator.itemgetter(2), reverse=True))


if __name__=='__main__':
    test_sorted()