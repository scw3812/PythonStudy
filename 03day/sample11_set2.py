m = {10, 20, 30, 10}

print(len(m))
print(10 in m)
# 셋 연산자 : 교집합, 합집합, 차집합
a = {1, 2, 3}
b = {3, 4}
print(a.union(b))  # 합집합
print(a.intersection(b))  # 교집합
print(a.difference(b))  # 차집합
# 셋은 중복이 불가능하기 때문에 중복값 제거하기 위해 셋으로 바꿔서 활용한다 -> list(셋)을 하면 중복 없는 리스트가 만들어짐
a.clear()
print(a)  # 빈 set은 set()이다
