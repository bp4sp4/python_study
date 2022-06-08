# func_mission3.py
# 함수 실습문제 3

'''
함수 정의 :
    함수명 : person_security(pno)
    처리내용 : 슬라이싱 이용
    전달받은 주민번호 첫자리부터 8글자 추출하고, 나머지 뒤 6자리는 ******로 처리한 다음 결과값 리턴
함수 실행 : enroll()
    try: except: finally: 로 구현하시오
    => 이름과 주민등록번호를 입력받음
    이름 : 홍길동 (name :str)
    주민등록번호 : 781225-1234567
함수로 전달해서 781225-1****** 형식으로 만들어서 리턴받음
=> 출력처리 : 이름 : 홍길동 주민번호 : 671225-1******
'''

def person_security(pno):
    return pno[0:8] + '******'

def enroll():
    try:
        name = str('이름 :')
        person_no = input('주민등록번호 :')
        print(f'이름 :{name}, 주민번호 :{person_security(person_no)}')
    except Exception as msg:
        print('에러발생', msg)
    finally:
        print('회원 정보 등록 끝')

        if __name__ == '__main__':
            enroll()