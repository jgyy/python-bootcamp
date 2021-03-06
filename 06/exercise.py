"""
50: Function practive overview exercise
"""


def lesser_of_two_evens(aaa, bbb):
    """
    function that compare lesser of 2 evens
    """
    if aaa % 2 == 1 or bbb % 2 == 1:
        return max(aaa, bbb)
    return min(aaa, bbb)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))

# ANIMAL CRACKERS: Write a function takes a two-word string
# and returns True if both words begin with same letter
def animal_crackers(text):
    """
    function that compare lesser of 2 evens
    """
    text_list = text.split(" ")
    return text_list[0][0] == text_list[1][0]


print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Kangaroo"))

# MAKES TWENTY: Given two integers, return True
# if the sum of the integers is 20 or if one of
# the integers is 20. If not, return False
def makes_twenty(one, two):
    """
    function that compare lesser of 2 evens
    """
    return one == 20 or two == 20 or one + two == 20


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))

# OLD MACDONALD: Write a function that capitalizes
# the first and fourth letters of a name
def old_macdonald(name):
    """
    function that compare lesser of 2 evens
    """
    word = ""
    for num in enumerate(len(name)):
        if num in (0, 3):
            word += name[num].capitalize()
        else:
            word += name[num]
    return word


print(old_macdonald("macdonald"))

# MASTER YODA: Given a sentence, return
# a sentence with the words reversed
def master_yoda(text):
    """
    function that compare lesser of 2 evens
    """
    text_list = text.split(" ")
    text_list.reverse()
    return " ".join(text_list)


print(master_yoda("I am home"))
print(master_yoda("We are ready"))

# ALMOST THERE: Given an integer n, return True
# if n is within 10 of either 100 or 200
def almost_there(num):
    """
    function that compare lesser of 2 evens
    """
    return 90 <= num <= 110 or 190 <= num <= 210


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# FIND 33:
# Given a list of ints, return True if the array
# contains a 3 next to a 3 somewhere.
def has_33(nums):
    """
    function that compare lesser of 2 evens
    """
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# PAPER DOLL: Given a string, return a string where for every
# character in the original there are three characters
def paper_doll(text):
    """
    function that compare lesser of 2 evens
    """
    long_text = ""
    for string in text:
        long_text += string * 3
    return long_text


print(paper_doll("Hello"))
print(paper_doll("Mississippi"))

# BLACKJACK: Given three integers between 1 and 11, if their
# sum is less than or equal to 21, return their sum. If their
# sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(aaa, bbb, ccc):
    """
    function that compare lesser of 2 evens
    """
    total = sum((aaa, bbb, ccc))
    if 11 in (aaa, bbb, ccc):
        total -= 10
    return "BUST" if total > 21 else total


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at
# least one 9). Return 0 for no numbers.
def summer_69(arr):
    """
    function that compare lesser of 2 evens
    """
    total = 0
    add = True
    for number in arr:
        if number == 6 and add is True:
            add = False
        if add:
            total += number
        if number == 9 and add is False:
            add = True
    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# SPY GAME: Write a function that takes in a list of
# integers and returns True if it contains 007 in order
def spy_game(nums):
    """
    function that compare lesser of 2 evens
    """
    num_string = [str(n) for n in nums]
    spy_list = list(filter(lambda x: x in ("0", "7"), num_string))
    if len(spy_list) > 0:
        spy = "".join(spy_list)
        return spy == "007"
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# COUNT PRIMES: Write a function that returns the number of
# prime numbers that exist up to and including a given number
def count_primes(num):
    """
    function that compare lesser of 2 evens
    """
    num_list = list(range(2, num + 1))
    not_prime = []
    for xxx in num_list:
        for yyy in num_list:
            not_prime.append(xxx * yyy)
    not_prime = set(not_prime)
    prime = set(filter(lambda x: x not in not_prime, num_list))
    return len(prime)


print(count_primes(100))
