#!/usr/bin/env python3

dict = {
    "obj1": "computer",
    "obj2": "iphone"
}

# get value item by key
print(dict["obj1"])
# add item in dictionary
dict["obj3"] = "tablet"
# clear dictionary declared empty
dict = {}

# edit an item in a dictionary
dict["obj1"] = "mac"

print(dict)

# get keys and values
for k, v in dict.items():
    print(k, v)

# another way
for key in dict:
    print(key)
    print(dict[key])

# get only keys
for key in dict.keys():
    print(key)

# get only values
for values in dict.values():
    print(values)
