# loopMission.py
# 반복문 실습문제


'''
키보드로 문자열을 입력받아서, 요구대로 처리하고 출력되게 하시오.
실행 :
문자열 입력 : apple ( value :str)
 처리내용  
    for 문 사용 : 글자의 유니코드 출력이 반복되게함
'''

# def practice1():
#     value = input('문자열 입력 :')
#     for st in value:
#         print(f'{st} 문자의 유니코드는 {ord(st)}이다.')
# 키보드로 구구단의 단수를 입력 받아서, 해당 단의 구구단을 출력하시오.
# 입력내용 :
'''
단수 : 3 (dan :int)
출력내용 3 *1 = 3
        3 * 2 =6
'''

def for_sum():
    dan = int(input('단수 :'))
    for su in dan(1, 10):
        print(f'{dan} * {su} = {dan * su}')