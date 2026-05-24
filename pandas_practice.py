import pandas as pd

data = {
  "name": ["佐藤", "山口", "田中"],
  "age": [25, 30, 22]
}

df = pd.DataFrame(data)
print(df)
print(df["name"])
#  表全体に一気に処理をかける
print(df[df["age"] >= 25])
print(df["age"])