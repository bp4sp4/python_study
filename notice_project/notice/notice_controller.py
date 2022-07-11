import notice.notice_class as model


# model 의 select_all() 구동용 함수
def select_list():
    not_list = model.select_all()
    return not_list

def insert_emp(tp_value):
    model.insert(tp_value)
    print("새로운 공지가 등록되었습니다.")
    return


def update_emp(tp_value):
    model.update(tp_value)
    print("공지 정보가 변경되었습니다.")
    return

def delete_emp(tp_value):
    model.delete(tp_value)
    print("공지가 삭제되었습니다.")
    return

