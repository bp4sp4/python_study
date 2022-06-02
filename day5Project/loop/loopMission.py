# loopMission.py
# 반복문 실습문제


'''
키보드로 문자열을 입력받아서, 요구대로 처리하고 출력되게 하시오.
실행 :
문자열 입력 : apple ( value :str)
 처리내용  
    for 문 사용 : 글자의 유니코드 출력이 반복되게함
'''

def practice1():
    value = input('문자열 입력 :')
    for st in value:
        print(f'{st} 문자의 유니코드는 {ord(st)}이다.')