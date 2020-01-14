import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(1, 13).reshape(3, 4), index=['A', 'B', 'C'], columns=['a', 'b', 'c', 'd'])
print(df)

df2 = pd.DataFrame(np.arange(1, 21).reshape(4, 5), index=['A', 'B', 'C', 'D'], columns=['a', 'b', 'c', 'd', 'e'])
print(df2)

print(df + df2)
print(df.add(df2, fill_value=0))
print(df.sub(df2, fill_value=0))
print(df.mul(df2, fill_value=0))
print(df.div(df2, fill_value=0))
