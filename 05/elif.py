"""
34. If Elif and Else Statements in Python
"""

HUNGRY = True
if HUNGRY:
    print("FEED ME!")
else:
    print("I'm not HUNGRY.")

LOCATION = "Bank"
if LOCATION == "Auto Shop":
    print("Cars are cool!")
elif LOCATION == "Bank":
    print("Money is cool!")
elif LOCATION == "Store":
    print("Welcome to the store!")
else:
    print("I do not know much.")

NAME = "Sammy"
if NAME == "Frankie":
    print("Hello Frankie!")
elif NAME == "Sammy":
    print("Hello Sammy!")
else:
    print("What is your NAME?")
