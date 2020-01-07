print("Hello World")
print('Hello World')
print("""Hello World""")
print('''Hello World''')

print(3)
print(1.23)

print(True)
print(False)
print(1 < 3)

print(None)
# 스칼라 데이터(1개짜리, 정수, 실수, 논리...), 집합형 데이터(리스트, 튜플...)

print([1, 3, "서창우", 2, 3, True])
# 리스트는 순서가 있고, 중복 허용, mutable
print({1, 2, 3, "서창우", 3, 10, 30, 12, True})
# 셋은 순서가 없고, 중복 허용X, mutable
print((1, 2, "서창우", 2, False))
# 튜플도 순서가 있고, 중복 허용, 튜플은 만들고나서 변경이 불가능(immutable)
print({"username": "서창우", "age": 25, (3, 2): 20, 10: 12})
# 딕트는 {name: value}, 키값으로는 immutable 데이터만 가능 -> 문자열, 튜플, 숫자 등?
