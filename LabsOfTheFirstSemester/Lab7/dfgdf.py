class Example:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def add_scores(self, points):
        self.score += points
    def __str__(self):
        return f"name:{self.name} scores:{self.score}"

ex1 = Example("chlen", 10)
ex1.add_scores(1000)
print(ex1)
