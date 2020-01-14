import pandas as pd


data_dict = {"이름": ["홍길동", "이순신"],
             "나이": [10, 20],
             "주소": ["서울", "경기"]}

# 1. 삭제된 복사본
df = pd.DataFrame(data=data_dict, index=["학생1", "학생2"])
df["이메일"] = ["naver", "google"]
df["서울거주여부"] = (df["주소"] == "서울")
df2 = df.drop("주소", axis=1)  # drop(, axis=) axis 인자가 0이면 행, 1이면 열
print(df, "\n", df2)
df2 = df.drop(["주소", "나이"], axis=1)
print(df2)

# 2. 자신이 삭제
del df["이메일"]
print(df)
