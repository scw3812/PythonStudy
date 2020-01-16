# 머신러닝: 기계학습
#     개념: 기계에게 학습 시켜서 패턴을 찾아내는 작업 -> 패턴이 잘못된 패턴일 수도 있다
#     종류
#         1. 지도학습: 문제와 답 제공 ex) 고양이 사진만 학습 -> 고양이 패턴만 찾기
#         2. 비지도학습: 문제만 제공 ex) 강아지, 고양이 사진 동시 학습 -> 스스로 패턴 찾기
#         3. 강화학습: 문제 + 보상
#     머신러닝 주요 패키지(필요한 라이브러리)
#         python, numpy, pandas, matplotlib, sklearn...
#     지도학습 종류
#         1. 분류(Classification): 정해진 값으로 분류 ex) 스팸메일 분류, 숫자 인식...
#         2. 회귀(Regression): 예측 ex) 부동산 전망 예측...
#     사이킷런
#         분류/ 회귀 모두 fit(), predict() 함수 이용
#         fit()은 학습, predict()는 예측
#         1. sklearn.datasets: 실습 데이터 셋
#         2. sklearn.preprocessing: 데이터 전처리 -> 인코딩, 피쳐 스케일링(0~1로 처리)...
#         3. sklearn.decomposition: 차원 축소 알고리즘
#         4. sklearn.model_selection: 교차 검증을 위한 학습/테스트 데이터 분리
#         5. sklearn.metrics: 다양한 성능 측정 방법 제공 -> accuracy, Recall...
#     사이킷런 알고리즘
#         1. 분류 알고리즘(Classifier): DecisionTreeClassifier, RandomForestClassifier, GradientBoostingClassifier, SVC...
#         2. 회귀 알고리즘(Regressor): LinearRegression, RandomForestRegressor, GradientBoostingRegressor, SVR...
#     ML 알고리즘
#         1. sklearn.ensemble: 앙상블 알고리즘(랜덤포레스트, 그래디언트부스터 포함)
#             a. 보팅(voting): 하나의 데이터셋에 여러 알고리즘 적용
#             b. 배깅(bagging): 여러 데이터셋에 하나의 알고리즘
#             c. 부스팅(boosting): 하나로 여러번
#         2. sklearn.linear_model: 선형회귀, 로지스틱 회귀 등에 최적화된 모듈
#         3. sklearn.neighbors: KNN(K값 기준 최근접 이웃 알고리즘), 분류 알고리즘
#         4. sklearn.tree: 의사결정트리(트리구조) -> 분류
#         5. sklearn.cluster: 비지도 학습의 분류

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier

def titanic_encode(data, columns):
    encoder = LabelEncoder()
    for c in columns:
        encoder.fit(data[c])
        data[c] = encoder.transform(data[c])
        print(data[c])


df = pd.read_csv("train.csv")

df["Cabin"].fillna("N", inplace=True)
df["Embarked"].fillna("N", inplace=True)
titanic_encode(df, ["Cabin", "Embarked", "Sex", "Ticket"])

df.loc[df["Age"].isnull(), "Age"] = df["Age"].mean()
df = df.drop(["Name", "Ticket"], axis=1)

input_data = df.drop(["Survived"], axis=1)
output_data = df["Survived"]

model = GradientBoostingClassifier()
model.fit(input_data, output_data)

test = pd.read_csv("test.csv")

test["Cabin"].fillna("N", inplace=True)
test["Embarked"].fillna("N", inplace=True)

titanic_encode(test, ["Cabin", "Embarked", "Sex", "Ticket"])

test.loc[test["Age"].isnull(), "Age"] = test["Age"].mean()
test.loc[test["Fare"].isnull(), "Fare"] = test["Fare"].mean()
test = test.drop(["Name", "Ticket"], axis=1)
print(model.predict(test))

submit = pd.DataFrame({
    "PassengerId": test["PassengerId"],
    "Survived": model.predict(test)
})
submit.to_csv("submit.csv", index=False)
