"""
collatz script
"""


def collatz_recursion(cur_num, count=0):
    """This recursively solves the Collatz Conjecture"""
    if cur_num <= 1:  # Base case
        return count
    if cur_num % 2 == 0:
        return collatz_recursion(cur_num / 2, count + 1)
    return collatz_recursion(cur_num * 3 + 1, count + 1)


# Some tests
print(collatz_recursion(2))  # 1
print(collatz_recursion(3))  # 7
print(collatz_recursion(4))  # 2
print(collatz_recursion(5))  # 5
print(collatz_recursion(6))  # 8
