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
print(m.get("age"))  # 없는 키값에 접근해도 에러가 안남
print(m.get(""))  # None
print(m.get("", "없음"))  # get()은 디폴트값을 줄 수 있다.
m.update({"email": "adsasd@naver.ocm"})
m.update({"username": "이순신", "age": 30})  # update()는 없는 키는 추가하고 있는 키는 수정
print(m)

del m["age"]
print(m)
m.clear()
print(m)

m = {"username": "홍길동", "age": 20}
print(list(m.keys()))  # keys()로 dict_keys를 반환 -> list()로 감싸줘서 활용가능
print(list(m.values()))  # values()로 dict_valuess를 반환 -> list()로 감싸줘서 활용가능
print(list(m.items()))  # items()로 dict_items(튜플)를 반환 -> list()로 감싸줘서 활용가능

print(len(m))
print("username" in m)
print("홍길동" in m)  # 딕트는 in을 쓸 때 키값으로 찾는다 밸류로는 못 찾는다
