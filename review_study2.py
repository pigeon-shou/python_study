scores = [80, 60, 90]

for score in scores:
    print(score)

for index, score in enumerate(scores):
    print(index, score)

for index, score in enumerate(scores, start=1):
    print(index, score)

users = {
    "name": "佐藤",
    "age": 25
}
print(users["age"])

def add(x, y):
    return x + y

result = add(3, 5)
print(result)

# 期待されているデータ型と渡されたデータ型が違う場合TypeErrorとなる
# オブジェクトが存在しない場合はattribute error
numbers = [1, 2, 3]
print(numbers[0])

class User:
    pass
user1=User()
user2=User()
user3=User()

class User:
    def __init__(self, name):
        self.name = name

user = User("佐藤")
print(user.name)

users = []
user = User("佐藤")
users.append(user)

import pandas as pd
users = pd.DataFrame({ 
    "user_id": [1, 2, 3],
      "name": ["佐藤", "田中", "鈴木"]
})
scores = pd.DataFrame({
    "user_id": [2, 3, 4],
    "score": [70, 90, 50]
})
df2 = users
df = scores 
df["score"]
df[df["score"] >= 80]

df.head()

df["score"].mean()
df["score"].max()
# df.groupby("department")["salary"].mean()

# SELECT department,
# AVG(salary)
# From employees
# GROUP BY department;

# df=pd.DataFrame(department)
# df.groupby("employee")["salary"].mean()

# df.merge(users, scores, on="user_id")

df3 = pd.merge(users, scores, on="user_id", how="left")
print(df3)
#  SELECT * FROM employees;