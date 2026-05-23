def judge_score(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"
    
print(judge_score(71))


def judge_score2(users):
    results = []
    for user in users:
        if user["score"] >= 60:
            result = f"{user["name"]}は合格です"
        else:
            result = f"{user["name"]}は不合格"
        results.append(result)
    return results

def judge_score3(users):
    for user in users:
        if user["score"] >= 60:
            print(f'{user["name"]}は合格です')
        else:
            print(f'{user["name"]}は不合格')
        
        
users = [
    {"name": "山口", "score": 55},
    {"name": "田中", "score": 88},
    {"name": "森本", "score": 100}
]

# forで回す
judge_score3(users)

# resultsに貯める
results = judge_score2(users)
for result in results:
    print(result)

class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def check_score(self):
        if self.score >= 60:
            print(f"{self.name}は合格です")
        else:
            print(f"{self.name}は不合格です")

user1 = User("yamaguchi", 90)
user2 = User("tanaka", 50)
user3 = User("mori", 70)

print(user1.name)
print(user1.score)
user1.check_score()

import json
with open("users2.json", "r") as file:
    users2 = json.load(file)

    print(users2)
def check_score(users2):
    results = []
    for user in users2:
        if user["score"] >= 60:
            result = f'{user["name"]}はごうかくです'
        else:
            result = f'{user["name"]}は不合格です'
        results.append(result)
    return results

results2 = check_score(users2)
for result in results2:
    print(result)