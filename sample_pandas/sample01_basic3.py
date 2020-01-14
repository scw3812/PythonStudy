import pandas as pd

df = pd.read_csv("cat.csv")

# 1. 행단위 데이터 추출1 - 인덱스명(라벨) -> loc[] 인덱서
print("0 인덱스명(라벨):", df.loc[0])
print("0, 1 인덱스명(라벨):", df.loc[[0, 1]])
print("0~5 인덱스명(라벨):", df.loc[:5])
# 2. 행단위 데이터 추출2 - 행위치(인덱스) -> iloc[] 인덱서
print("0 인덱스:", df.iloc[0])
print("0, 1 인덱스:", df.iloc[[0, 1]])
print("0~5 인덱스:", df.iloc[:5])
# 3. 가장 마지막 행 추출
print("마지막 인덱스:", df.iloc[-1])  # -> 시리즈 반환
print("마지막 인덱스:", df.tail(1))  # -> 데이터 프레임 반환
