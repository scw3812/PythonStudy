import cx_Oracle

# 오라클 접속 과정
# 1. con = cx_Oracle.connect(user, pw, host) -> 유저명, 비번, 호스트로 connection 만들기
# 2. cur = con.cursor -> 커서 객체 만들기
# 3. cur.execute(sql)로 sql문 실행하기
# 4. cur.fetchone()으로 테이블 한 줄씩 튜플로 얻기

user = "scott"
passwd = "tiger"
host = "localhost/xe"

con = cx_Oracle.connect(user, passwd, host)
print(con)

cur = con.cursor()
sql = "select deptno, dname, loc from dept where deptno=40"
cur.execute(sql)
row = cur.fetchone()  # tuple 반환
print(row)
