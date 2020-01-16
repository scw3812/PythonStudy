import pandas as pd
from sklearn.preprocessing import LabelEncoder

def titanic_encode(data, columns):
    encoder = LabelEncoder()
    for c in columns:
        encoder.fit(data[c])
        data[c] = encoder.transform(data[c])
        print(data[c])


df = pd.read_csv("train.csv")

df["Cabin"].fillna("N", inplace=True)
df["Embarked"].fillna("N", inplace=True)
titanic_encode(df, ["Cabin", "Embarked", "Sex", "Ticket"])

df.loc[df["Age"].isnull(), "Age"] = df["Age"].mean()
