import pandas as pd
import numpy as np

data_dict = {"이름": ["홍길동", "이순신", "강감찬", "유관순", "정조"],
             "나이": [10, 20, np.nan, 32, 48],
             "주소": ["서울", "경기", "제주", "서울", "경기"]}

df = pd.DataFrame(data=data_dict)
print(df)
print("나이의 합:", df["나이"].sum())
print("나이의 합:", df["나이"].sum(skipna=True))
print("나이의 합:", df["나이"].sum(skipna=False))  # skipna 인자를 False로 놔서 nan을 연산에 포함 가능, default는 True
