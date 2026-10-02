# ============================================================
# Python Dictionaries
# ============================================================

# ============================================================
# What is a Dictionary?
# ============================================================

# A Dictionary is a built-in Python data type used to store
# data in KEY : VALUE pairs.
#
# Each item consists of:
#
# key : value
#
# Example:
# "brand" : "Ford"
#
# Dictionaries are:
# ✔ Ordered (Python 3.7+)
# ✔ Changeable (Mutable)
# ✔ Do NOT allow duplicate keys
#
# Dictionaries are written using curly braces {}.


# ============================================================
# Creating a Dictionary
# ============================================================

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Print the dictionary

# print(thisdict)


# ============================================================
# Dictionary Items
# ============================================================

# Every dictionary item consists of:
#
# key : value
#
# Example:
#
# "brand" : "Ford"
#    ↑         ↑
#   Key      Value
#
# Keys must be unique.
# Values can be duplicated.


# ============================================================
# Accessing Dictionary Items
# ============================================================

# Dictionary values are accessed using their KEY,
# not an index.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Access the value of "brand"

# print(thisdict["brand"])

# Output:
# Ford


# ============================================================
# Ordered Dictionaries
# ============================================================

# Since Python 3.7,
# dictionaries preserve insertion order.

student = {
    "name": "Ali",
    "age": 20,
    "course": "MCA",
}

# print(student)

# The order remains:
#
# name
# age
# course


# ============================================================
# Changeable Dictionaries
# ============================================================

# Dictionaries are mutable.
#
# You can:
# ✔ Change values
# ✔ Add new items
# ✔ Remove items

car = {
    "brand": "Ford",
    "year": 1964
}
# print(car)

car["year"] = 2020

# print(car)


# ============================================================
# Duplicate Keys
# ============================================================

# Duplicate keys are NOT allowed.
#
# The last value overwrites the previous one.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

# print(thisdict)

# Output:
#
# {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 2020
# }


# ============================================================
# Dictionary Length
# ============================================================

# len() returns the number of key:value pairs.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# print(len(thisdict))

# Output:
# 3


# ============================================================
# Dictionary Data Types
# ============================================================

# Dictionary values can be any data type.

thisdict = {
    "brand": "Ford",             # String
    "electric": False,           # Boolean
    "year": 1964,                # Integer
    "colors": ["red", "white"]   # List
}

# print(thisdict)


# ============================================================
# Data Type of a Dictionary
# ============================================================

# type() returns the data type.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# print(type(thisdict))

# Output:
# <class 'dict'>


# ============================================================
# Creating a Dictionary Using dict()
# ============================================================

# Another way to create a dictionary is by using
# the dict() constructor.

person = dict(
    name="John",
    age=36,
    country="Norway"
)

# print(person)


# ============================================================
# Python Collection Types
# ============================================================

# List
# -----------------------
# Ordered      ✔
# Changeable   ✔
# Duplicates   ✔

# Tuple
# -----------------------
# Ordered      ✔
# Changeable   ✘
# Duplicates   ✔

# Set
# -----------------------
# Ordered      ✘
# Changeable   ✔
# Duplicates   ✘

# Dictionary
# -----------------------
# Ordered      ✔
# Changeable   ✔
# Duplicate Keys ✘


# ============================================================
# Accessing Dictionary Items
# ============================================================

# Access values using square brackets [].

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

model = thisdict["model"]

# print(model)


# ============================================================
# Using get()
# ============================================================

# get() also retrieves a value using its key.

model = thisdict.get("model")

# print(model)

# Difference:
#
# [] raises an error if the key does not exist.
#
# get() returns None instead.


# ============================================================
# Getting All Keys
# ============================================================

# keys() returns all keys.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

keys = car.keys()

# print(keys)

# Output:
#
# dict_keys(['brand', 'model', 'year'])


# ============================================================
# keys() Returns a Dynamic View
# ============================================================

# The returned object automatically updates
# if the dictionary changes.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

keys = car.keys()

# print(keys)      # Before change

car["color"] = "white"

# print(keys)      # After change


# ============================================================
# Getting All Values
# ============================================================

# values() returns every value.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

values = car.values()

# print(values)


# ============================================================
# values() Updates Automatically
# ============================================================

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

values = car.values()

# print(values)      # Before

car["year"] = 2020

# print(values)      # After


# ============================================================
# Adding New Values
# ============================================================

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

values = car.values()

# print(values)

car["color"] = "Red"

# print(values)


# ============================================================
# Getting All Items
# ============================================================

# items() returns every key:value pair
# as tuples.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

items = car.items()

# print(items)

# Output:
#
# dict_items([
# ('brand','Ford'),
# ('model','Mustang'),
# ('year',1964)
# ])


# ============================================================
# items() Updates Automatically
# ============================================================

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

items = car.items()

# print(items)

car["year"] = 2020

# print(items)


# ============================================================
# Adding Items After Calling items()
# ============================================================

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

items = car.items()

# print(items)

car["color"] = "Red"

# print(items)


# ============================================================
# Checking if a Key Exists
# ============================================================

# Use the "in" keyword.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "model" in thisdict:
    # print("Yes, 'model' exists in the dictionary.")
    pass

# If the key exists,
# the condition evaluates to True.


# ============================================================
# Difference Between [] and get()
# ============================================================

# [] Operator
# ----------------------------
# ✔ Fast
# ✔ Raises KeyError if key is missing.

# Example:
#
# value = thisdict["price"]   ❌ KeyError


# get() Method
# ----------------------------
# ✔ Safe
# ✔ Returns None if key is missing.

# Example:
#
# value = thisdict.get("price")
#
# Result:
# None


# ============================================================
# Summary of Common Dictionary Methods
# ============================================================

# get(key)
# ----------------------------
# Returns the value of a key.

# keys()
# ----------------------------
# Returns all keys.

# values()
# ----------------------------
# Returns all values.

# items()
# ----------------------------
# Returns all key:value pairs as tuples.

# len(dict)
# ----------------------------
# Returns the number of items.

# type(dict)
# ----------------------------
# Returns <class 'dict'>.


# ============================================================
# Quick Summary
# ============================================================

# ✔ Dictionaries store data as key:value pairs.
# ✔ Dictionaries are ordered (Python 3.7+).
# ✔ Dictionaries are mutable (changeable).
# ✔ Duplicate keys are NOT allowed.
# ✔ Values can be of any data type.
# ✔ Access values using keys, not indexes.
# ✔ Use get() for safe access.
# ✔ keys() returns all keys.
# ✔ values() returns all values.
# ✔ items() returns key:value tuples.
# ✔ keys(), values(), and items() return dynamic views that
#   automatically reflect dictionary changes.
# ✔ Use "in" to check if a key exists.

# -------------------------------------------------------------------------------------------------------------------

# ============================================================
# Python Dictionaries - Change, Add, Remove, Loop, Copy,
# Nested Dictionaries & Dictionary Methods
# ============================================================

# ============================================================
# Changing Dictionary Items
# ============================================================

# Dictionaries are mutable (changeable).
#
# You can:
# ✔ Change existing values
# ✔ Add new key:value pairs
# ✔ Remove key:value pairs


# ============================================================
# Change a Value Using the Key
# ============================================================

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Change the value of "year"

thisdict["year"] = 2018

# print(thisdict)

# Output:
# {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 2018
# }


# ============================================================
# update() Method
# ============================================================

# update() updates one or more key:value pairs.
#
# If the key already exists:
#     ✔ Value is updated.
#
# If the key does NOT exist:
#     ✔ A new key:value pair is added.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.update({"year": 2020})

# print(thisdict)


# ============================================================
# Change Value vs update()
# ============================================================

# Using []

thisdict["year"] = 2024

# Using update()

thisdict.update({"year": 2025})

# Both perform the same task.


# ============================================================
# Adding Dictionary Items
# ============================================================

# New items are added by assigning
# a value to a NEW key.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["color"] = "Red"

# print(thisdict)


# ============================================================
# Adding Items Using update()
# ============================================================

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.update({"color": "Red"})

# print(thisdict)

# Since "color" does not exist,
# update() creates it.


# ============================================================
# Removing Dictionary Items
# ============================================================

# Common methods:
#
# pop()
# popitem()
# del
# clear()


# ============================================================
# pop()
# ============================================================

# Removes a key:value pair
# using the specified key.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.pop("model")

# print(thisdict)


# ============================================================
# popitem()
# ============================================================

# Removes the LAST inserted item.
#
# (Python 3.7+)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.popitem()

# print(thisdict)

# Output:
#
# {
#     "brand":"Ford",
#     "model":"Mustang"
# }


# ============================================================
# del Keyword
# ============================================================

# Delete one key:value pair.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del thisdict["model"]

# print(thisdict)


# ============================================================
# Delete Entire Dictionary
# ============================================================

thisdict = {
    "brand": "Ford",
    "model": "Mustang"
}

del thisdict

# The following line causes an error because
# the dictionary no longer exists.

# print(thisdict)


# ============================================================
# clear()
# ============================================================

# Removes every key:value pair.
#
# The dictionary still exists.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.clear()

# print(thisdict)

# Output:
# {}


# ============================================================
# Looping Through Dictionaries
# ============================================================

# By default,
# looping through a dictionary returns KEYS.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for key in thisdict:
    # print(key)
    pass


# ============================================================
# Loop Through Values
# ============================================================

# Method 1

for key in thisdict:
    # print(thisdict[key])
    pass


# Method 2

for value in thisdict.values():
    # print(value)
    pass


# ============================================================
# Loop Through Keys
# ============================================================

for key in thisdict.keys():
    # print(key)
    pass


# ============================================================
# Loop Through Keys and Values
# ============================================================

# items() returns both key and value.

for key, value in thisdict.items():
    # print(key, value)
    pass


# ============================================================
# Copying Dictionaries
# ============================================================

# ============================================================
# Incorrect Way
# ============================================================

# This does NOT create a copy.

dict1 = {
    "brand": "Ford",
    "year": 1964
}

dict2 = dict1

# Both variables point to the SAME dictionary.

dict1["year"] = 2024

# print(dict2)

# dict2 also changes!


# ============================================================
# copy() Method
# ============================================================

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = thisdict.copy()

# print(mydict)

# Now both dictionaries are independent.


# ============================================================
# dict() Constructor
# ============================================================

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = dict(thisdict)

# print(mydict)


# ============================================================
# copy() vs =
# ============================================================

# =
# -----------------------
# Creates a reference.

# copy()
# -----------------------
# Creates a new dictionary.

# dict()
# -----------------------
# Also creates a new dictionary.


# ============================================================
# Nested Dictionaries
# ============================================================

# A dictionary can contain other dictionaries.

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# print(myfamily)


# ============================================================
# Another Way to Create Nested Dictionaries
# ============================================================

child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year": 2007
}

child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# print(myfamily)


# ============================================================
# Access Nested Dictionary Items
# ============================================================

# Syntax:
#
# dictionary["outer_key"]["inner_key"]

# print(myfamily["child2"]["name"])
# print(myfamily["child1"]["year"])

# Output:
# Tobias


# ============================================================
# Loop Through Nested Dictionaries
# ============================================================

for child, details in myfamily.items():

    # print(child)

    for key in details:
        # print(key + ":", details[key])
        pass


# ============================================================
# Common Dictionary Methods
# ============================================================

# clear()
# --------------------------
# Removes all items.

# copy()
# --------------------------
# Returns a copy.

# fromkeys()


# --------------------------
# Creates a dictionary using given keys.

# get()
# --------------------------
# Returns the value of a key.
# keys()

# --------------------------
# Returns key:value pairs.

# items()
# Returns all keys.
# --------------------------

# pop()
# --------------------------
# Removes a specified key.

# popitem()
# --------------------------
# Removes the last inserted item.

# setdefault()
# --------------------------
# Returns the value of a key.
# If the key doesn't exist,
# it inserts the key with the default value.

# update()
# --------------------------
# Updates or adds key:value pairs.

# values()
# --------------------------
# Returns all values.


# ============================================================
# Quick Comparison of Dictionary Methods
# ============================================================

# Change Value
# --------------------------
# dict[key] = value
# update()

# Add Item
# --------------------------
# dict[new_key] = value
# update()

# Remove Item
# --------------------------
# pop()
# popitem()
# del
# clear()

# Access Data
# --------------------------
# get()
# keys()
# values()
# items()

# Copy Dictionary
# --------------------------
# copy()
# dict()


# ============================================================
# Quick Summary
# ============================================================

# ✔ Dictionaries are mutable.
# ✔ Change values using [] or update().
# ✔ Add new items using [] or update().
# ✔ Remove items using pop(), popitem(), del(), or clear().
# ✔ Looping over a dictionary returns keys by default.
# ✔ Use values() to loop through values.
# ✔ Use keys() to loop through keys.
# ✔ Use items() to loop through both keys and values.
# ✔ Use copy() or dict() to create an independent copy.
# ✔ Using "=" only creates a reference.
# ✔ Dictionaries can contain other dictionaries (nested dictionaries).
# ✔ Access nested values using multiple keys.
# ✔ items() is useful for looping through nested dictionaries.
