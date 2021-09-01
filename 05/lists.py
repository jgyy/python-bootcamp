"""
38: List comprehensions in python
"""

MYSTRING = "hello"
mylist = list(MYSTRING)
print(mylist)
mylist = list("wordtwo")
print(mylist)
mylist = [x ** 2 for x in range(0, 11)]
print(mylist)
mylist = [x ** 2 for x in range(0, 11) if x % 2 == 0]
print(mylist)

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheit)
results = [x if x % 2 == 0 else "ODD" for x in range(0, 11)]
print(results)

mylist = [x * y for x in [2, 4, 6] for y in [100, 200, 300]]
print(mylist)
