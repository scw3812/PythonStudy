import pandas as pd

df = pd.DataFrame([100, 200], columns=["가격"], index=["사과", "배"])
print(df)
print(df.loc["사과"])
print(df.iloc[0])
