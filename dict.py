# dict = ハッシュのようなもの
user = {
  "name":"Shohei",
  "age": 32,
  "country": "Japan"
}

print(user["name"])
print(user["country"])

def where_from(user):
    if user["country"] == "Japan":
        return "日本出身"
    else:
        return "海外出身"

result = where_from(user)
print(f"私は{result}です")
print(f"私は{where_from(user)}です")

# list = 配列 list(配列）の中にdict（ハッシュ）が入っている
users = [
    {"name": "佐藤", "score": 80},
    {"name": "田中", "score": 50},
    {"name": "鈴木", "score": 100}
]

for user in users:
    print(user["score"])

def score_check(users):
    results = []
    for user in users:
        if user["score"] >= 60:
            results.append(f"{user["name"]}さんは合格")
        else:
             results.append(f"{user["name"]}さんは不合格")
    return results

results = score_check(users)

for result in results:
    print(result)
    
