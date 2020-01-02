m = {"username": "홍길동", "age": 20}
m2 = {}  # 비어있는 중괄호는 set이 아닌 dict
print(type(m2))
m3 = dict(username="이순신", age=20)
print(m3)
m4 = dict([("username", "손흥민")])  # list 안의 list, list 안의 tuple
print(m4)

print(m["username"], m["age"])
# print(m["email"]) 없는 키값을 넣으면 에러
m["address"] = "서울"
print(m)
m["username"] = "정약용"
print(m)
