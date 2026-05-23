# for = eachと同じようなもの
fruits = ["banana", "apple", "orange"]
for fruit in fruits:
    print(fruit)

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"{fruit}が入ってます")

nums = [111, 11, 17, 23]
for num in nums:
    print(str(num) + "は素数です")

name1 = input("一人目")
name2 = input("二人目")
name3 = input("３人目")

names = [name1, name2, name3]

for name in names:
    print(f"私は{name}です")

numbers = [11, 13, 37, 83]
for number in numbers:
    if number >= 20:
        print(f"{number}は20以上です")

numbers = [3, 8, 15]
for num in numbers:
    if num >= 10:
        print(f"{num}は10以上です")