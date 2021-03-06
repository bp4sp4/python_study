# 경로 표현 : loop/loppSample.py
# 모듈 표현 : loop.loopSample

'''
연산자(operator) :계산용 기호문자
연산자 우선순위 :
    여러 연산자가 섞여서 계산식이 구성될 경우,
    우선 순위가 높은 연산자가 먼저 계산이 되고, 계산된 결과를 가지고
    다음 순위의 연산자가 작동됨
    우선 순위가 같을 때는, 왼쪽에서 오른쪽으로 계산해 나감

1순위 (최우선 연산자) : (), {}
2순위 (단항 연산자 : 값 1개만 필요한 연산자) : +(sign),-(sign), ++(1증가), --(1감소), not(논리부정), not(논리부정),
-(tield :틸드(비트반전) -> bit 1 => 0, bit 0 =>1
이항 연산자 : 값 2개가 필요한 연산자
산술, 쉬프트(shift :비트 자리이동 연산ㄴ자), 비교(관계), 논리연산자
3순위(산술 연산자) : *, // | /, %(mod)
4순위(산순 연산자) : +,-
5순위(쉬프트 연산자) : 비트자리이동 연산자 => >> ,<<
6순위(비교 연산자) : <,>, <=, >=
7순위(비교 연산자) : ==, !=
8~ 12순위 (논리연산자) : 비트 논리 연산자
                        8순위 : and
                        9순위 : or
                        10순위 : ^(xor)
                        일반 논리 연산자 :
                        11순위 : and
                        12순위 : or
13순위(삼항연산자) : 항목이 3개로 구성, 조건식과 유사한 연산자
    변수 = 조건식? 값1 :값2
    조건이 참이면 값1, 거짓이면 값2를 변수에 대입함
14순위(대입연산자) : 순수대입연산자 =
    복합대입연산자 : 산술대입, 쉬프트 대입, 비트논리대입
    +=, -=, *=, **=, /=, //= , %=, >>=, <<= ,^ = ,|=, ^=1
15순위 (나열 연산자) : ,
'''

# 파이선에서의 반복문 작성과 사용
# 반복문(loop문)
# for 문 : 반복할 횟수가 정해진 경우에 주로 사용함
# while 문 : 반복할 횟수가 정해지지 않은 경우에 주로 사용함

# for 문 작성형식 1:
'''
for 변수 in 리스트 | 튜플 | 딕션너리 | 문자열 :
    반복 실행할 구문들 (변수 이용할 수 있음)
    
주의사항 : in 오른쪽에 정수리터럴(숫자) 사용 못 함 
for 변수 in 정수숫자: -> TypeError 발생함
    반복실행구문
'''
def  for_test1(): #TypeError 발생
    for k in 10:
        print(k)
# list 사용
def for_list():
    for i in [10, 20,30]:
        print(f'{i}은 5의 배수이다.')

# tuple 사용
def for_tuple():
    for t in (11,22,33,44,55):
        print(f'{t}는 짝수다.' if(t%2 ==0) else f'{t}는 홀수다.')

# set 사용
def for_set():
    for s in {1,2,3,4,5,6}:
        print(f'{s}의 제곱은 {s**2}이다.')\

# 문자열(str) 사용
def for_str():
    for st in 'Python':
        print(f'{st} 문자의 유니코드는 {ord(st)}이다.')

#for 문 작성형식 2 : range() 함수 사용
# range(시작값, 끝값) 또는 range(시작값, 끝값, 간격)
# 시작값 >=n >끝값, 간격은 생략되면 기본값이 1임

'''
for 변수 in range(start,end)
    변수를 사용한 반복실행 구문
'''
# 1부터 100까지 정수들의 합계를 구해서 출력 처리
# 반복할 내용 : 더하기(누적합산)
# 0 + 1 + 2 + 3 + 4 + .......+ 100
def for_sum():
    sum = 0
    for n in range(1, 101):
        print(n, ' + ', end='')
        sum += n

    print() # 그냥 엔터키 한번 누른것과 같은 효과
    print(f'합계 :{sum}')

# -------------------------------------------------
# import collections.iterable => deprecated : 버전업하면서 사용이 중지됨
import collections.abc

def test_iterable():
    nlist = [1,2,3,4]
    # iterable object : 리스트처럼 순차저긍로 값을 가진 객체를 말함
    # 목록 객체로 표현할 수 있음
    # isinstance() 함수 : 객체의 종류를 확인할 때 사용함
    print(isinstance(nlist, collections.abc.Iterable))
    # lterable 의 첫글자 대문자임

# range(시작값(이상), 끝값(미만), 스텝(값의 간격 : 기본 1) 함수
# range(끝값) => 예 > range(10) : 자동으로 시작값은 0부터  9까지 가능
def test_range():
    print(range(10)) # range(0, 10)
    lst = list(range(10))
    print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for 문 작성형식 3 : range() 연속 값을 인덱스로 이용
def for_indexing():
    # 리스트에 저장된 값 추출
    list1 = ['apple', 90, [1,2,3], ('A', 'B', 'C')]
    for data in list1:
        print(data)

    # 리스트의 저장 값을 인덱스를 이용해서 연속 처리
    for idx in range(len(list1)): #range(4) => range(0, 4)
        print(f'인덱스{idx} 번째 : {list1[idx]}')
