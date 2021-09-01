"""
112. Timing Your Python Code
"""
from time import time
from timeit import timeit


def func_num(num, choice=False):
    """
    function one or two
    """
    if not choice:
        return [str(number) for number in range(num)]
    return list(map(str, range(num)))


if __name__ == "__main__":
    start_time = time()
    func_num(999999)
    end_time = time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    STATEMENT = "func_num(9)"
    SETUP = """
def func_num(num, choice=False):
    if not choice:
        return [str(number) for number in range(num)]
    return list(map(str, range(num)))
    """
    print(timeit(STATEMENT, SETUP, number=99999))
