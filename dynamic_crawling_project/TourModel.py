# TourModel.py
# 오라클 db에 Tour 객체 정보 CRUD 처리 클래스

import common.oracle_db as oradb

class TourModel:
    # field
    conn = ''

    # constructor
    def __init__(self):
        oradb.oracle_init()  # 드라이브 등록
        self.conn = oradb.connect()  # 수업용계정 연결

    # 소멸자 (destructor)
    def __del__(self):
        if self.conn:  # 연결상태라면
            oradb.close(self.conn)  # 수업용계정 연결 해제

    # method
    # insert method
    def db_insert_tour(self, tour_tuple):
        query = "insert into tour values (seq_tour.nextval,\
                :1, :2, :3, :4, :5, :6, :7)"
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.conn.cursor() as cursor:
                cursor.execute(query, tour_tuple)
            oradb.commit(self.conn)
        except Exception as msg:
            oradb.rollback(self.conn)
            print('insert tour 에러 : ', msg)
        
    # select all method
    def db_selectall_tour(self):
        query = "select * from tour"
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.conn.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        except Exception as msg:
            print('selectall tour 에러 : ', msg)

    # select one method
    def db_selectone_tour(self, tp_value):
        query = "select * from tour where tour_id = :1"
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.conn.cursor() as cursor:
                cursor.execute(query, tp_value)
            return cursor.fetchone()
        except Exception as msg:
            print('selectone tour 에러 : ', msg)

    # delete all method
    def db_deleteall_tour(self):
        query = "delete from tour"
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.conn.cursor() as cursor:
                cursor.execute(query)
            oradb.commit(self.conn)
        except Exception as msg:
            oradb.rollback(self.conn)
            print('deleteall tour 에러 : ', msg)

# TourModel ---------------------------------------