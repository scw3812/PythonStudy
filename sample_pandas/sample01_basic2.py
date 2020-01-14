import pandas as pd

df = pd.read_csv("cat.csv")

# 1. 열단위 데이터 추출 1
print(df.columns)
name = df["name"]
print("name 컬럼값 추출:", name, type(name))
# 2. 열단위 데이터 추출 2
name_age = df[["name", "age"]]
print("name, age 컬럼값 추출:", name_age)
print("순서 변경 출력:", df[["gender", "name", "age"]])
