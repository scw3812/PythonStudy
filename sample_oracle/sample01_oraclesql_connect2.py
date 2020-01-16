import cx_Oracle

user = "scott"
passwd = "tiger"
host = "localhost/xe"

con = cx_Oracle.connect(user, passwd, host)
print(con)

cur = con.cursor()
sql = "select deptno, dname, loc from dept where deptno=:xxx"
cur.execute(sql, xxx=10)
row = cur.fetchone()  # tuple 반환
print(row)
