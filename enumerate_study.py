names = ["佐藤", "田中", "鈴木",]

for name in names:
    print(name)

for index, name in enumerate(names):
    print(index)
    print(name)

for index, name in enumerate(names, start=1):
    print(index, name)


scores = [80, 50, 90]

for index, score in enumerate(scores):
    print(index, score)

for index, score in enumerate(scores, start=1):
    print(index, score)

for index, score in enumerate(scores):
    if index == 2:
        print(index, score)


