import pandas as pd

data = {
    "name": ["佐藤", "田中", "鈴木", "山田", "高橋"],
    "team": ["A", "B", "A", "B", "A"],
    "year": [2024, 2024, 2025, 2025, 2024],
    "score": [80, 70, 90, 60, 100]
}

df =pd.DataFrame(data)
print(df)
# listで複数指定
print(df.groupby(["team", "year"])["score"].mean())
# multiindex化左側が特殊
result = df.groupby(["team", "year"])["score"].mean()
print(result.reset_index(drop=True))
print(result.reset_index())