import common.oracle_db as oradb


def select_all():
    conn = oradb.connect()
    query = "select * from notice"
    result = []
    cursor = ''
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception as msg:
        print("select_all() 쿼리 실행 에러 : ", msg)
        return result  # 빈 리스트가 리턴됨
    finally:
        cursor.close()
        oradb.close(conn)

    return result


def insert(tp_value):
    conn = oradb.connect()
    query = "insert into notice values (seq_notice.nextval,\
           :1, :2, :3, :4, :5, '', :7)"
    cursor = ''

    try:
        # employee 테이블에 새 행 추가 처리
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        oradb.commit(conn)
    except Exception as msg:
        print("insert() 쿼리 실행 에러 : ", msg)
        conn.rollback()
        return
    finally:
        cursor.close()
        oradb.close(conn)

    return
