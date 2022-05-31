# test_dict/dict_sample.py
# 모듈로 표현 : test_dict.dict_sample

# 사전(dict) 자료형
# 자바의 Map 과 비슷하게 key 와 value 를 쌍으로 저장하는 구조임
# dict 에서는 키는 변겨오디지 않는 값이어야 함 (키는 지정하면 변경할 수 없다.
# => tuple 을 사용할 수 있음
# dict에 저장하는 value는 모든 자료형 데이터 가능함

# dict 정의 방법 1 : dict() 함수 사용
def test1():
    dict1 =dict()
    print(dict1, type(dict1))

# dict 정의 방법 2 : {} 중괄호 사용
def test2():
    dict1 = {}
    print(dict1, type(dict1))

# dict 에 값 저장 방식 : 키 : 값 쌍으로 지정 표기함
def test3():
    dict1 = {'a' : 1, 'b':2, 'c':3}
    print(dict1, type(dict1))
# list 나 tuple 처럼 인덱스로 값 조회, 변경할 수 없음 : 인덱스 없음
# 키(key)를 이용해서 값 변경, 조회함 : 사전변수[키]
def test4():
    dict1 = {1: 'python', 'a': [1,2,3], (1,2): 123}
    print(dict1, type(dict1))

    # 값 변경 : 사전변수[키] = 바꿀값
    # 저장된 키만 사용해야함
    dict['a'] = 777
    print(dict1, type(dict1))

    # 값 추가 : 사전변수[키] = 값
    # 저장되어 있지 않은 키 사용해야 함
    dict[3] = [11,22,33]
    print(dict1, type(dict1))
    
    # 값 조회 : 사전변수[키]
    # 주의 : 없는 키로 조회하면 KeyError 발생함
    print(dict1['c'])

# dict 내장함수 활용
def test5():
    dict1 = {
        'a': 10,
        'b': 25,
        'c': 77
    }
    print('dict1:', dict1, type(dict1))

    # 키에 대한 리스트 만들기 : keys() 함수
    print('dict1 의 키 목록 :', dict1.keys())

    # 값에 대한 리스트 만들기 : values()함수
    print('dict1 의 값 목록', dict1.values())
    # (키, 값) 을 item 이라고 함, 아이템을 리스트 만들기 : items() 함수
    print('dict1 의 아이템 목록 :', dict1.items())

# dict 에 저장된 키 또는 값들을 리스트로 바꾸기
def test6():
    dict1 = {
        'a': 10,
        'b': 25,
        'c': 77
    }
    print('dict1:', dict1, type(dict1))

    dict_keys = list(dict1.keys())
    print('키 리스트 :', dict_keys)
    dick_values = list(dict1.values())
    print('키 리스트 :',dict1.values ())

# 사전과 사전을 합치기 : update() 함수
# 사전1.update(사전) : 사전1 이 변경됨
# 사전1과 사전2에 동일한 키가 있을 경우에는, 사전1의 키가 값을 변경함
def test7():
    dict1 = {'name': '갤럭시', 'price':120000, 'tex':0.1 }
    dict2 = {'content': '최신모델입니다.', 'pric':880000}
    print('dict1 :', dict1)
    print('dict2 :', dict2)

    dict1.update(dict2)
    print('dict1 :', dict1)
# dict 내장함수 2
def test8():
    dict1 = {'name': '갤럭시', 'price': 120000, 'tex': 0.1}
    print('dict1 :', dict1)
    # pop(key) 함수 : 해당 키에 대한  아이템을 꺼내면서 제거함
    dict1.pop('tex')
    print('dict :', dict1)

    # clear()함수 : 딕셔너리 안은 비움 (저장 아이템 전체 삭제)
    dict1.clear()
    print('dict1 :', dict1)

    dict2 = {'content': '최신모델입니다.', 'pric':880000}
    print('dict2 :', dict2)

    # copy() 함수 : 딕셔너리 객체를 새로 만들고, 값을 복사함
    dict3 = dict2.copy() #deep copy (깊은 복사
    print('dict3 :', dict3, id(dict3) )

    dd = dict2 # 주소복사 : 얇은 복사 (shallow copy)
    print('dd: ', dd,id(dd))
# dict 안에 키 또는 값이 존재하는지 확인 : in 사용
def test9():
    dict1 = {'name': '갤럭시', 'price': 120000, 'tex': 0.1}
    print('dict1 :', dict1)
    # 키 존재 여부 : 키 in 사전변수
    print('name 키가 존재하느냐?', 'name' in dict1)  # True
    print('content 키가 존재하느냐?', 'content' in dict1) # False

    # 값 존재 여부 : 값 in 사전변수.values()
    print('0.1값이 존재하느냐?', 0.1 in dict1.values()) # True
    print('880000 값이 존재하냐느?', 880000 in dict1.values()) # False

    # get(key) : 키로 값을 조회 == 사전변수[키]
    print('name :', dict1['name'], dict1.get('name'))
    dict1.pop('tex') # 아이템 제거
    # 없는 키 조회시 에러 발생
    # print('tex :', dict1['tex'])
    print('tex :', dict1.get('tex')) # None 리턴됨 (차이점)

    # del 사전변수[키]
    del dict1['name']
    print(dict1)