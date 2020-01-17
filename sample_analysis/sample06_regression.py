import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# 회귀(regression): 통계학에서 회귀는 독립변수와 종속변수간의 인과관계를 모델링 ex) 독립변수:iq, 종속변수:score
#   회귀식: 1차방정식, y = ax + b -> 기울기(=회귀계수) 찾기 -> 잔차(최소거리) 제곱의 합으로 가장 잘 예측하는 모델 찾기
#       단일 회귀식: 하나의 독립변수, 다중 회귀식: 여러개의 독립변수

score_iq = pd.read_csv("score_iq.csv")
print(score_iq)

# 독립변수와 종속변수
x = score_iq["iq"]
y = score_iq["score"]

# 산정도
plt.scatter(x, y)
plt.show()

# 회귀식
model = stats.linregress(x, y)
print("기울기:", model.slope)
print("절편:", model.intercept)
print("p-value:", model.pvalue)  # p-value가 0.05보다 작으면 회귀모델이 적합
print("표준오차:", model.stderr)

# 검증해보기
x2 = 140
y2 = 0.6514309527270089 * x2 - 2.8564471221976504
print(y2)