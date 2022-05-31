# test_set\set_sample.py
# 모듈로 표현 : test_set.set_sample

# 집합(set) 자료형
# 교집합, 합집합, 차집합 연산 가능한 자료형임
# 수학적 논리 개념을 이용 : 비트논리연산자 사용 (&, |)
# 저장방식은 자바의 Set 과 유사함
# 같은 값 중복 저장 안됨 => 중복값 제외에 이용할 수 있음
# 저장 순서가 없음 => 인덱스(저장 순번)가 없음

# set 객체 생성 (set 정의 방식) 1 : {} 사용
def test1():
    set1 = {1, 2, 3, 4, 1, 2,}
    print(f'set1 : {set1}')

# set 객체 생성 (set 정의 방식) 2 : set() 함수 사용
def test2():
    set1 = set()
    print(set1, type(set1))

# set에 문자열을 저장하는 경우 : 문자 하나씩 저장됨
def test3():
    set1 = set('Hello') # 중복 저장 안 함 : 'l'이 한개만 저장됨
    print(set1, type(set1))

    set2 = set('python')
    print(set2, type(set2))

# set에 리스트 저장할 수 있음
# 리스트 자체는 값 순서대로 저장됨
# => set 이 저장순서를 유지하게 하는 방법으로 이용함

def test4():
    set1 = set([1,2,3,4,5,6,7,8])
    print(set1, type(set1))

# set 자료형은 집합 연산 가능함 : 합집합, 교집합, 차집합
def test5():
    set1 = set([1,2,3,4,5,6,7,8])
    print(set1, type(set1))
    set2= set([4,5,6,7,8,9,10])
    print(set2, type(set2))

    #교(곱)집합 : & 연산자 또는 intersection() 함수 사용
    print('set1 & set2 : ', set1 & set2)
    print('intersection : ', set1.intersection(set2))

    #합집합 : | 연산자 또는 union() 함수 사용
    print('set1 | set2 : ', set1 | set2)
    print('union : ', set1.union(set2))

    #차집합 : - 연산자 또는 differenc() 함수 사용
    print('set1 - set2 : ', set1 - set2)
    print('difference : ', set1.difference(set2))

# 값 추가, 삭제 가능함
def test6():
    set1 = set([1, 2, 3, 4, 5, 6, 7, 8])
    print(set1, type(set1))

    # 값 1개 추가 : ad()
    set1.add(12)
    print(set1, type(set1))
    # 값 여러 개 추가 : update(리스트)
    set1.update([34])
    print(set1, type(set1))
    # 값 삭제 : remove()
    set1.remove(8)
    print(set1, type(set1))
# list 의 값 중복을 제거할 떄, set 을 이용할 수 있음
def test7():
    list1 = [1, 1, 1, 2, 2, 2 ,2, 3, 4, 4, 4, 5, 5, 5]
    set1 = set(list1)
    print(set1, type(set1))
    

    list1 = [set1]
    print('list1: ',list1, type(list1))

