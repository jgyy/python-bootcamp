"""
140. Advanced Sets
"""
s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)
sc = s.copy()
s.add(4)
print(sc)
print(s.difference(sc))
s1 = {1, 2, 3, 4}
s2 = {1, 4, 5, 6}
s1.difference_update(s2)
print(s1)
s.discard(2)
s1.add(1)
print(s)
print(s1.intersection(s2))
s3 = {5}
print(s1.isdisjoint(s3))
print(s2.issuperset(s1))
s1.update(s2)
