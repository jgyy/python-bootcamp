# Numbers
# Write an equation that uses multiplication, division, an
# exponent, addition, and subtraction that is equal to 100.25.
print(100 + 25)

# Answer these 3 questions without typing code. Then type code to check your answer.
# What is the value of the expression 4 * (6 + 5)
print(4 * (6 + 5))

# What is the value of the expression 4 * 6 + 5
print(4 * 6 + 5)

# What is the value of the expression 4 + 6 * 5
print(4 + 6 * 5)

# What is the type of the result of the expression 3 + 1.5 + 4?
print(type(3 + 1.5 + 4))

# What would you use to find a number’s square root, as well as its square?
# Square root:
print(100 ** 0.5)
# Square:
print(100 ** 2)

# Strings
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = "hello"
print(s[1])

# # Print out 'e' using indexing
# Reverse the string 'hello' using slicing:
print(s[::-1])

# # Reverse the string using slicing
# Given the string hello, give two methods of producing the letter 'o' using indexing.
print(s[4])
print(s[-1])

# Lists
# Build this list [0,0,0] two separate ways.
list1 = []
list1.append(0)
list1.append(0)
list1.append(0)
print(list1)
list2 = [0] + [0] + [0]
print(list2)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1, 2, [3, 4, "hello"]]
list3[2][2] = "goodbye"
print(list3)

# Sort the list below:
list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)

# Dictionaries
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {"simple_key": "hello"}
print(d["simple_key"])

d = {"k1": {"k2": "hello"}}
print(d["k1"]["k2"])

# # Getting a little tricker
d = {"k1": [{"nest_key": ["this is deep", ["hello"]]}]}
print(d["k1"][0]["nest_key"][1][0])

# # This will be hard and annoying!
d = {"k1": [1, 2, {"k2": ["this is tricky", {"tough": [1, 2, ["hello"]]}]}]}
print(d["k1"][2]["k2"][1]["tough"][2][0])

# Sets
# Use a set to find the unique values of the list below:
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))

# Booleans
print(2 > 3)
print(3 <= 2)
print(3 == 2.0)
print(3.0 == 3)
print(4 ** 0.5 != 2)

# Final Question: What is the boolean output of the cell block below?
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])
