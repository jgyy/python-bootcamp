"""
39: Python statement test overview
"""
STRING = "Print only the words that start with s in this sentence"
st_list = [s for s in STRING.split(" ") if s[0].lower() == "s"]
print(st_list)

# Use range() to print all the even numbers from 0 to 10.
print(list(range(0, 11, 2)))

# Use a List Comprehension to create a list of all numbers
# between 1 and 50 that are divisible by 3.
list_comp = [s for s in range(1, 51) if s % 3 == 0]
print(list_comp)

# Go through the string below and if the
# length of a word is even print "even!"
STRING = 'Print every word in this sentence that has an even number of letters'
st_word = ["even!" if len(s) % 2 == 0 else s for s in STRING.split(" ")]
print(st_word)

# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Use List Comprehension to create a list of the first letters of every word in the string below:
STRING = 'Create a list of the first letters of every word in this string'
st_first = [s[0] for s in STRING.split(" ")]
print(st_first)
