# 경로 표현 : conditional\ifSample.py
# 모듈 표현 : conditional.ifSample

# 제어문 : 조건문, if 문 테스트

'''
제어문(처리문) : logic
=> 준비된 값의 계산 처리를 위해 사용되는 처리문장
=> 종류 : 조건문, 반복문, 분기문
=> 조건문 : 조건을 제시해서 결과가 참(True) | 거짓(False)이 나오게끔
        해서 결과에 따라서 처리내용이 다르게 작동되게 하는 구문
=> 반복(loop)문 : 반복되는 구간을 루프(loop)라고 함 - if 문
        반복 실행할 구문(들)을 원하는 횟수 또는 종료조건이 될 떄까지
        반복 실행되게 작성하는 구문 - for 문, while 문
=> 분기문 : 실행 순서를 중간 생략시키거나, 강제로 종료시키는 구문
        - continue 문, break 문
'''

# 조건문에서는 조건식(표현식 : expression) 작성이 중요함
# 조건표현식(계산식)은 반드시 결과가 참|거짓이 나오게끔 작성함
# 참 | 거짓의 값을 만드는 연산자 사용함 : 비교, 논리 연산자
# if 문, if ~else 문, if ~else if 문, else 문,

'''
if 조건식 : 
    조건식의 결과가 참(True) 일때 실행할 구문 (반드시 들여쓰기함)
    실행할 구문은 여러 개여도 됨
if (조건식) => 조건식은 ()로 묶어서 작성해도 됨
    결과가 참일때 실행할 코드 구문등
'''

# 조건문 작성형식 1 : if 만 사용할 조건문
def iftest():
    # if(True) +> True 이면 ㅏㅇ래의 내용이 실행됨
    if (False): # if가 False 이면 아래의 내용은 실행되지 않는다.
        print('if 조건이 참이면 실행됩니다.')
        print('여러 개의 구문을 순서 대로 착성합니다.')

    print('if 문이 종료되고 나서 실행할 구문입니다.')

    # if(True):
    # print('test') # IndentationError (들여쓰기 에러)

# if 의 조건식은 주로 값을 확인하거나, 값이 원하는 버뮈 안의 값인지 확인
# 입력받은 정수숫자가 1이냐?
def iftest2():
    num = int(input('정수 숫자 입력 :'))
    if(num == 1):
        print('num : ', num)
        
# 정수를 입력받아서, 짝수인지 확인
# 짝수 : 2의 배수를 말함. 2로 나눈 나머지가 0 인 수
# 홀수 : 2의 배수가 아닌 수, 2로 나눈 나머지가 1인 수
def testEven():
    num = int(input('정수 하나 입력 : '))
    if(num & 2 == 0):
        print(f'입력받은 {num}은 짝수이다.')

# 조건문 작성형식 2: if ~ else문
'''
if(조건식):
    참일때 처리내용
else:
    거짓일때 처리내용
'''
def testEven2():
    num = int(input('정수 하나 입력 : '))
    if(num % 2 == 0):
        print(f'입력받은 {num}은(는) 짝수이다.')
    else: # num % 2 == 1 또는  num % 2 !=0
        print(f'입력받은 {num}은(는) 홀수이다.')

# 정수를 입력받아서, 1부터 100 사이의 값이면 입력값의 제곱을 출력
# 해당 범위의 값이 아니면 '1~100 사이의 값만 입력하세요.' 출력
# 1<= 입력받은 값 <=100

def test_ifelse():
    num = int(input('정수 하나 입력 : '))
    if(num >= 1 and num <= 100):
        print(f'{num}의 제곱은 {num ** 2}')
    else:
        print('1이상 100이하의 값만 입력하세요.')


# in 연산자 : 군집 자료형형(list, tuple, dict, set)에 사용함
# 변수 또는 값 in 군집자료형변수 : x in s
# s 안에 x가 있느냐? 있으면 True, 없으면 False
# x not in s : s 안에 x가 없느냐? 없으면 True, 있으면 False

def test_in():
    print(2 in [1, 2, 3]) # True
    print(1 not in (1, 2, 3)) # False
    print('a' in 'abcdef') # True
    print('a' not in ('a', 'b', 'c')) # True

# 결재수단 중에 'money' 가 있으면, '5000원을 현금지불하셨습니다.' 출력
# 없으면 '다른 결재 수단을 선택하세요.' 출력
def checkPayment():
    payment = ['card', 'money', 'phone']
    price = 5000

    if('money' in payment):
        print(f'{price}원을 현금 지불하셨습니다.')
    else:
        print('다른 결재 수단을 선택 하세요.')

# 조건문 작성형식 3 : 다중 if 문
# if elif elif elif else
# if elif elfi elif
def checkPayment2():
    payment = ['결재수단', 'card', 'money', 'phone', 'zeropay']
    print('=================결재 수단 ==================')
    print('1. 카드')
    print('2. 현금')
    print('3. 핸드폰')
    print('4. 제로페이')

    no = int(input('결재수단에 대한 번호 입력 :'))
    price = 5000

    if(no == 1):
        print(f'{price}원을 {payment[1]}로 결재하셨습니다.')
    elif(no == 2): # no 가 1이 아니고 2냐
        print(f'{price}원을 {payment[2]}로 결재하셨습니다.')
    elif(no == 3): # no 가 1도,2도 아니고 3이냐
        print(f'{price}원을 {payment[3]}로 결재하셨습니다.')
    elif(no == 4): # no 가 1도,2도,3도 아니고 4냐
        print(f'{price}원을 {payment[4]}로 결재하셨습니다.')
    else:  # no 가 1도,2도,3도 아니고 4냐
        print('잘못 입력하셨습니다. 다시 입력하세요.')

# 중첩 조건문 : if 문 안에서 if 문 사용
def mulii_if():
    n1 = 10
    n2 = 20

    if n1 == 10:
        print(f'n1 : {n1}')
        if n2 == 20:
            print(f'n2 : {n2}')
        else:
            print('n2가 20 이 아니다.')
    else:
        print('n1은 10이 아니다.')
# 간단 if 문 :
# 변수 = 참일 때 실험내용 if 조건식 else 거짓일 떄 실행내용
def shortCondition():
    a = 3
    message = 'a is 1' if(a == 1) else 'a is not 1'
    print(message)

def shortCondition2():
    score = int(input('점수 입력 :'))
    result = '합격' if(score >= 60) else '불합격'
    print(result)














