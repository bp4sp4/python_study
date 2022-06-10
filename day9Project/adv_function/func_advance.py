# func_advance.py
# 함수의 활용

# 재귀함수 (재귀적 호출 함수 : Recursive call function)
# 함수 안에서 자신을 호출(실행)하는 함수 (반복문과 유사함)
# 무한루프가 되지 않도록 종료 조건을 반드시 기술해야 함
# 파이선은 무한루프에 빠지면 자동으로 일정구간 반복 후에 에러 발생시킴

# fectorial 구하는 함수 만들기 : 재귀 함수 적용
def fectorial(n):
    k = int(input("입력 받을 정수 :"))
    if n ==0 :
        return 1
    return  n * fectorial(n-1)




if __name__ == '__main__':
    print('\n10! : ', fectorial(10))