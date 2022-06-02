# mission.py
# 다중 if 문 실습문자


'''
키보드로 학생이름 점수 입력받아 학점을 처리해서 출력하시오.
입력내용 :
    학생이름 : 홍길동(name:str)
    점수 : 78 (score:int)
처리 내용 :
    <조건 처리> : 점수에대한 등급 (grade :str) 처리
    점수가 90 이상 등급 A
    점수가 80 이상 90 미만 등급 B
    점수가 70 이상 80 미만 등급 C
    점수가 60 이상 70 미만 등급 D
    점수가 60 미만 등급 F
출력 내용 :
    홍길동으 점수는 78점 이고, 등급은 C입니다.
'''

def pratice4():
    name = str(input('학생이름 :'))
    score = int(input('점수 :'))
    grade = ['A','B','C','D','F']

    if(score >= 90):
        print(f'{name}의 점수는 {score}이고, 등급은 {grade[0]} 입니다.')
    elif(score >= 80 and score < 90):
        print(f'{name}의 점수는 {score}이고, 등급은 {grade[1]} 입니다.')
    elif (score >= 70 and score < 80):
        print(f'{name}의 점수는 {score}이고, 등급은 {grade[2]} 입니다.')
    elif (score >= 60 and score < 70):
        print(f'{name}의 점수는 {score}이고, 등급은 {grade[3]} 입니다.')
    else:
        print(f'{name}의 점수는 {score}이고, 등급은 {grade[4]} 입니다.')
# 방법2
#     if (score >=90):
#      grade = 'A'
#     elif(score >=80):
#      grade ='B'
#     elif (score >= 70):
#      grade = 'B'
#     elif (score >= 60):
#      grade = 'B'

# 중첩 if 실습문제

'''
정수 두 개를 키보드로 입력받아 요구조건대로 계산처리
입력내용 :
    첫번째수  num2 : int
    두번째 num2 : int
처리 내용 :
    조건 1 : 두수 모두 양수여야함
    조건 2 : 두수 모두 양수이면, 1~100 사이의 값인지 확인
    두수의 합 차,곱,몫 나머지 게산하여 출력함
    1~100 사이의 값이 아니면, `1~100 사이의 값만 입력하세요.' 출력
    양수가 아니면, '양수만 입력해야합니다. 출력
    조건문 종료되면 '프로그램이 종료되었습니다. 출력함
마지막 출력구문 : if 문과 별개의 구문
    프로그램이 종료되었습니다.
'''
def practice5():
    num1 = int(input('첫번째 수 :'))
    num2 = int(input('두번째 수 :'))
    if (num1 > 0 and num2 >0):
        if(num2 <= 100 and num2 <= 100):
            print('{} + {} = {}'.format(num1, num2, num1 + num2))
            print('{} - {} = {}'.format(num1, num2, num1 - num2))
            print('{} * {} = {}'.format(num1, num2, num1 * num2))
            print('{} // {} = {}'.format(num1, num2, num1 // num2))
            print('{} % {} = {}'.format(num1, num2, num1 % num2))
        else:
            print('1~100사이의 값만 입력하세요')
    else:
        print('양수만 입력해야 됩니다.')
    print('프로그램이 종료되었습니다.')
