square = lambda num: num ** 2


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]


check_even = lambda num: num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]
print(list(map(square, my_nums)))
names = ["Andy", "Eve", "Sally"]
print(list(map(splicer, names)))
print(list(map(lambda x: x[0], names)))
print(list(filter(check_even, my_nums)))
print(square(3))
