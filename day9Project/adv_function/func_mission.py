# func_mission.py
# 재귀함수, 람다함수, 내장함수 실습문제
def fectorial(n):
    if n == 0:
        return 1
    else:
        return n * fectorial(n-1)
# 1. 재귀함수()
def test1():
    try:
        num = int(input('정수 입력 : '))
    except:
        print('정수만 입력하세요.')
    else:
        print(f'{num}! : {fectorial(num)}')
    finally:
        print('test1 --the end--------------')
# 2. 람다함수()
def test2():
    try:
        num = int(input('정수 입력 :'))
    except:
        print('정수만 입력하세요.')
    else:
        print(f'{num}! : {(lambda n: n ==0 and 1 or n * fectorial(n-1))(num)}')
    finally:
        print('test2 --the end--------------')

def test3():
    try:
        num = int(input("정수 입력 : "))
    except:
        print('정수만 입력하세요.')
        result = 1
        for n in range(num, 0, -1):
            result *= n
        print(f'{num}! : {result}')
    finally:
        print('test3 --the end--------------')
def test4():
    print([dan * su for dan in range(2, 10) for su in range(1, 10)])

def test5():
    print([(lambda x,y : '{} x {} = {} '.format(x, y, x * y,))(x,y) for x in range(2,10) for y in range(1, 10)])

# def test_func(a):
    # if a > 10:
    #     return 'a가 10보다 크다'
    # else:
    #     return 'a가 10보다 작거나 같다.'
def test6():
    print((lambda a: 'a가 10보다 크다.' if a > 10 else 'a가 10보다 작건다 같다.')(14))
    
# def test_func2(a):
#     ls = []
#     for i in range(a):
#         ls.append(i ** 2)
#         return  ls
    
def test7():
    print(list(map(lambda a: a**2, range(5))))
    # map() 과 람다함수 사용

    




# 함수 실행 --------------------------------
def func_mission():
    prompt = '''
    ***** 함수 활용 테스트 *****
    1. 재귀함수 : 입력받은 정수의 펙토리얼 구하기
    2. 람다함수 : 입력받은 정수의 펙토리얼 구하기
    3. 반복문 사용 : 입력받은 정수의 펙토리얼 구하기
    4. 리스트 내포 : 구구단 2단~9단까지 곱하기 결과 저장 출력
    5. 람다함수 리스트 내포 : 구구단 2단~9단까지 곱하기 결과 출력
    6. 람다 함수로 바꾸기 실습
    7. map() 함수와 람다함수 사용으로 바꾸기 실습
    0. 끝내기
    '''
    while True:
        try:
            print(prompt)
            no = int(input('번호 선택 :'))
        except:
            print('숫자만 입력하세요.')
        else:
            if no == 1:
                test1()
            elif no == 2:
                test2()
            elif no == 3:
                test3()
            elif no == 4:
                test4()
            elif no == 5:
                test5()
            elif no == 6:
                test6()
            elif no == 7:
                test7()
            elif no == 0:
                break
            else:
                print('잘못 입력하셨습니다.')
        finally:
            print('함수 활용 테스트 종료.')




# 실습문제 실행 테스트 -----------------
if __name__ == '__main__':
    func_mission()