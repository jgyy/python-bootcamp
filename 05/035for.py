list_sum = 0
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    list_sum += num
    print(list_sum)

    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number: {num}")

mystring = "Hello World"
for letter in mystring:
    print(letter)

tup = (1, 2, 3)
for item in tup:
    print(item)

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
for a, b in mylist:
    print(a)
    print(b)

mylist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in mylist:
    print(b)

d = {"k1": 1, "k2": 2, "k3": 3}
for key, value in d.items():
    print(value)
