import pandas as pd

data = {
    "name": ["佐藤", "田中", "鈴木"],
    "score": [85, 40, 92]
}

df = pd.DataFrame(data)
print(df)

df["passed"] = True
print(df)
df["passed"] = df["score"] >= 60
# True/FalseのSeries　Booleanを変更するだけ
print(df)

df["10multi"] = df["score"] * 10
print(df)

df["over80"] = df["score"] >= 80
print(df)

df["name_copy"] = df["name"]
print(df)
print(df.dtypes)
print(type(df["passed"]))
print(type(df))