sales = [
  {"name": "佐藤", "price": 1200},
  {"name": "田中", "price": 800},
  {"name": "佐藤", "price": 1500}
]
total = 0
for sale in sales:
    print(sale["name"])
    print(sale["price"])
    total = total + sale["price"]
    print(total)

total2 = 0
for sale in sales:
    if sale["name"] == "佐藤":
        total2 += sale["price"]

print(total2)

for sale in sales:
    if sale["price"] >= 1500:
        print(sale["price"])

count = 0
for sale in sales:
    count += 1

print(count)

total3 = []

for sale in sales:
    if sale["price"] >= 1000:
        total3.append(sale["price"])

print(total3)

name = "shohei"
print(name.upper())

data = {
    "name": [ "", "", "" ],
    "score": [60, 80, 30]
}

print(data.keys())
# dictはkey名data[""]listはindex

data2 = {
    "name": ["a", "b"],
    "score": [60, 80],
    "age": [20, 30],
    "height": [170, 180]
}
print(data2.keys())
# list化で無理やりindexをつける
keys = list(data2.keys())
print(keys)
print(keys[3])

# forでもとれる

count = 0

for key in keys:
    if count == 2:
        print(key)
    count += 1

# enumerateでindexをつけることも可能each_with_indexに似ている
for index, key in enumerate(data2.keys()):
    if index == 3:
        print(key)