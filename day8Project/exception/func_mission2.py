# func_mission2.py
# 함수 만들어 사용하기 실습문제 2
'''
함수 정의 :
    함수 이름 : find_chr(문자열, 찾을문자)
    함수 처리 내용 : 반복문으로 문자열 안에서 글자를 하나씩 꺼내서
    찾을문자와 일치하는지 확인하고 카운트함
    카운트한 갯수를 리턴함
함수 실행 : func_string()
        try: except: finally: 로 구현하시오
        키보드로 문자열 입력받고, 찾을 문자 하나를 입력받음
        문자열 : apple
        찾을 문자 : p
        함수로 두 개를 전달해서, 문자 안에 포함된 찾을문자의 갯수를 리턴받음
        결과 출력 확인 => apple 에 p 가 2개 들어있었습니다.
'''

def find_chr(values, chr):
    count = 0
    for ch in values:
        if ch == chr:
            count += 1
        return count

def func_string():
    try:
        st = input('문자열 :')
        ch = input('찾을 문자 :')
        print(f'{st}에 {ch}가 {find_chr(st, ch)}개 포함되어 있스빈다.')
    except Exception as msg:
        print('에러 발생 :', msg)
    finally:
        print('문자 관련 함수 연습 끝')


if __name__ == '__main__':
    func_string()