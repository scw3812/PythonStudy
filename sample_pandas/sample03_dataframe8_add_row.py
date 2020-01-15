import pandas as pd

data_dict = {"이름": ["홍길동", "이순신"],
             "나이": [10, 20],
             "주소": ["서울", "경기"]}

df = pd.DataFrame(data=data_dict, index=["학생1", "학생2"])
print(df)

data_dict2 = {"이름": ["정조", "유관순"],
              "나이": [30, 15],
              "주소": ["부산", "제주"]}

df2 = pd.DataFrame(data=data_dict2, index=["학생1", "학생2"])

# 새 DataFrame 만들기
new_df = df.append(df2, ignore_index=True)  # append() 사용시 인덱스가 그대로 유지되는 것을 없애고 싶으면 ignore_index 인자를 True
print(new_df)

new_df = pd.concat([df, df2], ignore_index=True)
print(new_df)

# 원래 DataFrame에 추가
df.loc["학생3"] = ["유관순", 15, "부산"]
print(df)
