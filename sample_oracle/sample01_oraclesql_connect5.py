import cx_Oracle

user = "scott"
passwd = "tiger"
host = "localhost/xe"

con = cx_Oracle.connect(user, passwd, host)

# update
cur = con.cursor()
sql = "delete from dept where deptno=:x"  # sql문에 세미콜론 있으면 안됨
cur.execute(sql, x=3)
con.commit()
