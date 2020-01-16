import pandas as pd
import numpy as np

dept_df = pd.DataFrame({"deptno": [10, 20, 30, 40],
                        "dname": ["개발", "인사", "관리", "영업"],
                        "loc": ["서울", "부산", "제주", "광주"]})
emp_df = pd.DataFrame({"empno": ["A1", "A2", "A3", "A4", "A5"],
                       "ename": ["홍길동", "이순신", "강감찬", "정조", "영조"],
                       "sal": [1000, 2000, 1500, 4500, 4200],
                       "deptno": [10, 20, 30, 10, 20]})

print(dept_df)
print(emp_df)

# groupby에서 사용자 정의 함수 적용 -> agg()
def my_mean(vs):
    n = len(vs)
    sum = 0
    for v in vs:
        sum += v
    return sum / n


# 1. 그룹핑(groupby() 함수 이용)
print("부서별 sal 총합:", emp_df.groupby(by="deptno")["sal"].sum())
print("부서별 sal 평균:", emp_df.groupby(by="deptno")["sal"].mean())
print("부서별 sal 평균:", emp_df.groupby(by="deptno")["sal"].agg(my_mean))
print("부서별 sal 최댓값:", emp_df.groupby(by="deptno")["sal"].max())
print("부서별 sal 최솟값:", emp_df.groupby(by="deptno")["sal"].min())
print("부서별 sal 평균, 합(agg 활용):\n", emp_df.groupby(by="deptno")["sal"].agg([my_mean, sum]))
