<span style="color:red">조금이라도 공부한거올리기</span>
<h1>2022-06-08</h1>
<h3> Python 8일차 </h3>
<h3>함수 정의 코드</h3>
<pre>
<code>
함수 정의(함수 만들기)
def sayHello():
    # 반환값 없고 매개변수도 없는 함수임
    print('안녕하세요.')
    print('파이선에서 함수 만들기 확인')
    return   # 반환값 없을때는 생략함
</code>
</pre>
<span>함수 정리는 9일차와 함께 정리</span>
<h3>예외 처리 소스 코드</h3>
<pre>
<code>
def test_input_error2():
    num = input('정수를 입력하세요')
    try:
        num = int(num) # 에러 발생 가능성이 있는 구문
        print(num, type(num))
    except:
        print('정수만 입력해야 됩니다. 다시입력하세요')

- 예외 처리시 except: 에 pass 를 사용하면
- 오류 발생시 프로그램이 멈추지 않고 계속 동작되게 할 수 있음

def except_pass():
    lst = ['3', '예외처리', 4, 2, 67.5, 'python']
    digit_num = []
    print(lst)
    # lst 에서 숫자만 골라내서 digit_num 에 기록 저장 처리
    for idx in range(len(lst)):
        try:
            digit_num.append(int(lst[idx]))
        except:
            pass
    print(digit_num)
</code>
</pre>
* try 구동 -> 에러발생 -> except -> finally
* try 구동 -> 정상처리 -> else -> finally
<pre>
<code>
def test_except():
    try:
        print('try area')
    else:
        print('else area')
</code>
</pre>
<h3>예외처리 구문 총정리 코드</h3>
<pre>
<code>
def try_except():
    lst = ['34', 'Hello', '4', 2, 47, 'apple']
    try:
        idx = int(input('조회할 순번 입력 : ')) - 정수가 아닌 값 입력시 에러 발생
        print(f'{idx} 번째 요소는 {lst[idx]} 이다.') - 없는 순번에 대한 에러 발생
    except IndexError as msg:
        print('잘못된 인덱스입니다.', msg)
    except ValueError as msg:
        print('숫자만 입력해야합니다', msg)
    except Exception as msg:
        print('에러 발생 :', msg)
    else:
        print('try 쪽 구문들이 정상 실행되었음')
    finally:
        print('다중 예외 처리 테스트 종료')
</code>
</pre>
[예외처리 미션 실습문제](https://github.com/bp4sp4/python_study/tree/main/day8Project/exception) mission1,2,3 확인

<h1>2022-06-07</h1>
<h3> Python 7일차 </h3>

<h3>파이선에서의 파일입출력 처리</h3>

* open() --> write() or read() --> close()
* 파일변수 = open('디렉토리명\\파일명.확장자', '열기모드')<br>
* 파일 입출력의 기본은 텍스트(문자) 파일 입출력임
* 열기모드 w,x : 새로 쓰기
*  w(wt) : 대상파일이 없으면 파일을 자동으로 새로 만듦
  * 대상파일이 있으면 기존 내용을 지우고 새로쓰기 상태로 엶
* x(xt) : 대상파일이 있으면 에러 발생남
* r(rt) 읽기전용
* a(at) : 추가 쓰기
* 대상파일이 없으면 w처럼 파일을 새로 만듦
* 대상파일이 있으면 기존 내요을 그래도 두고 열림
* 기본적으로 기존 내용 뒤에 추가쓰기됨

<h1>2022-06-03</h1>
<h3> Python 6일차 </h3>

<h1>2022-06-02</h1>
<h3> Python 5일차 </h3>

<h3>제어문(처리문) : logic </h3>
* 준비된 값의 계산 처리를 위해 사용되는 처리문장
* 종류 : 조건문, 반복문, 분기문
* 조건문 : 조건을 제시해서 결과가 참(True) | 거짓(False)이 나오게끔
        해서 결과에 따라서 처리내용이 다르게 작동되게 하는 구문
* 반복(loop)문 : 반복되는 구간을 루프(loop)라고 함 - if 문<br>
        반복 실행할 구문(들)을 원하는 횟수 또는 종료조건이 될 떄까지<br>
        반복 실행되게 작성하는 구문 - for 문, while 문
* 분기문 : 실행 순서를 중간 생략시키거나, 강제로 종료시키는 구문
        - continue 문, break 문
<pre>
<code>
if 조건식 : 
    조건식의 결과가 참(True) 일때 실행할 구문 (반드시 들여쓰기함)
    실행할 구문은 여러 개여도 됨
if (조건식) => 조건식은 ()로 묶어서 작성해도 됨
    결과가 참일때 실행할 코드 구문등
</code>
</pre>
[if문 실습문제](https://github.com/bp4sp4/python_study/tree/main/day5Project/Contional) ifMisson.py 확인

<h1>2022-05-31</h1>

<h3> Python 4일차 </h3>
<h3>사전(dict) 자료형 </h3>
* 자바의 Map 과 비슷하게 key 와 value 를 쌍으로 저장하는 구조임
* dict 에서는 키는 변겨오디지 않는 값이어야 함 (키는 지정하면 변경할 수 없다.
* => tuple 을 사용할 수 있음
* dict에 저장하는 value는 모든 자료형 데이터 가능함

<pre>
<code>
* dict 정의 방법 1 : dict() 함수 사용
def test1():
    dict1 =dict()
    print(dict1, type(dict1))

* dict 정의 방법 2 : {} 중괄호 사용
def test2():
    dict1 = {}
    print(dict1, type(dict1))

* dict 에 값 저장 방식 : 키 : 값 쌍으로 지정 표기함
def test3():
    dict1 = {'a' : 1, 'b':2, 'c':3}
    print(dict1, type(dict1))

* dict 내장함수 활용
def test5():
    dict1 = {
        'a': 10,
        'b': 25,
        'c': 77
    }
    print('dict1:', dict1, type(dict1))

    * 키에 대한 리스트 만들기 : keys() 함수
    print('dict1 의 키 목록 :', dict1.keys())

    * 값에 대한 리스트 만들기 : values()함수
    print('dict1 의 값 목록', dict1.values())
    * (키, 값) 을 item 이라고 함, 아이템을 리스트 만들기 : items() 함수
    print('dict1 의 아이템 목록 :', dict1.items())
</code>
</pre>
[내장함수 연습](https://github.com/bp4sp4/python_study/tree/main/day4Project/mission) 3개 파일 확인

<h1>2022-05-30</h1>
<h3> Python 3일차 </h3>

<h3>list 자료형 특징 : 리스트를 다루는 함수(메소드)들이 제공됨</h3>

  * append() : 뒤에 추가 <br>
  * insert() : 사이에 추가 <br>
  * remove() : 값 삭제 <br>
  * pop() : 꺼내면서 리스트에서 뺌 <br>
  * reverse() : 리스트 안에 데이터 순서를 반대로 바꿈(뒤집기) <br>
  * clear() : 리스트 비움<br>

<h3>문자열에 포맷(format) 적용해서 코드 작성 방법</h3> <br>
  * 문장(문자열)에 여러 종류의 값을 섞어서 적용하고자 할 떄 사용 함 <br>
  * 포맷문자 이용 : %서식문자 (서식문자는 값타입에 따라 정해져 있음) <br>
  * 정수 : %d (decimal : 10진수), %o (octal : 8진수), %x(hex: 16진수 <br>
  * 실수 : %f <br>
  * 문자열 : %s
  * 기호 % 출력시에는 %% <br>
<pre>
<code>
pname = input('상품명 :')
pamount = int(input('갯수 : '))

print(pname, '제품을', pamount, '개 주문하였습니다', sep='')
print(f'{pname} 제품을 {pamount}개 주문 하였습니다.')
print('%s 제품을 %d 개 주문하였습니다.' %(pname, pamount))
print('{} 제품을 {} 개 주문하였습니다.'.format(pname,pamount))

format() 사용시 값 적용 순서를 조정할 수도 있음
st1 = '이름은 {1}이고, 나이는 {2}세이고 혈액형은 {0}형입니다.'.format('B', '홍길동', 27)
print(st1)

format() 안에서 값에 이름을 지정할 수 있음
문장 안에 순번이 아닌 {이름}을 적용할 수도 있음
st2 = 'Today is {today}. Tomorrow is {tomorrow}.'.format(today='Monday', tomorrow='Tuseday')
print(st2)

</code>
</pre>


* <h3>자료형이란</h3>
  * 파이선은 객체지향형 스크립트 언어이다. <br>
  * 자료형(값의 종류)은 객체와 레퍼런스로 관리됨 <br>
  * 객체(object) : 클래스(class)로 만들어진 결과물(기억공간) <br>
  * 레퍼런스(reference) : 객체의 위치(주소) 정보를 가진 주소변수 <br>
  * 객체(변수)가 가지는 값은 실행될 때 동적할당(allocation)되도록 되어 있음 <br>


<h1>2022-05-27</h1><br>

<h3> Python 2일차</h3>

[문자열다루기](https://github.com/bp4sp4/python_study/blob/main/day2Project/chap03_str.py)
chap03_str.py 참고하여 공부

* <h3>변수 할당시 = (대입연산자) 사용함</h3>
  * 대입연산자는 반드시 완쪽에는 변수를, 오른쪽에는 값 또는 계산식 위치함<br>
  * 값 = 변수 : 에러임<br>
  * 파이선의 input() 함수로 입력되는 값은 모두 문자형(str)이다.
  * 숫자형으로 바꾸고자 한다면, 정수는 int('정수문자'), 실수는 float('실수문자') 사용함 <br>
  * 문자형으로 바꾸고자 한다면, str('문자') 사용함
 <pre>
<code>
error code
 * 100 = a <-- error <br>
 print('더하기 확인 :', num+100) <-- error  숫자와 문자는 계산할 수 없음

# f-string 포매팅 사용
print(f'{custom_name}고객님의 사용금액은 {price}원, 발생 포인트는 {int(point)}')

# format()사용
print('현재 이용 하실수 있는 누적포인트는 {} 점입니다.'.format(total_point))
</code>
</pre>


* 순수대입연산자
  + 합 대입 연산자 : 산술대입연산자가 주로 사용됨 
  + 산술연산자 : +, -, *, /, **, //, %(mod)
  + +=, -=, *=, /=, %=, **=, //= 
  + 메모리의 변수공간의 값에 직접 연산하므로 연산속도가 빠름 (사용 권장함)
  <hr>

* 파이선 코드 문장은 한줄 작성이 원칙임
* 문장이 길어서 한 줄 작성이 불편할 경우에는 여러 줄로 나눌 수 있음 
* 줄 끝에 반드시  백슬러시(\)를 표시해야함

<h1>2022-05-26</h1> <br><h3><P>PyCharm 1일차</h3></P>
 
 * 식별자 : 프로그래머가 지어주는 이름을 말함<br>
 * 변수(variable) : 프로그램 구동시 메모리(RAM)에 값 기록하는 공간(방)<br>
 * 함수(function) : 반복 사용되는 코드의 부분코드에 이름 표시한 것<br>
 * 모듈(module) : 함수들을 따로 모아놓은 파일<br>
 * 클래스(class) : 파이선은 객체지향형 스크립트 언어임
 * 한 줄 주석은 앞에 '#' 기호 붙임
<hr>
<p>주석 예재 코드 </p>
<pre><code>
'''<br>
파이선의 여러줄 주석문(comment)
작은 또는 큰 따옴표를 앞뒤에 3개씩 표시하면 됨<br>
'''
# 샵을 사용해 주석 처리 가능
</code>
</pre>

