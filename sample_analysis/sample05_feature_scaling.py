import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# 피쳐스케일링 -> 단위가 다른 데이터를 비슷하게 맞춰주는 작업
# -> 평균을 0으로 근접, 분산을 1로 근접

iris = load_iris()
iris_data = iris.data

# 1. DataFrame 변환 -> 평균, 분산 함수 사용하기 위해
df = pd.DataFrame(iris_data, columns=iris.feature_names)
print(df)
print("평균:", df.mean())
print("분산:", df.var())

# 2. 피쳐 스케일링(정규화)
scaler = StandardScaler()
scaler.fit(df)
iris_scaled = scaler.transform(df)
df = pd.DataFrame(iris_scaled, columns=iris.feature_names)
print("평균:", df.mean())
print("분산:", df.var())
