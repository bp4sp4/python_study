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