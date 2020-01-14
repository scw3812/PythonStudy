import pandas as pd

df = pd.read_csv("cat.csv")

# 1. 행과 열 조합
# print("0 위치의 name과 age 컬럼만 출력:", df[["name", "age"]].iloc[0])
print("0 라벨의 name과 age 컬럼만 출력:\n", df.loc[0, ["name", "age"]])  # loc[]은 라벨이므로 문자열로
print("0 위치의 name과 age 컬럼만 출력:\n", df.iloc[0, [0, 1]])  # iloc[]는 위치이니까 숫자로
print("0, 2, 4 위치의 name과 age 컬럼만 출력:\n", df.loc[[0, 2, 4], ["name", "age"]])
print("3 위치 이후의 모든 컬럼:\n", df.iloc[3:, :])