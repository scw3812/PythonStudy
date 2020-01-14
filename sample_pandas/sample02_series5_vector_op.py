import pandas as pd

s = pd.Series([10, 20])
print(s)

# 1. 시리즈 - 스칼라
print(s+2)

# 2. 시리즈 - 시리즈
print(s + s)
print(s * s)
s2 = pd.Series([10, 20, 30])  # 시리즈의 같은 인덱스(위치가 아니라 라벨)끼리 연산, 인덱스 수가 다르면 넘어가는 인덱스는 다 NaN
print(s + s2)

x = pd.Series([10, 20], index=['x', 'y'])
x2 = pd.Series([100, 200], index=['y', 'x'])
print(x + x2)
