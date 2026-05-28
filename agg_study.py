import pandas as pd

data = {
    "team": ["A", "B", "A", "B", "A"],
    "score": [80, 70, 90, 60, 100]
}
df = pd.DataFrame(data)
print(df)

# teamごとに分け　scoreを対象とし、複数あaggregation実行
print(df.groupby("team")["score"].agg(["mean", "max", "min"]))
print(df.groupby("team")["score"].agg(["mean", "max", "min", "count"]))
print(df.groupby("team")["score"].agg(["mean", "max", "min"]).reset_index())

print(df.sort_values("score").reset_index(drop=True))
print(df.sort_values("score", ascending=False).reset_index(drop=True))
print(df.sort_values(["score", "team"], ascending=False).reset_index())
print("全部森")
# sortlistは左から第一基準、第二基準、第３基準・・・と今回たまたまmeanで降順となったから変化がなかった

print(df.groupby("team")["score"].agg(["mean", "max", "count", "sum"]).sort_values(["mean", "max", "count", "sum"], ascending=False))
print(df.groupby("team")["score"].agg(["mean", "max", "count", "sum"]).sort_values(["mean", "max", "count", "sum"]))
df["country"] = "Japan"
print(df)
