class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def check_score(self):
        if self.score >= 60:
            #  printは表示するだけ返り値としてはnone
             return f"{self.name}さんは合格"
        else:
            return f"{self.name}さんは不合格"

user1 = User("yamaguchi", 100)
print(user1.name)
print(user1.score)
print(user1.check_score())
    