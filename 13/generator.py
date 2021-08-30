"""
100. Generators with Python
"""


def create_cubes(nums):
    """
    function to return cubes
    """
    for num in range(nums):
        yield num ** 3


def gen_fibon(nums):
    """
    generating fibonachi
    """
    num_a = 1
    num_b = 1
    for _ in range(nums):
        yield num_a
        num_a, num_b = num_b, num_a + num_b


def simple_gen(nums):
    """
    generator function
    """
    for num in range(nums):
        yield num


if __name__ == "__main__":
    for cube in create_cubes(99):
        print("cubes:", cube)
    for fib in create_cubes(99):
        print("fib:", fib)
    gen = simple_gen(9)
    print(next(gen))
    print(next(gen))
    STR = "HELLO"
    siter = iter(STR)
    print(next(siter))
    print(next(siter))
