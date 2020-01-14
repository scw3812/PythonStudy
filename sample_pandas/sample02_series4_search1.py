import pandas as pd
# 넘파이 어레이가 리스트의 업그레이드 버전이었다면 시리즈는 딕트의 업그레이드 버전 -> 시리즈는 인덱싱하면 키값으로 찾는다
data_dict = {"이름": ["홍길동", "이순신", "유관순", "강감찬", "정조"],
             "나이": [10, 20, 30, 40, 50],
             "주소": ["서울", "경기", "대전", "부산", "제주"]}

df = pd.DataFrame(data_dict)
# 1. 색인
age_series = df["나이"]
print("age 컬럼에서 첫번째 값:", age_series[0])
print("age 컬럼에서 0, 2, 4 값:", age_series[[0, 2, 4]])
print("age 컬럼에서 2부터 끝 값:", age_series[1:])
print("age 거꾸로:", age_series[::-1])
print("age 마지막:", age_series.tail(1))
print("age 마지막:", age_series.iloc[-1])

# 2. 불린 색인
print("벡터연산:", age_series > 20)
print("불린연산1:", age_series[age_series > 20])
print("불린연산2:", age_series[(age_series > 30) & (age_series < 50)])
print("불린연산3:", age_series[age_series > age_series.mean()])
print("불린연산4:", df["이름"][age_series > age_series.mean()])
