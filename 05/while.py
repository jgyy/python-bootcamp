"""
36: While loops in python
"""

AXE = 0
while AXE < 5:
    if AXE == 2:
        break
    print(f"The current value of AXE is {AXE}")
    AXE += 1
else:
    print("X IS NOT LESS THAN 5")

AXE = [1, 2, 3]
for item in AXE:
    # comment
    pass

MYSTRING = "Sammy"
for letter in MYSTRING:
    if letter == "a":
        continue
    if letter == "m":
        break
    print(letter)
