import pandas as pd

data_dict = {"이름": ["홍길동", "이순신"],
             "나이": [10, 20],
             "주소": ["서울", "경기"]}

df = pd.DataFrame(data=data_dict, index=["학생1", "학생2"])

data_dict2 = {"이름": ["정조", "유관순"],
              "나이": [30, 15],
              "주소": ["부산", "제주"]}

df2 = pd.DataFrame(data=data_dict2, index=["학생1", "학생2"])

new_df = pd.concat([df, df2], ignore_index=True)
print(new_df)

# 새 DataFrame 만들기
print(new_df.drop(2, axis=0))
print(new_df.drop([0, 1], axis=0))

new_df.index = ["A", "B", "C", "D"]
print(new_df.drop(["A", "B"], axis=0))
