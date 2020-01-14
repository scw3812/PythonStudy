import pandas as pd

s = pd.Series([10, 20])
print(s)

# 1. 시리즈 - 스칼라
print(s + 2)

# 2. 시리즈 - 시리즈
print(s + s)
print(s * s)
s2 = pd.Series([10, 20, 30])  # 시리즈의 같은 인덱스(위치가 아니라 라벨)끼리 연산, 인덱스 수가 다르면 넘어가는 인덱스는 다 NaN
print(s + s2)

x = pd.Series([10, 20, 30], index=['x', 'y', 'z'])
x2 = pd.Series([100, 200, 40], index=['y', 'x', 'a'])
print(x + x2)

# 3. 함수로 연산
print(x.add(x2, fill_value=0))
print(x.sub(x2, fill_value=0))
print(x.mul(x2, fill_value=0))
print(x.div(x2, fill_value=0))  # fill_value 인자로 비어있는 값에 대체값을 넣을 수 있음

# 4.
x = pd.Series([10, 20, 30, 40], index=['x', 'y', 'k', 'z'])
print(x.reindex(['k', 'x', 'y', 'z']))
