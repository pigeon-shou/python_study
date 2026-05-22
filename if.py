# if
age = int(input("年齢を入力してください"))
print(age)

age = int(input("年は？"))

if age >= 20:
    print("成人しています")
else:
    print("未成年です")    
                
name = input("名前を入力してください")
age = int(input("年齢を入力してください"))

if age >= 18:
    print(f"{name}さんは{age}才なので選挙権があります")
else:
    print(f"{name}さんは{age}なので選挙権がありません")    
