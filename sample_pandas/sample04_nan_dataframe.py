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