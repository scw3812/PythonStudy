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

# 1. 병합(merge) - 공통컬럼 존재 -> on="공통컬럼"
merge_df = pd.merge(dept_df, emp_df, on="deptno")
print(merge_df)
print(merge_df[["empno", "ename", "sal", "dname"]])

# 2. 병합(merge) - 공통컬럼 X -> left_on="왼쪽 컬럼" right_on="오른쪽 컬럼"
emp_df = pd.DataFrame({"empno": ["A1", "A2", "A3", "A4", "A5"],
                       "ename": ["홍길동", "이순신", "강감찬", "정조", "영조"],
                       "sal": [1000, 2000, 1500, 4500, 4200],
                       "d_no": [10, 20, 30, 10, 20]})
merge_df = pd.merge(dept_df, emp_df, left_on="deptno", right_on="d_no")
print(merge_df)
print(merge_df[["empno", "ename", "sal", "dname"]])

# 3. outer 조인 -> how 속성에 left -> 왼쪽 다, right -> 오른쪽 다, outer -> 싹 다
emp_df = pd.DataFrame({"empno": ["A1", "A2", "A3", "A4", "A5"],
                       "ename": ["홍길동", "이순신", "강감찬", "정조", "영조"],
                       "sal": [1000, 2000, 1500, 4500, 4200],
                       "deptno": [np.nan, 20, 30, 10, 20]})
merge_df = pd.merge(dept_df, emp_df, on="deptno", how="left")
print(merge_df)

# 4. 컬럼과 인덱스 merge
df = pd.DataFrame({"도시": ["서울", "부산", "제주", "제주", "서울", "서울"],
                   "도시번호": [1000, 455, 333, 2222, 666, 7777]})
df2 = pd.DataFrame(["특별시", "광역시", "자치도"], index=["서울", "부산", "제주"], columns=["도시종류"])
merge_df = pd.merge(df, df2, left_on="도시", right_index=True)  # index 속성을 True로 하면 컬럼과 인덱스로 합쳐줌
print(merge_df)
