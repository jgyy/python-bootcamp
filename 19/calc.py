"""
Calculator
Have the user enter 2 number - a. b -
and an operator - op - and calculate
the solution - c - according to the
type of the given operator
"""


def calc(one, two, operator):
    """
    Returns a string like this: a op b = c
    where c is the computed value according to the opeartor
    """

    if operator == "+":
        return str(one) + " " + operator + " " + str(two) + " = " + str(one + two)
    if operator == "-":
        return str(one) + " " + operator + " " + str(two) + " = " + str(one - two)
    if operator == "*":
        return str(one) + " " + operator + " " + str(two) + " = " + str(one * two)
    if operator == "/":
        return str(one) + " " + operator + " " + str(two) + " = " + str(one / two)
    return 'Please only type one of these characters: "+, -, *, /"!'


def main():
    """
    Wrapper function
    """
    first = int(input("Please type the first number: "))
    second = int(input("Please type the second number: "))
    ope = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : '
    )

    print(calc(first, second, ope))


if __name__ == "__main__":
    main()
