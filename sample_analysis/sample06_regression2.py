import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

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

# formula 이용한 회귀 모델 작성
# formula = '종속변수' ~ '독립변수'(단일 회귀)
# formula = '종속변수' ~ '독립변수'+'독립변수'+...(다중 회귀)
result = smf.ols(formula="y ~ x", data=score_iq).fit()
print(result.summary())

for i in range(len(score_iq.score)):
    print(score_iq.score[i], result.predict()[i])
