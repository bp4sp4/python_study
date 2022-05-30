# chap03_builtType.py
# 파이선 내장자료형(built in type) 확인용

# 파이선은 객체지향형 스크립트 언어이다.
# 자료형(값의 종류)은 객체와 레퍼런스로 관리됨
# 객체(object) : 클래스(class)로 만들어진 결과물(기억공간)
# 레퍼런스(reference) : 객체의 위치(주소) 정보를 가진 주소변수
# 객체(변수)가 가지는 값은 실행될 때 동적할당(allocation)되도록 되어 있음

# a # 변수 선언(변수 방이름 지어주는 것)만으로는 에러임
a = 1 # 반드시 값 기록이 되어야 변수 생성이 됨
# 1은 정수이므로, 변수고악ㄴ a의 type은 <class 'int'> 가 됨
# 변수 생성시 메모리에 객체공간을 만들고, 객체 안에 1을 기록하고
# 만들어진 객체의 주소를 a에 기록함
# a 는 값을 가진 객체의 주소를 가진 레퍼런스 변수임
print('a 가 참조하는 객체가 가진 값:', a)
print('a가 가진 위치 정보:', id(a))

b = 1
print('b 가 가진 위치(주소)정보 : ', id(b))
# 파이선은 같은 값이 메모리에 객체로 존재하면, 새로 할당하지 않고
# 기존의 객체의 주소를 리턴함
# a가 가진 주소와 b 가 가진 주소가 같음

a = 2 # <class 'int> 객체 공간을 만들고, 그 안에 2 기록하고
# 2가 기록된 객체 공간의 주소를 a에 기록함
print('a 가 참조하는 객체가 가진 값:', a)
print('a가 가진 위치 정보:', id(a))

print('b 가 참조하는 객체가 가진 값:', b)
print('b가 가진 위치 정보:', id(b))

# 정수 : <class 'int'>, 양수, 0, 음수 1씩 차이나는 수
num1 = 0
num2 = -11
num3 = 24
print('num1 :', num1, type(num1), id(num1))
print('num2 :', num2, type(num2), id(num2))
print('num3 :', num3, type(num3), id(num3))

# 정수 자료형 값 표현은 기본 10진수임
# 파이선에서도 코드 구문에 정수값 표현시 다른 진수들을 사용할 수 있음
# 정수값 앞에 진수를 표시하는 접두어를 붙여주면 됨
# 8진수(octal)는 숫자 앞에 0o(zero 영문자 o)을 표기함
# 16진수(hex)는 숫자 앞에 0x | 0X 를 표기함
# 파이선에서는 2진수(bit)도 표기할 수 있음, 숫자 앞에 0b를 표기함
dnum = 12345 # 10진수(decimal)
bnum = 0b0111 # 2진수(bit)
onum = 0o12 # 8진수(octal)
xnum = 0xf5 #16진수(hex)

# print() 함수로 출력시에는 ㅓㅈㅇ수는 십진수로 출력되도록 되어 있음
print('dnum :', dnum, type(dnum), id(dnum))
print('bnum :', bnum, type(bnum), id(bnum))
print('onum :', onum, type(onum), id(onum))
print('xnum :', xnum, type(xnum), id(xnum))

# 문자형태로 된 숫자는 계산 할 수 없음
# 계산할수 있게 하려면 숫자로 변환해야함
# int('정수형문자'), float('실수형문자')
snum = '789'
print('snum :', snum, type(snum))
# result = snum + 2 # 원하는 결과는 791 => error
#해결
result = int(snum) + 2
print('result : {}, {} \n'.format(result, type(result)))

# 파이선에서는 정수 자료형 값의 범위 제한이 없음
# c언어, c++ int 값 범위 : -32678 ~ 32767
# 자바의 int 값 범위 : - 2147693748 ~ 2147493847

inum = 1234567899999999999999999999999999999999999999999999
print('inum : {}, {} \n'.format(inum, type(inum)))

# 실수 자료형 : <class 'float'>
# 소숫점 아래 값을 취급하는 수
# 1.23(부동소수점형 표기 | 비과학용 표기, flating),
# 123 + e-2 (과학용 표기, scientific)
# 과학용 표기는 +는 오른쪽, -는 왼쪽으로 소수점을 이동시킨다는 의미임
# e제곱수는 자리이동 칸수를 의미함, 10의 제곱수를 의미함
# + e3은 (* 10의 3제곱), -e3 은 (/10의 3제곱)을 의미함
fnum = 25e-4 # 0.0025
print(f'fnum : {fnum}, {type(fnum)}') # print() 함수는 기본 floating 표기임

# 지수형의 + 표기는 생략되기도 함
fnum = 3e3 # 3000.0
print(f'fnum : {fnum}, {type(fnum)}')