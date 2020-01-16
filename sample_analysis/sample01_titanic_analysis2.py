import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")
# 연령별 사망자수(생존자수)?
def get_category(age):
    cat = ""
    if age <= -1:
        cat = "Unknown"
    elif age <= 5:
        cat = "Baby"
    elif age <= 19:
        cat = "Child"
    elif age <= 30:
        cat = "Young Adult"
    elif age <= 60:
        cat = "Adult"
    else:
        cat = "Old"
    return cat


# df["Age"] = df["Age"].apply(get_category)
group_name = ["Unknown", "Baby", "Child", "Young Adult", "Adult", "Old"]
df["age_cat"] = df["Age"].apply(lambda n: get_category(n))
vx = sns.barplot(x="age_cat", y="Survived", data=df, hue="Sex", order=group_name)
plt.show()
