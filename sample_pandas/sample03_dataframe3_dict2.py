import pandas as pd

kpop = {"BTS": {2001: "aaa", 2002: "bbb"},
        "EXO": {2001: "xxx", 2002: "zzz"}}  # 바깥 키 값은 컬럼, 안쪽 키 값은 인덱스

df = pd.DataFrame(data=kpop)
print(df)
