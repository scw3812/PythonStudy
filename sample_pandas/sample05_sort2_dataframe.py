import pandas as pd
import numpy as np

arr = np.arange(8).reshape((2,4))
df = pd.DataFrame(arr, index=["three", "one"],
                  columns=list('dabc'))
print(df)
# 1. 인덱스 정렬
index_df = df.sort_index()
print(index_df)
index_df = df.sort_index(axis=1)
print(index_df)
index_df = df.sort_index(axis=1, ascending=False)
print(index_df)
# 2. 값 정렬
value_df = index_df.sort_values(by="d")
print(value_df)
value_df = index_df.sort_values(by="one", axis=1)
print(value_df)
value_df = index_df.sort_values(by="one", axis=1, ascending=False)
print(value_df)
