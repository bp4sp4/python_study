# 패키지 설치하고 임포트 선언
import cx_Oracle

# 사용자 정의 변수
dbURL = "localhost:1521/xe"
dbUSER = "c##student"
dbPASSWD = "student"

# 각 기능별 함수 정의
# 오라클 드라이브 초기 등록 설정 함수
def oracle_init():
    cx_Oracle.init_oracle_client(lib_dir="C:\instantclient_21_6")

# 오라클 연결 함수
def connect():
    try:
        conn = cx_Oracle.connect(dbUSER, dbPASSWD, dbURL)
        conn.autocommit = False   # 자동 커밋 해제
        return conn
    except Exception as msg:
        print("오라클 연결 에러 : ", msg)

# connection close 함수
def close(conn):
    try:
        conn.close()
    except Exception as msg:
        print("오라클 연결 해제 에러 : ", msg)

# commit 함수
def commit(conn):
    try:
        conn.commit()
    except Exception as msg:
        print("오라클 트랜잭션 커밋 에러 : ", msg)
        conn.rollback()  # 에러 발생시 취소됨