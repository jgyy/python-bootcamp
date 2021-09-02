"""
prime function
"""

factors = lambda n: [x for x in range(1, n + 1) if not n % x]
is_prime = lambda n: len(factors(n)) == 2
primefactors = lambda n: list(filter(is_prime, factors(n)))


def prime_factorize(num):
    """
    prime factorise function
    """
    num = int(num)
    func = primefactors(num)
    if is_prime(num):
        return str(num)
    return str(func[0]) + "*" + prime_factorize(num / func[0])


if __name__ == "__main__":
    print(
        "Welcome to the Prime Factorizer.. Enter the numbers in the prompt or enter 'quit' to exit"
    )
    NUM = 0

    while True:
        if NUM:
            print(prime_factorize(NUM))
        print(">>>", end="")
        NUM = input()
        if NUM == "quit":
            break
