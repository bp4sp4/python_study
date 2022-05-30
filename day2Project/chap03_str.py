# chap03_str.py
# 파이선에서 문자열 다루기

# 파이선에서 문자열(str)은 시퀀스(sequence : 순차자료형)로 취급됨
# 시퀀스 자료형은 값의 순번(인덱스, index)이 매겨짐. 0부터 시작됨

# 문자 선택 연산자 (인덱싱) : 문자변수[인덱스순번]
ss = 'Hi,-python'

print('첫번째 글자 : ', ss[0])
print('다섯번째 글자(인덱스 4) : ', ss[4])
print('뒤에서 첫번째 글자 : ', ss[-1])

# 문자열 범위 선택 연산자 (슬라이싱) : 문자열값 부분 추출시 사용
# 문자변수[시작인덱스:끝인덱스-1:간격]
print(ss[0:3]) # 0, 1, 2번째 3글자 추출
print(ss[0:5:2])

# 슬라이싱을 이용해서 문자열을 역순으로 정렬
print(ss)
print(ss[::-1])  # 간격을 음수로 지정함

# 슬라이싱과 연결연산 혼합 사용 가능함
n1 = 'abcdef'
n2 = '12345'
n3 = n1[0:3] + n2[1:]
print(n3)  # abc2345

# 문자열 반복 연산자 : *
print('Hello!' * 3)

# 문자 처리 내장함수
# upper(), lower() : 영문자일때 대/소문자로 변환함수
tt = 'apple'
print(tt)
# 파이선에서는 기록된 문자값은 변경할 수 없음
#tt[1] = 'b'  # error
# 해결 : 제공되는 관련 함수를 사용하면 됨
print(tt.upper())

tt2 = 'BANANA'
print(tt2.lower())

# swapcase(), capitalize()
tt3 = 'tEst stR pyTHOn'
print(tt3)
print(tt3.swapcase())  # 소문자는 대문자로, 대문자는 소문자로 변환 함수
print(tt3.capitalize())  # 문장의 첫 글자를 대문자로 변환, 나머지는 소문자로

# title() : 각 단어의 첫글자를 대문자로 변환
print(tt3.title())

# strip(), lstrip(), rstrip()
tt4 = '      test str values     '
print('|', tt4, '|', sep='')
print('|', tt4.strip(), '|', sep='')  # strip() : 문자 앞뒤의 공백 제거함
print('|', tt4.lstrip(), '|', sep='')  # lstrip() : 문자 앞(왼쪽)의 공백 제거함
print('|', tt4.rstrip(), '|', sep='')  # rstrip() : 문자 뒤(오른쪽)의 공백 제거함

# split(), splitlines()
tt5 = 'abc-def-ghi-j'
print('tt5 : ', tt5)
print(tt5.split('-'))  # split() : 지정하는 문자를 기준으로 문자값을 분리함
# 여러 개의 문자들로 분리됨 => 리스트 형식이 됨

# splitlines() : 줄(line) 단위로 분리해서 리스트를 리턴함
tt6 = '''python
java
javascript
c++'''
print(tt6)
print(tt6.splitlines())

# index(), find() : 글자 위치(순번 : 인덱스) 조회
print(tt5.index('e'))  # 문자열 안에 있는 'e' 문자의 위치 조회
# 없는 문자를 조회하면 에러남
# print(tt5.index('k'))

print(tt5.find('e'))   # 찾아낸 문자의 위치를 리턴
print(tt5.find('k'))   # 없는 문자 조회시에는 -1 리턴함

# 이외의 다른 문자 관련 함수 조회하려면
print(dir(str))

# 문자열에 포맷(format)을 적용하여 코드 작성하는 방법
# 문자열 값 사이에 다른 종류의 값이나 변수를 적용하려고 할 때 이용
amount = int(input('갯수 입력 : '))
st = '나는 사과를 %d 개 주문하였음' %amount
print(st)

# 정수 10진수 (decimal) : %d
# 문자열 (string) : %s
# 실수형 숫자 (float) : %f
product_name = input('주문할 상품명 : ')
price = int(input('제품의 단가 : '))

st2 = '상품명은 %s 이고, 기본 단가는 %d 이다.' %(product_name, price)
print(st2)







