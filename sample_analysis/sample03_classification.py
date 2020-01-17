# import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# sklearn.datasets 데이터
#   학습 데이터(feature): dataset.data
#     결과(label): dataset.target
#     컬럼: dataset.feature_names

# iris = load_iris()
# print(iris.keys())
# input_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# print(input_data.isnull().sum())
# output_data = pd.DataFrame(data=iris.target)
# print(output_data)
#
# x_train, x_test, y_train, y_test = train_test_split(input_data, output_data)
#
# tree = DecisionTreeClassifier()
# tree.fit(x_train, y_train)
# print(tree.score(x_test, y_test))

# 1. 데이터 불러오기
iris = load_iris()

# 2. feature, label 분리 -> 데이터프레임이 아니여도 머신러닝을 실행하는데 상관 없다
iris_feature = iris.data
iris_label = iris.target

# 3. ML 선택
dt_clf = DecisionTreeClassifier()

# 4. 학습데이터와 테스트 분리
x_train, x_test, y_train, y_test = train_test_split(iris_feature, iris_label, test_size=0.2, random_state=11)
# random_state -> random 시드 역할(시드는 난수 생성의 기준으로, 시드 설정하면 난수 발생시 처음 나오는 값을 고정시켜줌)

# 5. 학습
dt_clf.fit(x_train, y_train)

# 6. 예측
prediction = dt_clf.predict(x_test)

# 7. 정확도
print(accuracy_score(y_test, prediction))
