name = "山口"
age = 25
print(name)
print(age)
height = 170.5

print(type(name))
print(type(age))
print(type(height))

scores = [80, 60, 90]
print(scores)
print(scores[0])
print(scores[1])
print(scores[2])

for score in scores:
    print(score)

for index, score in enumerate(scores):
    print(index, score)

user= {
    "name": "山口",
    "age": 25
}

print(user["name"])
print(user["age"])

if user["age"] <= 20:
    print("未成年")
else:
    print("成人")

def greet(name):
    print(f"こんにちは{name}")

greet("佐藤")

def add(a, b):
    return a + b 

result = add(17, 12345)
print(result)

class User:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"こんにちは{self.name}")

user = User("山田")
user.greet()
print(user.name)

users =[]
users.append(User("佐藤"))
users.append(User("田中"))
print(type(users))
for user in users:
    print(user.name)
    user.greet()
    print(type(user))
# オブジェクトそのものを格納している

import pandas as pd

df = pd.read_csv("users2.csv")
print(df)

import json
with open("sample.json", "r") as f:
    data = json.load(f)

print(data) 

import pandas as pd
data = {
    "name": ["佐藤", "田中", "鈴木"],
    "score": [80, 65, 90]
}

df = pd.DataFrame(data)
print(df)
# Series
print(df["name"])
# DataFrame
print(df[["name"]])
# 複数取得
print(df[["name", "score"]])
print(df[df["score"] >= 80])
# 条件式だけだとBoolean
print(df["score"] >= 80 )
#複数条件
print(
    df[
        (df["score"] >= 81)
        &
        (df["score"]<=90)
    ]
)

print(df.sort_values("score"))
print(df.sort_values("score", ascending=False))

print(df["score"].mean())
print(df["score"].max())
print(df["score"].min())
print(df["score"].sum())
print(df["score"].count())

import pandas as pd

df = pd.DataFrame(
    {
        "department": ["営業", "営業", "開発", "開発"],
        "score": [80, 60, 90, 70]
    }
)

print(
    df.groupby("department")["score"].mean()
)
print(
    df.groupby("department")["score"].sum()
)
print(
    df.groupby("department")["score"].count()
)

# SQL版: SELECT department, AVG(score) FROM users GROUP BY department;

users = pd.DataFrame(
    {
        "user_id": [1, 2, 3],
        "name": ["佐藤", "田中", "鈴木"]
    }
)

scores = pd.DataFrame({
    "user_id": [1,2,4],
    "score": [80,70,90]
})

# pdのメソッドmerge
result = pd.merge(
    users, scores, on="user_id"
)

print(result)

result = pd.merge(
    users, scores, on="user_id", how="left"
)
print(result)

result = pd.merge(
    users, scores, on="user_id", how="right"
)
print(result)

result = pd.merge(
    users, scores, on="user_id", how="outer"
)
print(result)


# 総合問題
import pandas as pd
df = pd.read_csv("users.csv")

result = (
    df[df["score"] >= 70]
    .groupby("department")["score"]
    .mean()
    .sort_values(ascending=False)
)

print(result)

import pandas as pd

df = pd.DataFrame({
    "name": ["佐藤", "田中", "鈴木", "高橋", "伊藤"],
    "department": ["営業", "営業", "開発", "開発", "開発"],
    "score": [80, 60, 90, 75, 85]
})

print(df)

filtered_df = df[df["score"] >= 70]
print(filtered_df)
grouped = filtered_df.groupby("department")
# 営業と開発で別れただけ
print(grouped)
mean_score = grouped["score"].mean()
print(mean_score)
print(type(mean_score))
print(mean_score.reset_index())
result = mean_score.reset_index().sort_values("score", ascending=False)
print(result)