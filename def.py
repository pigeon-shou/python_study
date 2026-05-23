def greet():
    print("こんにちは")

greet()
greet()
greet()

def greet(name):
    print(f"こんにちは{name}さん")

greet("shohei")

names = ["佐藤", "田中", "山口"]

for name in names:
    greet(name)

def double(number):
    return number * 2

result = double(5)
print(result)
print(double(7))

def square(number):
    return number ** 2

result = square(4)

print(result)

def diff(num):
    print(num - 50)

diff(70)


def multi(number):
    return number * 2

numbers = [1, 2, 3, 4]

for number in numbers:
    print(multi(number))

def div(num):
    return num / 2
    

# print(result_1)
print(div(110))

def check_even(number):
    if number % 2 == 0:
        return "偶数"
    else:
        return "奇数"

print(check_even(221))

scores = [50, 80, 30, 100]

def checker_60(score):
    if score >= 60:
        return "合格"
    else:
        return  "不合格"
    

for score in scores:
    result = checker_60(score)
    print(result)