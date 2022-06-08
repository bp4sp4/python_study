# mission2.py


'''
try except finally를 사용해서 예외 발생 처리 구문을 작성하시오.
실행 내용 :
    가로의 세로 크기를 입력받아서,
    사각형의 면적과 둘레를 계산해서 출력 처리
    가로와 세로 : 숫자형태로만 입력이 되어야 함
    => 입력받은 가로, 세로는 int 형으로 바꾸고 계산에 사용함
    => 사각형의 면적 : 가로 * 세로
    => 사각형의 둘레 : 2 * (가로 + 세로)
예외 처리 :
    입력 받은 가로, 세로가 숫자 형태가 아닐때
    '숫자만 입력해야 됩니다.' 출력함
'''
from Tools.scripts.which import msg


def calulator():
    try:
        width = int(input('가로 :'))
        height = int(input('세로 : '))
        print(f'사각형의 가로 : {width}, 세로 : {height}')
        print(f'사각형의 면적 : {width * height}')
        print(f'사각형의 둘레 : {2 * (width + height)}')
    except:
        print('숫자만 입력해야합니다.')
    finally:
        print('도형 계산 처리 종료')

def calulator2():
        try:
            width = int(input('가로 :'))
            height = int(input('세로 : '))
        except:
            print('숫자만 입력해야합니다.')
        else:
            print(f'사각형의 가로 : {width}, 세로 : {height}')
            print(f'사각형의 면적 : {width * height}')
            print(f'사각형의 둘레 : {2 * (width + height)}')
        finally:
            print('도형 계산 처리 종료')

if __name__ == '__main__':
    calulator2()