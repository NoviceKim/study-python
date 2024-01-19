from connection_module import *


# save 기능 함수 제작 - connection_module 에 있는 execute()를 데코레이터로 사용
@execute
def save(cursor: Cursor, query: str, params: tuple):
    cursor.execute(query, params)


@execute
def save_many(cursor: Cursor, query: str, params: tuple):
    cursor.executemany(query, params)


@execute
def find_all(cursor: Cursor, query: str):
    cursor.execute(query)
    return cursor.fetchall()


@execute
def find_all_by(cursor: Cursor, query: str, params: tuple):
    cursor.execute(query, params)
    return cursor.fetchall()


@execute
def find_by_id(cursor: Cursor, query: str, params: tuple):
    cursor.execute(query, params)
    return cursor.fetchone()


@execute
def update(cursor: Cursor, query: str, params: tuple):
    cursor.execute(query, params)


@execute
def delete(cursor: Cursor, query: str, params: tuple):
    cursor.execute(query, params)