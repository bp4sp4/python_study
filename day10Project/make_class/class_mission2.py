# class_mission2.py
# time 모듈을 이용해서, 클래스의 객체 생성시간 - 소멸시간 출력

# import 시에 모듈이 가진 함수만 선택해서 임포트할 수 있음
# from 모듈명 import 함수명, 함수명, ...
from time import  ctime, sleep

# 클래스 정의
class Life:
    def __init__(self):
        # 파이선에서는 필드를 따로 선언하지 않고
        # 메소드 안에서 self.변수명을 사용하면 자동 필드가 됨
        self.create_time = ctime()
        print('인스턴스 생성 시간 :', self.create_time)

    def __del__(self):
        print('인스ㅓㄴ스 소멸 시간: ', ctime())

# 실행 함수 정의
def test():
    mylife = Life()
    print('sleeping for 5 second...')
    sleep(5)

#함수 실행
test()
print('프로그램 실행 종료')