# import common.oracle_db as oradb
import notice.notice_controller as ncontroll

def mn_display():
    prompt = """
    *** 회사 정보 관리 프로그램 ***

    1. 공지 천체 검색
    2. 공지 등록
    3. 공지 수정
    4. 공지 삭제
    0. 프로그램 끝내기    

    """

    while True:
        print(prompt)
        no = int(input("메뉴 번호 선택 : "))

        if no == 1:
            not_list = ncontroll.select_list()
            print("현재 전체 직원 수 : ", len(not_list))
            not_print(not_list)
        elif no == 2:
            not_list = not_employee()
            ncontroll.insert_emp(not_list)
        elif no == 3:
            ncontroll.update_emp(not_list())
        elif no == 4:
            empid = input('삭제할 공지 사번 : ')
            ncontroll.delete_emp((empid,))
        elif no == 0:
            print("프로그램을 종료합니다.")
            return
        else:
            print("번호가 잘못 입력되었습니다. 다시 입력하세요.")

def not_print(nlist):
    for emp in nlist:
        for col in emp:
            print(col, end=', ')
        print()

def not_employee():
    print('새로 등록할 직원 정보를 순서대로 입력하세요.')
    notice_no = int(input('공지번호 : '))
    notice_title = (input('공지제목 : '))
    notice_writer = (input('작성자아이디 : '))
    notice_date = (input('등록날짜: '))
    notice_content = input('공지내용 : ').upper()
    notice_upfile = (input('첨부파일 : '))
    readcount = int(input('조회수 : '))

    tp_value = (notice_no, notice_title, notice_writer, notice_date, notice_content, notice_upfile, readcount)

    return tp_value