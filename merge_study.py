import pandas as pd

users = pd.DataFrame({
    "user_id": [1, 2, 3],
    "name": ["佐藤", "田中", "鈴木"]
})

print(users)

scores = pd.DataFrame({
    "user_id": [1, 2, 3],
    "score": [80, 70, 90]
})

print(scores)

result = pd.merge(users, scores, on="user_id")

print(result)

users2 = pd.DataFrame(
  { "user_id": [1, 2, 3],
   "name": ["佐藤", "田中", "鈴木"]
  })

scores2= pd.DataFrame({
  "user_id": [1, 2, 4],
  "score": [80, 70, 100]
})
print("練習")
print(users2)
print(scores2)
# 共通部分だけ
result = pd.merge(users2, scores2, on = "user_id", how = "inner")
print(result)
#  left　左の引数を基準に NaN= not a number
result2 = pd.merge(users2, scores2, on = "user_id", how = "left")
print(result2)

# right 右を基準に残す
result3 = pd.merge(users2, scores2, on = "user_id", how = "right")
print(result3)

# outer全部残す
result4 = pd.merge(users2, scores2, on = "user_id", how = "outer"  ) 
print(result4)