# class_mission1.py
# 클래스 실습문제
'''
클래스 작성 : 클래스명은 book
클래스 멤버변수 : 기본 private 처리함
    title = '제목없음'
    author = '작자미상'
    price = 0
    text = 0.05
매개변수 없는 기본생성자와 기본소멸자 작성함
클래스 멤버함수 :
    info() => 필드 값들을 하나의 문장으로 만들어서 리턴함. format() 활용
    각 필드에 대한 set_필드명() => 전달받은 값으로 변경하도록 처리
    각 필드에 대한 get_필드명() => 해당 필드값 리턴 처리
클래스 사용 :
    => Book 클래스에 대한 객체 생성
    => 레퍼런스를 이용한 set 메소드로 객체의 필드값 변경하고
    => info() 메소드 출력 확인
    => get 메소드 이용해서 도서가격과 할인율이 적동된 도서금액을  계산
    = get 메소드 이용해서 도서가격과 할인율이 적용된 도서금액을 계산 출력
    도서금액 = 도서가격 + (도서가격 * 부가세율)
'''

class Book:
    __title = '제목없음'
    __author = '작자미상'
    __price = 0
    __tex = 0.05
    def __int__(self):
        print('Book 클래스 기본생성자 작동됨')

    def __del__(self):
        print('Book 클래스 인스턴스 작동됨')

    def info(self):
        return '도서제목 : {}, 저자 : {} , {}원, 부가세 : {} %'\
            .format(self.__title,self.__author,self.__price,self.__tex)

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def set__tex(self, tex):
        self.__tex = tex

    def get_author(self):
        return  self.__author

    def get_price(self):
        return  self.__price

    def get_tex(self):
        return  self.__tex

    bref = Book()
    print(bref.info())
    print(Book.info(bref))

    bref.set_title('파이썬 내꺼 만들기')
    bref.set_author('홍길동')
    bref.set_price(35000)
    bref.set_tex(0.1)

    print(bref.info)

    bookPrice = bref.get_price() + (bref.get_price() * bref.get_tex())
    print('도서금액 : ', bookPrice)
    

