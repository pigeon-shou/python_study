import pandas as ps

data = {
  "name": ["佐藤", "田中", "鈴木"],
  "score": [80, 65, 90]
}

df =ps.DataFrame(data)

print(df["score"])

print(df[df["score"] >= 80])

df["country"] = "japan"

df.loc[1, "score"] = 70

df.iloc[2, 1] = 95

df.loc[df["score"] <= 70, "score"]  = 0

print(df)
print(df["score"] >= 80)
# 問題８は上からTrue, False, Trueになります boolean(ブーリアン真偽値型)

data2 = {
  "name": ["佐藤", "田中", "鈴木", "高橋"],
  "status": ["ok", "error", "ok", "error"]
}

df2 = ps.DataFrame(data2)
print(df2)
print(df2[df2["status"] == "error"])
print(df2.dtypes)


