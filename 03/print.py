"""
19: Print Formatting with strings
"""
print("This is a string {}".format("INSERTED"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
RESULT = 100 / 777
print("The RESULT was {r:1.3f}".format(r=RESULT))

NAME = "Jose"
AGE = 3
print(f"Hello, his NAME is {NAME}")
print(f"{NAME} is {AGE} years old")
