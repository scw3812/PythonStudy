import pandas as pd

s = pd.Series([10, 3, 5, 6, 10,4, 3, 3])

print("중복제거후 반환:", s.unique())
print("각 요소의 개수:", s.value_counts())
print("값 존재 여부(불린 리스트 반환):", s.isin([10]))
print("값 존재여부(값반환):", s[s.isin([10])])
