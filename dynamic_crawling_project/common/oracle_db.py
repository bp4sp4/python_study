# common.oracle_db.py
# common(공통) 패키지에 오라클 연동 모듈 정의

# 패키지 설치 확인 후 임포트 사용함
import cx_Oracle

# 연결 값 저장용 사용자 정의 변수 (전역변수)
dbURL = 'localhost:1521/xe'
dbUSER = 'c##student'
dbPASSWD = 'student'

def oracle_init():  # 애플리케이션에서 딱 한번만 구동시키면 됨
    cx_Oracle.init_oracle_client('C:\instantclient_21_6')

def connect():
    try:
        conn = cx_Oracle.connect(dbUSER, dbPASSWD, dbURL)
        conn.autocommit = False
        return conn
    except Exception as msg:
        print('오라클 연결 에러 : ', msg)

def close(conn):
    try:
        if conn:  # conn 이 None 이 아니면 (True 이면)
            conn.close()
    except Exception as msg:
        print('오라클 연결 해제 에러 : ', msg)
        
def commit(conn):
    try:
        if conn:  # conn 이 None 이 아니면 (True 이면)
            conn.commit()
    except Exception as msg:
        print('트랜잭션 커밋 에러 : ', msg)
        conn.rollback()  # 커밋 실패시 롤백 처리
        
def rollback(conn):
    try:
        if conn:  # conn 이 None 이 아니면 (True 이면)
            conn.rollback()
    except Exception as msg:
        print('트랜잭션 롤백 에러 : ', msg)

