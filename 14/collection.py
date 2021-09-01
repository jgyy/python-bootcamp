"""
104. Python Collections Module
"""
from collections import Counter, defaultdict, namedtuple

if __name__ == "__main__":
    mylist = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
    sentence = "Lorem ipsum, dolor sit amet consectetur adipisicing elit.".split()
    print(Counter(mylist))
    print(Counter("Lorem ipsum, dolor sit amet consectetur adipisicing elit."))
    print(Counter(sentence))
    count = Counter("qwertyuiopqwertyuiopqazwsxedcrfvqazqazqazqazqazqascqsxcqwsedfvg")
    print(count.most_common(4))
    print(list(count))
    default = defaultdict(lambda: 0)
    default["correct"] = 100
    print(default["wrong"])
    Dog = namedtuple("Dog", ["age", "breed", "name"])
    sammy = Dog(5, "husky", "Sam")
    print(sammy.name, sammy.age, sammy.breed)
