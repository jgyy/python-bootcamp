"""
21: Lists in python
"""

my_list = [1, 2, 3, "STRING", 4.0]
print(my_list)
print(len(my_list))
mylist = ["one", "two", "three"]
print(mylist[0])
print(mylist[1:])
another_list = ["four", "five"]
new_list = mylist + another_list
print(another_list)
new_list[0] = "ONE ALL CAPS"
new_list.append("six")
print(new_list)
new_list.append("seven")
popped_item = new_list.pop()
print(popped_item)
print(new_list.pop(0))

new_list = ["a", "e", "x", "b", "c"]
num_list = [4, 1, 8, 3]
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
print(type(new_list.sort()))
my_sorted_list = new_list
print(my_sorted_list)
num_list.reverse()
print(num_list)
