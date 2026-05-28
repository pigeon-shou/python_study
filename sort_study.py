import pandas as pd
data = {
    "name": ["佐藤", "田中", "鈴木", "高橋"],
    "score": [85, 40, 92, 70]
}

df =pd.DataFrame(data)
print(df)
# 昇順が基本
print(df.sort_values("score"))
# 昇順を無効化＝降順
print(df.sort_values("score", ascending=False))
# 保存
sorted_df = df.sort_values("score")
print(sorted_df)
print("複数列")

data2 = {
  "name": ["satou", "tanaka", "suzuki", "takahasi", "abe"],
  "score": [85, 40, 92, 70, 70]
}
df2 = pd.DataFrame(data2)
# 一個だけなら""文字列を渡すが、複数条件つまり複数データならlist化して渡す
print(df2.sort_values(["score", "name"]))


print(df2.sort_values("score").reset_index())
print(df2.sort_values("score").reset_index(drop=True))

print("練習問題")
print(df2.sort_values("name"))
print(df2.sort_values("score", ascending=False))
print(df2.sort_values("score", ascending=False).reset_index(drop=True))