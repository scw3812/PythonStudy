import pandas as pd
import numpy as np

arr = np.array([100, 200])
df = pd.DataFrame(arr, columns=["가격"], index=["사과", "배"])
df2 = pd.DataFrame([100, 200], columns=["가격"], index=["사과", "배"])
print(df)
print(df2)
