import pandas as pd

data = {
  "name": ["佐藤", "田中", "鈴木"],
  "age": [25, 30, 22]
}

df = pd.DataFrame(data)

print(df)
print(df["name"])
# 行を取り出す時
print(df.loc[0])
# 条件で絞る時
adult = df[df["age"] >= 25]
print(adult)

# 追加
df["country"] = "Japan"
print(df["country"])

df.loc[1, "age"] = 35
df.iloc[2,1] = 19
print(df)
# 行を指定、　その後にカラムを指定
df.loc[df["age"] < 25, "age"] = 0
# 真偽値の判定をdfに渡す必要がある
print(df[df["age"] == 0])