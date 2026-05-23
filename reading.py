with open("sample.txt", "r") as file:
    text = file.read()

print(text)

with open("memo.txt", "w") as file:
    file.write("Pyhton勉強中")

with open("sample2.txt", "r") as file:
    text2 = file.read()

print(text2)

with open("memo2", "w") as file:
    file.write("memo2に書き込み完了")