# 지도학습, 비지도학습 : iris data 사용

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris = sns.load_dataset('iris')
print(iris)
iris_feature = iris.drop('species', axis=1)
iris_label = iris['species']
X_train, X_test, y_train, y_test = \
    train_test_split(iris_feature, iris_label, random_state=1)
print(len(X_train))
print(len(X_test))
print(len(y_train))

# 지도학습 : iris 분류
from sklearn.naive_bayes import GaussianNB
dt_clf = DecisionTreeClassifier()
dt_clf.fit(X_train, y_train)
pred = dt_clf.predict(X_test)
print(pred)

from sklearn.metrics import accuracy_score
print('accuracy_score : ', accuracy_score(y_test, pred))
print()

# 비지도학습 : iris 차원 축소

from sklearn.decomposition import PCA
model = PCA(n_components=2)
model.fit(iris_feature)  # 독립변수만 입력, Label(y)는 지정하지 않음
result = model.fit_transform(iris_feature)  # 데이터를 2차원으로 변환
print(result)
# [[-2.68412563  0.31939725]
#  [-2.71414169 -0.17700123]
#  [-2.88899057 -0.14494943] ...
iris['PCA1'] = result[:, 0]
iris['PCA2'] = result[:, 1]
sns.lmplot('PCA1', 'PCA2', data=iris, hue='species', fit_reg=False)
plt.show()

# PCA 모델이 iris의 Label에 대한 지식이 없는데도 2차원 표현에서 종류가 2개로 잘 분류된 것을 알 수 있다.


print()

# 비지도학습 : iris 군집화

from sklearn.cluster import KMeans
kmodel = KMeans(n_clusters=3, init='random', random_state=0)  # 'k-means++'
# n_clusters:클러스터 개수 지정
# init: 초기 클러스터 중심을 선택하는 방법 지정(초기값은 k-means++)
pred = kmodel.fit_predict(X_train)  # k-means 클러스터링으로 구분한 결과 얻기
print('pred : ', pred)


