import json
with open("users.json", "r") as file:
    users =json.load(file)

    print(users)

    for user in users:
        print(user["name"])
        print(user["score"])
    
    results = []
    
    for user in users:
        if user["score"] >= 60:
            result = f"{user["name"]}さんは合格です"
        else:
            result = f"{user["name"]}さんは不合格です"
        
        results.append(result)
    
    for result in results:
        print(result)