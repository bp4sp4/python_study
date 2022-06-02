# ifelse_missoion2.py
# if else 실습문제
'''
키브드로 나눌값과 나누기할 수를 입력 받아 계산해서 출력하시오
입력내용 :
    나눌 값 : 25 (value : int)
    나누기할 수 : 0 (div_num : int)
처리 내용 :
    조건 처리 나누기할 수가 0이 아니면 계산해서 몫과 나머지 출력함
    나누기할 수가 0이면 '0으로 나눌 수 없습니다.' 출력
마지막 출력구문 : if 문과 별개의 구문
    프로그램이 종료되었습니다.
컴퓨터는 0 나누기 못함

'''
def practice2():
    value = int(input('나눌 값 :'))
    div_num = int(input('나누기할 수 : '))

    if (div_num != 0):
        print('몫 : {}'.format(value // div_num))
        print('나머지 : {}'.format(value % div_num))
    else:
        print('0은 나누기할 수 없습니다.')
    print('프로그램이 종료되었습니다.')