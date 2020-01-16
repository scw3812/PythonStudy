import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 머신러닝은 숫자만 이해한다 -> 인코딩 필수

str_items = ["냉장고", "전자레인지", "컴퓨터", "선풍기", "믹서", "믹서"]
encoder = LabelEncoder()
encoder.fit(str_items)  # 머신러닝에서 데이터 인식(학습)시키는 작업
str_items = encoder.transform(str_items)
print(str_items)

# 타이타닉 인코딩 처리
def encoding(data, column):
    encoder = LabelEncoder()
    encoder.fit(data[column])  # 머신러닝에서 데이터 인식(학습)시키는 작업
    data[column] = encoder.transform(data[column])
    print(data[column])


df = pd.read_csv("train.csv")

df["Cabin"].fillna("N", inplace=True)
encoding(df, "Cabin")
df["Embarked"].fillna("N", inplace=True)
encoding(df, "Embarked")
encoding(df, "Sex")
encoding(df, "Ticket")

df.loc[df["Age"].isnull(), "Age"] = df["Age"].mean()
