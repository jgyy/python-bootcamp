my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)
print(my_dict["key1"])
price_lookup = {"apple": 2.99, "orange": 1.99, "milk": 5.80}
print(price_lookup["apple"])
d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insideKey": 100}, "key1": ["a", "b", "c"]}
print(d["k2"][2])
print(d["k3"]["insideKey"])
my_list = d["key1"]
print(my_list)
letter = my_list[2]
print(letter.upper())
print(d["key1"][2].upper())
d = {"k1": 100, "k2": 200}
d["k3"] = 300
d["k1"] = "NEW VALUE"
print(d)
print(d.keys())
print(d.values())
print(d.items())
