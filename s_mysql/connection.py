import pymysql
from pymysql.cursors import Cursor

# 서버 설정
# host에 들어가는 ip 주소만 바꾸면, 다른 사람 서버에 있는 DB에도 접속할 수 있다
# 단, aws에서 3306 포트로 보안 연결이 되어 있어야 함
conn = pymysql.connect(host='13.125.190.19', user='mysql', password='1234', db='test', charset='utf8', autocommit=False)

# 쿼리문 보내 줄 객체 설정
cursor = conn.cursor(pymysql.cursors.DictCursor)

# DB에 보낼 쿼리문 작성
# sql = "insert into tbl_member(email, password, name) values('kgh1234', '1234', '김광협')"

# # 위에서 만든 쿼리문 실행
# cursor.execute(sql)
#
# # 쿼리문 실행 확정
# conn.commit()

sql = "select email, password, name from tbl_member"

cursor.execute(sql)

# fetchall() - 서버 DB에 있는 모든 결과 데이터를 list 형태로 가져옴
# fetchone() - 서버 DB에 있는 첫 번째 결과 데이터를 list 형태로 가져옴
# fetchall() - 서버 DB에 있는 n개의 결과 데이터를 list 형태로 가져옴
# 가져온 list의 각 인덱스에는 dict 데이터가 {'컬럼명1': '내용1', '컬럼명2': '내용2', ...} 같은 식으로 들어있음
# 가져만 오기 때문에, 직접 보려면 print를 따로 써줘야 됨
print(cursor.fetchall())
conn.commit()

# 마지막에는 항상 커넥션 닫아줄 것
cursor.close()
conn.close()