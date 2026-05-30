import pandas as pd

users = pd.DataFrame(
  { "user_id": [1, 2, 3],
   "name": ["佐藤", "田中", "鈴木"]
  }
)

scores = pd.DataFrame({
    "user_id": [2, 3, 4],
    "score": [70, 90, 100]
})

pd.merge(
    users,
    scores,
    on="user_id",
    how="left"
)

print(scores)