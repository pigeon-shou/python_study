import pandas as pd

data = {
  "name": ["佐藤","田中","鈴木", "高橋"],
  "score": [85, 40, 92, 70]
}

df =pd.DataFrame(data)
print(df)
print(df["score"] >= 80)
print(df[df["score"] >= 80])

print(df[(df["score"] >= 70) &  (df["score"] <= 90)])

print("ここから練習")
print(df[df["score"] <= 80])
print(df[df["name"] == "高橋"])
print(df[(df["score"] >= 50) & (df["score"] <= 90)])

print("２段階取得")
print(df[df["score"] >=80]["name"])
print(df[["name", "score"]])
print("SeriesとDFの違い")
print(df["name"])
print(df[["name"]])

print(df["name"].shape)
print(df[["name"]].shape)