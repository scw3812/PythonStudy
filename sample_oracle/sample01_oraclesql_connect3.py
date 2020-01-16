import cx_Oracle

user = "scott"
passwd = "tiger"
host = "localhost/xe"

con = cx_Oracle.connect(user, passwd, host)

# insert
cur = con.cursor()
sql = "insert into dept (deptno, dname, loc) values (:x, :y, :z)"
cur.execute(sql, x=3, y="개발2", z="제주2")
con.commit()
