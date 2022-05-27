# chap02_input.py

# 파이선에서 실행시 키보드로 값 입력받기
# input() 함수 사용함
# 변수이름 = input('입력을 위한 메세지 문장')

# 입력을 위한 메세지 없이 실행 테스트
# num = input()
# num = input('숫자를 입력하세요 :')
# print('num:', num)
# print('num 에 저장된 값의 종류 : ', type(num))
# 파이선의 input() 함수로 입력되는 값은 모두 문자형(str) 이다.
# print('더하기 확인 :', num+100) # 숫자와 문자는 계산할 수 없음

# 숫자형으로 바꾸고자 한다면,
# 정수는 int('정수문자'), 실수는 float('실수문자') 함수 사용함

# int_num = int(num)
# print('int_num :', int_num, type(int_num))
# print('더하기 확인 : ', int_num + 100)
# fst = int(input('첫번째 정수:'))
# sed = int(input('두번째 정수: '))
#
# print(fst, '+', sed, '=', (fst + sed))
# print(fst, '-', sed, '=', (fst - sed))
# print(fst, '*', sed, '=', (fst * sed))
# print(fst, '//', sed, '=', (fst // sed))
# print(fst, '%', sed, '=', (fst % sed))
# print(fst, '**', 2, '=', (fst **2))
# print(sed, '**', 2, '=', (sed **2))

'''
이름 str 나이 int 성별(str 남|여로 입력) 키: float 몸무게 float
홍길동은 27세 남자이고, 키는 186.5cm 몸무게는 72kg 입니다.
'''

name = str(input('이름:'))
age = int(input('나이:'))
gender = str(input('성별 [남/여] :'))
stature = float(input('키:'))
weight = float(input('몸무게:'))
# print(name,'은',age,'세',gender,'자이고','키는',stature,'cm','몸무게는',weight,'kg입니다')

print('{}은 {}세 {}자이고, 키는 {}cm 몸무게는 {}kg 입니다.'.format(name,age,gender,stature,weight))
print('{0}은 {1}세 {2}자이고, 키는 {3}cm 몸무게는 {4}kg 입니다.'.format(name,age,gender,stature,weight))
