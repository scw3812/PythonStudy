import pandas as pd

name_series = pd.Series(["cat01", "cat02"], name="이름")
age_series = pd.Series([2, 3], name="나이")
gender_series = pd.Series(["M", "F"], name="성별")

df = pd.DataFrame([name_series, age_series, gender_series])
df.columns = ["고양이1", "고양이2"]
print(df)
print(df.T)  # Transpose -> 행, 열 바꾸기
