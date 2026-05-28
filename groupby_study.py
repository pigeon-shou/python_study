import pandas as pd

data = {
  "name": ["佐藤", "田中", "鈴木", "山田",],
  "team": ["A", "B", "A", "B"],
  "score": [80, 70, 90, 60]
}

df = pd.DataFrame(data)
print(df)

# teamで分けます。score列を対象にmean平均を計算
print(df.groupby("team")["score"].mean())
print(df.groupby("team")["score"].sum())
print(df.groupby("team")["score"].max())
print(df.groupby("team")["score"].count())

