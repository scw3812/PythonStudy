import pandas as pd
import numpy as np

s = pd.Series(np.arange(4), index=list('dabc'))
print(s)
# 1. 인덱스로 정렬
s_index = s.sort_index()
print(s_index)
s_index = s.sort_index(ascending=False)
print(s_index)
# 2. 값으로 정렬
s_value = s_index.sort_values()
print(s_value)
s_value = s_index.sort_values(ascending=False)
print(s_value)
