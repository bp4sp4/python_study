<h1>2022-05-30</h1>
<h3> Python 3일차 </h3>

<h3>list 자료형 특징 : 리스트를 다루는 함수(메소드)들이 제공됨</h3>
  * append() : 뒤에 추가
  * insert() : 사이에 추가
  * remove() : 값 삭제
  * pop() : 꺼내면서 리스트에서 뺌
  * reverse() : 리스트 안에 데이터 순서를 반대로 바꿈(뒤집기)
  * clear() : 리스트 비움

<h3>문자열에 포맷(format) 적용해서 코드 작성 방법</h3>
  * 문장(문자열)에 여러 종류의 값을 섞어서 적용하고자 할 떄 사용 함
  * 포맷문자 이용 : %서식문자 (서식문자는 값타입에 따라 정해져 있음)
  * 정수 : %d (decimal : 10진수), %o (octal : 8진수), %x(hex: 16진수
  * 실수 : %f
  * 문자열 : %s
  * 기호 % 출력시에는 %%
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
  * 파이선은 객체지향형 스크립트 언어이다.
  * 자료형(값의 종류)은 객체와 레퍼런스로 관리됨
  * 객체(object) : 클래스(class)로 만들어진 결과물(기억공간)
  * 레퍼런스(reference) : 객체의 위치(주소) 정보를 가진 주소변수
  * 객체(변수)가 가지는 값은 실행될 때 동적할당(allocation)되도록 되어 있음


<h1>2022-05-27</h1><br>

<h3> Python 2일차</h3>

[문자열다루기](https://github.com/bp4sp4/python_study/blob/main/day2Project/chap03_str.py)
chap03_str.py 참고하여 공부

* <h3>변수 할당시 = (대입연산자) 사용함</h3>
  * 대입연산자는 반드시 완쪽에는 변수를, 오른쪽에는 값 또는 계산식 위치함<br>
  * 값 = 변수 : 에러임<br>
  * 파이선의 input() 함수로 입력되는 값은 모두 문자형(str)이다.
  * 숫자형으로 바꾸고자 한다면, 정수는 int('정수문자'), 실수는 float('실수문자') 사용함
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

