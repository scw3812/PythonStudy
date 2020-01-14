import pandas as pd


data_dict = {"이름": ["홍길동", "이순신"],
             "나이": [10, 20],
             "주소": ["서울", "경기"]}

df = pd.DataFrame(data=data_dict, index=["학생1", "학생2"])
df["이메일"] = ["naver", "google"]
df["서울거주여부"] = (df["주소"] == "서울")
print(df)
