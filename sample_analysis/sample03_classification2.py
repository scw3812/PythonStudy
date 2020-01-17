import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

# 교차검정
# 오버핏(over-fitting): 학습시 사용했던 데이터로는 정확도가 높지만 다른 데이터로는 정확도가 떨어짐
# -> 교차검정으로 이를 해결

iris = load_iris()
iris_feature = iris.data
iris_label = iris.target
dt_clf = DecisionTreeClassifier()

score = cross_val_score(dt_clf, iris_feature, iris_label, scoring="accuracy", cv=3)
# scoring 인자는 검증기준, cv 인자는 데이터 나누는 개수
print("교차검증별 정확도:", np.round(score, 4))
print("평균 정확도:", np.round(np.mean(score), 4))
