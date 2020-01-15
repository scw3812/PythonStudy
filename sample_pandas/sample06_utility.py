import pandas as pd
import numpy as np

# 유틸리티 함수
# 1. all() 모두 만족해야 True, any() 하나만 만족해도 True()
# Series
s = pd.Series([2, 4, 6])
print("시리즈 s가 모두 짝수?:", (s % 2 == 0).all())
print("시리즈 s가 하나라도 짝수?:", (s % 2 == 0).any())

# DataFrame
df = pd.DataFrame({"k": [2, 4, 6, 5], "k2": [1, 3, 5, 7]})
print("df의 k 컬럼이 모두 짝수?:", (df["k"] % 2 == 0).all())
print("df의 k2 컬럼이 하나라도 짝수?:", (df["k2"] % 2 == 0).any())

# 2. cut() 카테고리 생성
ages = [23, 45, 67, 32, 47, 64, 31, 100, 29, 34]
bins = [20, 28, 35, 60, 100]

data = pd.cut(ages, bins)  # pd.cut(arr, arr2) arr2를 카테고리로 arr이 어디에 포함되는지를 리스트로 반환
print(data.codes)  # codes -> 카테고리 번호 리스트 반환
print(pd.value_counts(data))
data = pd.cut(ages, bins, right=False)  # right 인자가 True이면 포함관계가 (a,b], False이면 포함관계가 [a,b)
print(data)

group_names = ["청년", "중년", "장년", "노년"]
data = pd.cut(ages, bins, labels=group_names)
print(data)

# 3. Series 중복 제거
s = pd.Series([0, 1, 1, 2, 1, 1, 2, 2], index=list("abcdefgh"))
print("중복값?", s.duplicated())  # 위에서부터 처음 나온 값은 False,  두번 나오는 값부터 True인 시리즈 반환
print("중복값 삭제후 반환", s.drop_duplicates())

# 4. DataFrame 중복 제거
df = pd.DataFrame({"k": ["one"]*3 + ["two"]*4, "k2": [1, 1, 2, 3, 4, 4, 4]})
print(df)
print("중복값?\n", df.duplicated())  # 한 행을 하나의 값으로 봄
print("중복값 삭제후 반환\n", df.drop_duplicates())

# 5. Series 수정
s = pd.Series([1, 3, 5, 9999, 6, -8888])
print(s)
replace_s = s.replace(9999, np.nan)
print(replace_s)
replace_s = s.replace([9999, -8888], [np.nan, 0])
print(replace_s)
replace_s = s.replace({9999: np.nan, -8888: 0})
print(replace_s)

# 6. DataFrame 수정
data_dict = {"이름": ["홍길동", "이순신"],
             "나이": [10, 9999],
             "주소": ["서울", "경기"]}
df = pd.DataFrame(data_dict)
replace_df = df.replace({9999: np.nan})
print(replace_df)

# 7. filter() -> axis 인자로 행, 열 정하고, 비슷한 것도 찾을 수 있음
arr = np.arange(12).reshape((3, 4))
df = pd.DataFrame(arr, index=["mouse", "rabbit", "habit"], columns=["one", "two", "three", "four"])
print(df)
print("행으로 검색:\n", df.filter(["mouse", "rabbit"], axis=0))
print("열로 검색:\n", df.filter(["one", "two"], axis=1))
print("행으로 검색, bit 포함:\n", df.filter(like="bit", axis=0))
print("열로 검색, t 포함:\n", df.filter(like="t", axis=1))