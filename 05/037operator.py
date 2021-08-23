from random import shuffle, randint

for num in range(0, 11, 2):
    print(num)

word = "abcde"
for index, letter in enumerate(word):
    print("At index {} the letter is {}".format(index, letter))

mylist1 = [1, 2, 3, 4, 5, 6]
mylist2 = ["a", "b", "c"]
mylist3 = [100, 200, 300]
for a, b, c in zip(mylist1, mylist2, mylist3):
    print(b)

print(list(zip(mylist1, mylist2)))
print("x" in [1, 2, 3])
print("x" in ["x", "y", "z"])
print("a" in "a world")

d = {"mykey": 345}
print("mykey" in d)
print(345 in d.keys())
mylist = [10, 20, 30, 40, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(mylist))
print(max(mylist))

random_list = shuffle(mylist)
print(mylist)
print(type(random_list))
print(randint(0, 100))
output = int(input("Enter number here: "))
print(output)
print(type(output))
