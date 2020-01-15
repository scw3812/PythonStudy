import pandas as pd
import numpy as np

# NaN(nan = None = Null)이 발생하는 경우
# 1. 값과 인덱스 개수 불일치
s = pd.Series({"A": 100, "B": 200}, index=["A", "B", "C", "D"])  # 리스트로 넣으면 에러 남
print(s)
# 2. 연산시 개수 불일치
s = pd.Series({"A": 100, "B": 200})
s2 = pd.Series({"A": 100, "B": 200, "C": 300})
s3 = s + s2
print(s3)

# 1. NaN 찾기
print("pd.isnull(벡터연산):", pd.isnull(s3))
print("pd.isna:(벡터연산)", pd.isna(s3))
print("s3.isnull:(벡터연산)", s3.isnull())
print("s3.isna:(벡터연산)", s3.isna())

# 2. NaN 삭제
s = pd.Series([100, 200, np.nan])
print(s)
drop_s = s.dropna()
print(drop_s)

# 3. NaN 임의의 값으로 변경
s = pd.Series([100, 200, np.nan])
print(s)
change_s = s.fillna(0)
print(change_s)

# 4. 다른 곳에서 가져온 임의의 값으로 변경
s = pd.Series([100, 200, 300], index=[0, 2, 4])
print(s)
s2 = s.reindex(range(6), method="ffill")  # reindex() 할 때 nan 나올것을 대비해서 method 인자를 설정해주면 nan을 처리할 수 있다.
# ffill(front fill) -> 앞에서 값을 가져옴, bfill(back fill) -> 뒤에서 값을 가져옴
print(s2)
