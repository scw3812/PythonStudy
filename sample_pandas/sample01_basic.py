import pandas as pd

df = pd.read_csv("cat.csv")
print(df, type(df))
print("df.shape:", df.shape)
print("df.columns:", df.columns)
print("df.index:", df.index)
print("데이터 타입:", df.dtypes)
print("전반적인 정보:")
df.info()
print("상위 5개:", df.head())
print("상위 3개:", df.head(3))
print("하위 5개:", df.tail())
print("하위 3개:", df.tail(3))
