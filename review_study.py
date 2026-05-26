print("Hello Python")

name = "佐藤"
print(name)

a = 10
b = 3
print(a + b)

name = "田中"
print(f"こんにちは{name}さん")

data = ["python", "Ruby", "Java"]
print(data[1])
data.append("Go")
print(data)

score = 80
if score >= 80:
    print("合格")

age = 18
if age >= 20:
    print("成人")
else:
    print("未成年")

numbers = [1, 2, 3]
for number in numbers:
    print(number)

numbers = [3, 8, 12, 15]
for num in numbers:
    if num >= 10:
       print(num)
    
data = {
    "name": "佐藤",
    "age": 25
}

print(data["name"])

def call_name(name):
    print(f"こんにちは{name}さん")

call_name("佐藤")

class User:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"私は{self.name}です"


user = User("山口")
print(user.introduce())

user2 = User("田中")
print(user2.introduce())

import pandas as pd

data = { "name": ["佐藤", "田中"],
         "score": [80, 65] 
        }

df = pd.DataFrame(data)
print(df)

print(df[df["score"] >= 70])

numbers = [5, 12, 8, 20]
results = []
for num in numbers:
    if num >= 10:
        results.append(num)

print(results)
for result in results:
    print(result)

users = [
    {"name": "佐藤", "age": 20},
    {"name": "田中", "age": 17},
    {"name": "鈴木", "age": 25}
]    
for user in users:
    if user["age"] >= 20:
        print(user["name"])
# この処理をpandasなら print(df[df["age"] >= 20])でとってこれる

print(users[0]["name"])
print(users[2]["age"])
# 二十三問目
"生成されたuserというインスタンスが佐藤という値とintroduceという処理を持っているので、user.intruduceというメソッドと佐藤という値が使える"