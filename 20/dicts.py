"""
141. Advanced Dictionaries
"""
d = {"k1": 1, "k2": 2}
print(d)
print({x: x ** 2 for x in range(10)})
print({x: y ** 2 for x, y in zip(["a", "b", "c"], range(3))})
for k in d.items():
    print(k)
print(d.items())
print(d.keys())
print(d.values())
