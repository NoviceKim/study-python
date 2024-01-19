import pymysql
from pymysql.cursors import Cursor


# 원하는 MySQL 서버와 연동하는 함수
def connect():
    conn = pymysql.connect(host='3.38.101.83', user='mysql', password='1234', db='test', charset='utf8', autocommit=False)
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    return conn, cursor


# CRUD: save, find_all, find_by_id, update, delete 중, 한 가지 함수가 인자로 들어옴
def execute(crud):
    result = None

    def manage(*args):
        nonlocal result
        conn, cursor = connect()

        try:
            # CRUD 함수 실행, 이 때 cursor 객체를 함께 전달해 줌으로써 해당 쿼리가 실행되도록 함
            result = crud(cursor, *args)
            conn.commit()

        except Exception as e:
            print(e.__str__())
            conn.rollback()

        # CRUD 함수의 성공/실패 여부와 관계없이, cursor, conn을 닫음
        finally:
            cursor.close()
            conn.close()

        return result

    return manage
