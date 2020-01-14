import pandas as pd

data_dict = {"이름": ["홍길동", "이순신"],
             "나이": [10, 20],
             "주소": ["서울", "경기"]}

df = pd.DataFrame(data=data_dict, index=["학생1", "학생2"])

name_series = df["이름"]
print(name_series)
print("시리즈 인덱스:", name_series.index)
print("시리즈 값:", name_series.values)
print("시리즈 정렬:", name_series.sort_index(ascending=False))

age_series = df["나이"]
print("age 평균:", age_series.mean())
print("age 최대:", age_series.max())
print("age 최소:", age_series.min())
print("age 중간값:", age_series.median())
print("age 합계:", age_series.sum())
print("age 개수:", age_series.count())
print("age 통계 요약:\n", age_series.describe())

