#sample_module.py
# 파이선에서 모듈 만들어서 사용하기
#
# 모듈(module) : 파이선 소스 파일(파일명.py) 이다.
# 파일명이 모듈명이 됨
# 모듈용 소스파일에는 함수와 변수가 저장되면 됨
# 모듈이 제공하는 함수와 변수를 사용하려면, import 모듈명 선언하면 됨
# import 후에 모듈명,함수명() 또는 모듈명, 변수명 으로 사용하면 됨

import keyword
# keyword.py 파일을 의미함

# print(keyword.kwlist) # 예약어 리스트 출력

# 모듈은 다른 파이선 파일에서 사용할 수 있도록 함수(기능)와 변수(값)들을
# 따로 저장해서 제공하는 목적의 소스 파일이다.
#
# 모듈 임포트시에 모듈명에 대한 줄임말을 같이 선언할 수도 있음

import keyword as k
print(k.__file__) # 해당 모듈(파일)의 위치가 출력됨

# help('modules') #현재 설치되어 있는 모듈 확인

# 모듈 활용법 확인 : help('모듈이름')
help('random')



import time # 날짜나 시간 관련 기능 제공

print(time.localtime()) # 현재 날짜와 시간정보 출력
time.sleep(1) # 1초 멈춤
print(time.localtime())

import random # 임의의 숫자를 발생시키는  기능 제공
print(random.random()) # 0.0 <= 임의의 난수 < 1.0
print(random.randint(1, 5)) # 1 <= 임의의 정수 < 5
print(random.randrange(1, 10, 2)) # 1 <= 2간격의 정수 하나 <10

import  math # 수학 계산
print('원주율 : ', math.pi)
print('5! : ', math.factorial(5))

import calendar

calendar.prmonth(2022,11)

# --------------------------------------------------------------
# 사용자 wjddml 모듀 ㄹ사용하기
import mymodule as my
print('더하기 :', my.sum(10, 20))
print('빼기 :', my.sum(15, 7))
print('곱하기 :', my.mul(10, 20))
print('나누기한 몫 :', my.divide(12, 3))
try:
    print('나누기한 몫 :', my.divide(12, 0))
except Exception as msg:
    print(msg)
    pass
print('나누기한 나머지 :', my.divide(12, 7))
try:
    print('나누기한 나머지 :', my.divide(12, 0))
except Exception as msg:
    print(msg)
    pass
print('가장 큰 값 :', my.max())
print('가장 큰 값 :', my.max(10))
print('가장 큰 값 :', my.max(1, 3,4,5,6,7,8,9,4,2))
print('가장 큰 값 :', my.min())
print('가장 큰 값 :', my.min(10))
print('가장 큰 값 :', my.min(13,5,4,6,7,9,4,6))
print('글자 갯수 :', my.strlen())
print('가장 큰 값 :', my.strlen('module test'))
# print('원주율 : ', my.pi)
# print('카운트 : ', my.count)

# __name__: 현재 실행되고 있는 있는 모듈 이름 확인할 때 사용함
print(__name__) # __main__출력됨
# 프로그램을 실행하면, 기본파일은 main 모듈이 됨
# 다르게 표현하면, main만 실행할 수 있다는 의미임

if __name__ == '__main__':
    print('이 파일(모듈)이 직접 실행이 되면, 자동 메인이 됨')
    
# 파이선에서는 소스파일을 직접 실행시키면 자동으로 해당 소스파일일을
# __main__ 모듈로 설정하는 것을 확인할 수 있음