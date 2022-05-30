# chap04_tuple.py
# 튜플(tuple) 자료형
# 리스트와 저장방식은 같음
# 여러 종류의 값들을 순차적으로 저장하는 자료형
# 리스트와 다른 점은 저장된 값은 변경할 수 없음

# 튜플 정의방법 1 : 소괄호() 로 정의
tpl_1 = ()
print(tpl_1, type(tpl_1))

# 튜플 정의방법 2 : tuple() 함수로 정의
tpl_2 = ()
print(tpl_2, type(tpl_2))

# 튜플도 리스트와 같이 인덱싱, 슬라이싱 연산 가능함
lst = [10, 20, 30]
tpl = (11, 22 ,33)
print(lst, type(lst))
print(tpl, type(tpl))

print('0번째 값: ', lst[0], tpl[0])
print('0~1번 인덱스까지 추출:', lst[0:2], tpl[0:2])
print('리스트 합치기 :', lst+lst)
print('튜플 합치기 :', tpl+tpl)

# 튜플과 리스트의 차이점 : 튜플은 값 변경 못 함
lst[2] = 77
print('lst :', lst)
# tpl[2] = 15 #error
# 실행시 에러가 발생하면, 아래쪽 코드는 실행되지 못함
print('tpl : ', tpl)

# 주의사항
# 튜플 생성시에 1개의 값만 가질때 반드시 값 뒤에 콤마(,) 표기할 것
tpl_3 = (1)
print(tpl_3, type(tpl_3))
tpl_4 = (1,)
print(tpl_4, type(tpl_4))
# 저장 데이터가 1개일때는 소괄호 생략해도 됨
tpl_5 = 2,
print(tpl_5, type(tpl_5))

#튜플 내장함수
# count() : 찾는 값의 갯수 조회
# 튜플변수.count(찾는값) =>  저장된 갯수 리턴됨
number_count = tpl.count(11)
print('tpl 에 저장된 숫자 11의 갯수 : ', number_count)

# index() :  찾는 값의 인덱스(순번) 조회
# 튜플변수.index(찾는값) => 찾는값이 있으면 index가 리턴됨
find_index = tpl.index(33)
print('tpl에 저장된 33의 위치:', find_index)
# print('tpl에 저장된 55의 위치:', tpl.index(55))

# len(튜플변수) : 저장된 전체 데이터 갯수 조회
print(('tpl 에 저장된 데이터 갯수: ', len(tpl)))

# 참고사항 1 : () 없이 하나의 변수에 값 나열 대입하면 자동 튜플이 됨
x = 1, 2, 3