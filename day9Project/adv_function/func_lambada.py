# func_lambda.py
# 파이선에서 람다함수 만들기

'''
리스트 내포, 간단 조건문처럼 여러 줄로 된 코드를 간결하게 표현할 수 있는 새로운 함수 정의방법
def로 정희하는 함수를 간단하게 lambda 로 작성함
한줄로 표현 가능한 처리 내용일 떄  주로 이용함
일회성 코드일 떄 이용할 수 있음
함수 이름이 없음. 참조변수가 함수이름을 대신할 수는 있음

작성과 사용법 :
참조변수 = lambda 매개변수, 매개변수 : 처리구문
사용1 : 참조변수(전달값, 전달값)
사용2 : (lambda 매개변수, 매개변수 : 처리구문) (전달값, 전달값)
'''

# 일반 함수 만들기
def add(x, y):
    return x+y

# 람다함수 만들기
add2 =lambda x,y: x+y

if __name__ == '__main__':

    #일반함수 실행
    result = add(10, 20)
    print('더하기:', result)

    #람다함수 실행(사용)
    result = add2(10, 20)
    print('람다 확인 :', result)

    # 주로 이용 : 람다함수 자것ㅇ과 실행을 함꼐처리
    print('더하기 결과 :', (lambda x,y: x+y)(10,20))

    #람다함수 매개변수에도 기본, 키워드, 가변
    print('(기본)더하기 결과 :', (lambda x,y =20 : x+y)(10))
    print('(기본)더하기 결과 :', (lambda x,y: x+y)(y=10, x=20))
    print('(기본)더하기 결과 :', (lambda x, *y: x*y)(3, 1, 2,3))

    #람다함수 안에 간단 조건문 사용할 수 이씅ㅁ

    def add(x, y):
        return x + y
    print(lambda x,y : x if x % 2 == 0 else y)(3,5)
