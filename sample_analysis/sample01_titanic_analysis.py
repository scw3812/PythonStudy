# 머신러닝
#     1. 지도학습
#         분류
#         회귀
#     2. 비지도학습
#     3. 강화학습
# 데이터 분석
#     1. 데이터 수집
#     2. feature engineering(전처리) -> NaN 처리, 값 분류, encoding...
#     3. 데이터 분석: 기초통계, 추론통계, 시각화...

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")
print("상위 5개 출력:", df.head())
print("컬럼명 출력:", df.columns)
df.info()
print("NaN 확인:", df.isnull().sum())
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df.loc[df["Age"].isnull(), "Age"] = df["Age"].mean()
print("Age NaN 대신 평균:", df["Age"].fillna(df["Age"].mean(), inplace=True))  # inplace=True ->  얕은 복사
print("Cabin NaN 대신 N:", df["Cabin"].fillna("N", inplace=True))
print("Embarked NaN 대신 N:", df["Embarked"].fillna("N", inplace=True))
print("Cabin 항목 값을 첫글자로 변경")
df["Cabin"] = df["Cabin"].str[0]
print(df["Cabin"].value_counts())
# 분석?
# 성별 생존자 수?
print(df.groupby(["Sex", "Survived"])["Survived"].count())
# 부자와 가난한 사람의 생존자 수?
print(df.groupby(["Pclass", "Survived"])["Survived"].count())

# 시각화
vx = sns.barplot(x="Pclass", y="Survived", data=df)
plt.show()
