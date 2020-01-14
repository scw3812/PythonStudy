import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(1, 13).reshape(3, 4), index=['A', 'B', 'C'], columns=['a', 'b', 'c', 'd'])
print(df.reindex(["C", "A", "B"]))  # reindex()는 인덱스 순서만 변경하는게 맞다(다른 인덱스로 바꾸려고 하면 NaN이 되버림)

