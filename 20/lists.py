"""
142. Advanced Lists
"""
l = [1, 2, 3]
l.append(4)
print(l)
print(l.count(10))
print(l.count(1))
x = [1, 2, 3]
x.append([4, 5])
print(x)
y = [1, 2, 3]
y.extend([4, 5])
print(y)
print(l.index(2))
l.insert(2, "inserted")
print(l)
ele = l.pop()
print(ele)
l.remove("inserted")
print(l)
