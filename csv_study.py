import csv
with open("users.csv", "r") as file:
    # csvを一行ずつ読むreaderメソッド、csvのモジュール
    reader = csv.reader(file)
# 一行目を飛ばす
    next(reader)
    results = []
    for row in reader:
        name = row[0]
        score = int(row[1])

        

        if score >= 60:
            result = f"{name}さんは合格です"
        else:
            result = f"{name}さんは不合格です"
        
        results.append(result)
    
    for result in results:
        print(result)