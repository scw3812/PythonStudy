import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

str_items = ["냉장고", "전자레인지", "컴퓨터", "선풍기", "믹서", "믹서"]
encoder = LabelEncoder()
encoder.fit(str_items)
str_items = encoder.transform(str_items)
print(str_items)

# One-hot encoding
df = pd.DataFrame({"item": ["냉장고", "전자레인지", "컴퓨터", "선풍기", "믹서", "믹서"]})
print(pd.get_dummies(df))

encoder = OneHotEncoder()
encoder.fit(df)
print(encoder.transform(df))
