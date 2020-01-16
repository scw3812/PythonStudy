import cx_Oracle

user = "scott"
passwd = "tiger"
host = "localhost/xe"

con = cx_Oracle.connect(user, passwd, host)

# update
cur = con.cursor()
sql = "update dept set dname=:x, loc=:y where deptno=:z"  # sql문에 세미콜론 있으면 안됨
cur.execute(sql, x="인사", y="서울", z=3)
con.commit()
