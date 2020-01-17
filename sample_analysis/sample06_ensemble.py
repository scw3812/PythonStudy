import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 앙상블 알고리즘
# 다양한 ML 사용
# 1. voting
#     하나의 데이터셋 + 서로 다른 ML 사용 -> 서로 다른 정확도
#     정확도 사용 방법
#         1. 하드 보팅: 투표 형식(나온 3개의 정확도 중에 투표로 뽑는 것)
#         2. 소프트 보팅: 확률
# 2. bagging
#     여러개의 데이터셋 + 같은 ML
# 3. boosting
#     여러번 학습과 예측
#     첫번째 학습과 예측에서 잘못된 것을 두번째 학습에서 가중치 이용해서 수정해서 재학습/예측 반복

cancer = load_breast_cancer()
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
print(df)
# 개별 모델
lc_r = LogisticRegression(max_iter=10000)  # iter -> 최대 반복 횟수
knn_clf = KNeighborsClassifier(n_neighbors=4)

# 개별 모델을 묶어 주는 보팅
vo_clf = VotingClassifier(estimators=[("LR", lc_r), ("KNN", knn_clf)], voting="soft")

# 학습 데이터와 테스트 데이터로 분리
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.2, random_state=11)

# 학습과 예측
vo_clf.fit(x_train, y_train)
prediction = vo_clf.predict(x_test)

# 정확도
print("VotingClassifier 정확도:", accuracy_score(y_test, prediction))

# 개별 ML 정확도
models = [lc_r, knn_clf, vo_clf]
for m in models:
    m.fit(x_train, y_train)
    prediction = m.predict(x_test)
    name = m.__class__.__name__
    print(name + " 정확도:", accuracy_score(y_test, prediction))
