import pandas as pd
import numpy as np

data_dict = {"이름": ["홍길동", "이순신", np.nan],
             "나이": [np.nan, 20, 30],
             "주소": ["서울", "경기", "제주"]}

df = pd.DataFrame(data_dict)

# 1. NaN 찾기
print("pd.isnull(벡터연산):", pd.isnull(df))
print("pd.isna:(벡터연산)", pd.isna(df))
print("df.isnull:(벡터연산)", df.isnull())
print("df.isna:(벡터연산)", df.isna())

# 2. NaN 삭제
drop_df = df.dropna()
print(drop_df)
drop_df = df.dropna(axis=1)
print(drop_df)

# 3. NaN 임의의 값으로 변경
change_df = df.fillna(0)
print(change_df)
change_df = df.fillna({"나이": 0, "이름": "NA"})  # 인자로 딕트를 넣어줘서 선택적 변경 가능
print(change_df)
change_df = df.fillna({"나이": {0: 0}})  # 인자로 딕트를 넣어줘서 선택적 변경 가능
print(change_df)

arr = np.arange(9).reshape((3, 3))
df = pd.DataFrame(arr, index=list('acd'), columns=["X", "Y", "Z"])
print(df)
df2 = df.reindex(list('abcd'))
print(df2)

# 1. 명시적으로 지정된 임의의 값으로 채우기
df2 = df.reindex(list('abcd'), fill_value="N")
print(df2)
# 2. front 값으로 채우기
df2 = df.reindex(list('abcd'), method="ffill")
print(df2)
# 3. back 값으로 채우기
df2 = df.reindex(list('abcd'), method="bfill")
print(df2)