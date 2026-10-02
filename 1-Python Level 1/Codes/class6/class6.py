# ============================================================
# PYTHON LISTS - SORT, COPY, JOIN & LIST METHODS
# ============================================================
#
# Topics Covered:
# 1. sort() - Ascending Sort
# 2. sort(reverse=True) - Descending Sort
# 3. Custom Sorting using key=
# 4. Case Sensitive Sorting
# 5. Case Insensitive Sorting
# 6. reverse() Method
# 7. Copying Lists
#    - copy()
#    - list()
#    - Slice Operator (:)
# 8. Joining Lists
#    - + Operator
#    - append() in Loop
#    - extend()
# 9. Complete List Methods Reference
#
# ============================================================


# ============================================================
# 1. SORT LIST (ALPHABETICALLY)
# ============================================================

# sort() sorts the original list in ascending order.

thislist = [
    "orange",
    "mango",
    "kiwi",
    "pineapple",
    "banana"
]

thislist.sort()

# print(thislist)

# Output:
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']


# ------------------------------------------------------------
# Sorting Numbers
# ------------------------------------------------------------

thislist = [
    100,
    50,
    65,
    82,
    23
]

thislist.sort()

# print(thislist)

# Output:
# [23, 50, 65, 82, 100]


# ============================================================
# 2. SORT DESCENDING
# ============================================================

# Use reverse=True

thislist = [
    "orange",
    "mango",
    "kiwi",
    "pineapple",
    "banana"
]

thislist.sort(reverse=True)

# print(thislist)

# Output:
# ['pineapple', 'orange', 'mango', 'kiwi', 'banana']


# ------------------------------------------------------------
# Descending Numeric Sort
# ------------------------------------------------------------

thislist = [
    100,
    50,
    65,
    82,
    23
]

thislist.sort(reverse=True)

# print(thislist)

# Output:
# [100, 82, 65, 50, 23]


# ============================================================
# 3. CUSTOM SORT USING key=
# ============================================================

# key allows us to define our own sorting rule.

# Example:
# Sort numbers according to
# how close they are to 50.

# ---------------------------------------------------
# print(abs(-20))     
# print(abs(3.14))    
# print(abs(-0.0))

# price_yesterday = 150
# price_today = 135

# difference = abs(price_yesterday - price_today)
# print(difference) 

# ---------------------------------------------------
def myfunc(n):
    print("Run", n)
    return abs(n - 50)


thislist = [
    100,
    50,
    65,
    82,
    23
]

# thislist.sort(key=myfunc)
# print(thislist)

# Output:
# [50, 65, 23, 82, 100]

# Explanation:
#
# Distance from 50:
#
# 50  -> 0
# 65  -> 15
# 23  -> 27
# 82  -> 32
# 100 -> 50
#
# Smaller distance comes first.


# ============================================================
# 4. CASE SENSITIVE SORT
# ============================================================

# By default, sort() is case-sensitive.

thislist = [
    "banana",
    "Orange",
    "Kiwi",
    "cherry"
]

thislist.sort()

# print(thislist)

# Output:
# ['Kiwi', 'Orange', 'banana', 'cherry']

# Explanation:
#
# Capital letters come before
# lowercase letters in ASCII/Unicode.
# in ASCII, uppercase letters (A-Z) range from 65 to 90, and lowercase letters (a-z) range from 97 to 122

# ============================================================
# 5. CASE INSENSITIVE SORT
# ============================================================

# Use key=str.lower

thislist = [
    "banana",
    "Orange",
    "Kiwi",
    "cherry"
]

thislist.sort(key=str.lower)

# print(thislist)

# Output:
# ['banana', 'cherry', 'Kiwi', 'Orange']

# Explanation:
#
# Every item is temporarily converted
# to lowercase before comparison.


# ============================================================
# 6. REVERSE ORDER
# ============================================================

# reverse() simply reverses
# the current order of the list.

thislist = [
    "banana",
    "Orange",
    "Kiwi",
    "cherry"
]

thislist.reverse()

# print(thislist)

# Output:
# ['cherry', 'Kiwi', 'Orange', 'banana']

# NOTE:
#
# reverse()
# DOES NOT SORT.
#
# It only reverses the existing order.


# ============================================================
# DIFFERENCE:
# sort() vs reverse()
# ============================================================

# sort()
#
# ✔ Sorts items
# ✔ Ascending by default
#
# Example:
#
# [3,1,2]
# becomes
# [1,2,3]


# reverse()
#
# ✔ Only reverses order
#
# Example:
#
# [3,1,2]
# becomes
# [2,1,3]


# ============================================================
# 7. COPY A LIST
# ============================================================

# ------------------------------------------------------------
# Wrong Way
# ------------------------------------------------------------

list1 = [
    "apple",
    "banana",
    "cherry"
]

list2 = list1

# list2 is NOT a new list.
#
# Both variables point to
# the SAME object.

# list1.append("orange")
# print(list2)

# Output:
# ['apple', 'banana', 'cherry', 'orange']


# ============================================================
# A. copy() METHOD
# ============================================================

thislist = [
    "apple",
    "banana",
    "cherry"
]

mylist = thislist.copy()
# print(mylist)

thislist.append("orange")
# print(mylist)

# Output:
# ['apple', 'banana', 'cherry']

# Creates a separate copy.


# ============================================================
# B. list() CONSTRUCTOR
# ============================================================

thislist = [
    "apple",
    "banana",
    "cherry"
]

mylist = list(thislist)

# print(mylist)

# Output:
# ['apple', 'banana', 'cherry']


# ============================================================
# C. SLICE OPERATOR
# ============================================================

thislist = [
    "apple",
    "banana",
    "cherry"
]

mylist = thislist[:]
# thislist.append("New")

# print(thislist)
# print(mylist)

# Output:
# ['apple', 'banana', 'cherry']

# [:]
# Copies the entire list.


# ============================================================
# 8. JOIN LISTS
# ============================================================

# ------------------------------------------------------------
# A. Using +
# ------------------------------------------------------------

list1 = [
    "a",
    "b",
    "c"
]

list2 = [
    1,
    2,
    3
]

list3 = list1 + list2

# print(list3)

# Output:
# ['a', 'b', 'c', 1, 2, 3]


# ============================================================
# B. Using append()
# ============================================================

list1 = [
    "a",
    "b",
    "c"
]

list2 = [
    1,
    2,
    3
]

for x in list2:
    list1.append(x)

# print(list1)

# Output:
# ['a', 'b', 'c', 1, 2, 3]


# ============================================================
# C. Using extend()
# ============================================================

list1 = [
    "a",
    "b",
    "c"
]

list2 = [
    1,
    2,
    3
]

list1.extend(list2)

# print(list1)

# Output:
# ['a', 'b', 'c', 1, 2, 3]


# ============================================================
# DIFFERENCE:
# append() vs extend()
# ============================================================

# append()
#
# Adds ONE object.

list1 = [1, 2]
list2 = [3, 4]

list1.append(list2)
# print(list1)

# Output:
# [1, 2, [3, 4]]


# extend()
#
# Adds every element individually.

list1 = [1, 2]
list2 = [3, 4]

list1.extend(list2)

# print(list1)

# Output:
# [1, 2, 3, 4]


# ============================================================
# 9. COMPLETE LIST METHODS
# ============================================================

# append(item)
# ------------------------------------------------------------
# Adds one item at the end.
#
# Example:
# fruits.append("orange")


# clear()
# ------------------------------------------------------------
# Removes every item.
#
# Example:
# fruits.clear()


# copy()
# ------------------------------------------------------------
# Creates a shallow copy.
#
# Example:
# fruits.copy()


# count(value)
# ------------------------------------------------------------
# Counts occurrences of a value.
#
# Example:

fruits = [
    "apple",
    "banana",
    "apple",
    "apple"
]

# print(fruits.count("apple"))

# Output:
# 3


# extend(iterable)
# ------------------------------------------------------------
# Adds all items from another iterable.
#
# Example:
# fruits.extend(other_list)


# index(value)
# ------------------------------------------------------------
# Returns first index of a value.
#
# Example:

fruits = [
    "apple",
    "banana",
    "cherry",
    "banana",
]

# print(fruits.index("banana"))

# Output:
# 1


# insert(index, value)
# ------------------------------------------------------------
# Inserts item at given position.
#
# Example:
# fruits.insert(1, "orange")


# pop(index)
# ------------------------------------------------------------
# Removes item by index.
#
# Example:
# fruits.pop(2)


# remove(value)
# ------------------------------------------------------------
# Removes first matching value.
#
# Example:
# fruits.remove("banana")


# reverse()
# ------------------------------------------------------------
# Reverses order.
#
# Example:
# fruits.reverse()


# sort()
# ------------------------------------------------------------
# Sorts list.
#
# Example:
# fruits.sort()

# ============================================================
# SUMMARY
# ============================================================

# Sorting:
# --------
# sort()
# sort(reverse=True)
# sort(key=...)

# Copying:
# --------
# copy()
# list()
# [:]

# Joining:
# --------
# +
# append() in loop
# extend()

# Useful Methods:
# ---------------
# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()

# -----------------------------------------------------------------------------------------------------------------------------


# ============================================================
# PYTHON TUPLES - COMPLETE NOTES & EXAMPLES
# ============================================================
#
# Topics Covered:
# 1. What is a Tuple?
# 2. Creating Tuples
# 3. Tuple Properties
#    - Ordered
#    - Unchangeable (Immutable)
#    - Allows Duplicates
# 4. Tuple Length
# 5. Single Item Tuple
# 6. Tuple Data Types
# 7. type() Function
# 8. tuple() Constructor
# 9. Python Collections Overview
# 10. Access Tuple Items
# 11. Negative Indexing
# 12. Range of Indexes (Slicing)
# 13. Negative Range Slicing
# 14. Check if Item Exists
# 15. Update Tuples (Workarounds)
# 16. Add Items to Tuples
# 17. Remove Items from Tuples
# 18. Delete Entire Tuple
#
# NOTE:
# Tuples are IMMUTABLE (Unchangeable).
#
#
# ============================================================


# ============================================================
# 1. WHAT IS A TUPLE?
# ============================================================

# A tuple is used to store multiple items
# in a single variable.

# Tuple is one of Python's four built-in
# collection data types.

# Tuples are:
#
# ✔ Ordered
# ✔ Unchangeable (Immutable)
# ✔ Allow Duplicate Values

# Tuples are created using ROUND BRACKETS ()

mytuple = ("apple", "banana", "cherry")

# print(mytuple)

# Output:
# ('apple', 'banana', 'cherry')


# ============================================================
# 2. CREATING TUPLES
# ============================================================

thistuple = (
    "apple",
    "banana",
    "cherry"
)

# print(thistuple)

# Output:
# ('apple', 'banana', 'cherry')


# ============================================================
# 3. TUPLE PROPERTIES
# ============================================================

# ------------------------------------------------------------
# A. ORDERED
# ------------------------------------------------------------

# Tuples maintain the insertion order.

fruits = (
    "apple",
    "banana",
    "cherry"
)

# Index:
#
# 0 -> apple
# 1 -> banana
# 2 -> cherry

# Order never changes automatically.


# ------------------------------------------------------------
# B. UNCHANGEABLE (IMMUTABLE)
# ------------------------------------------------------------

# Once created,
# tuple items cannot be:
#
# ❌ Modified
# ❌ Added
# ❌ Removed

# Example (This would raise an error)

# fruits[1] = "orange"


# ------------------------------------------------------------
# C. ALLOWS DUPLICATES
# ------------------------------------------------------------

thistuple = (
    "apple",
    "banana",
    "cherry",
    "apple",
    "cherry"
)

# print(thistuple)

# Output:
# ('apple', 'banana', 'cherry',
#  'apple', 'cherry')


# ============================================================
# 4. TUPLE LENGTH
# ============================================================

# len() returns the number of items.

thistuple = (
    "apple",
    "banana",
    "cherry"
)

# print(len(thistuple))

# Output:
# 3


# ============================================================
# 5. CREATE A SINGLE ITEM TUPLE
# ============================================================

# IMPORTANT:
#
# A single item tuple MUST have a comma.

thistuple = ("apple",)

# print(type(thistuple))

# Output:
# <class 'tuple'>


# ------------------------------------------------------------
# Without Comma
# ------------------------------------------------------------

thistuple = ("apple")

# print(type(thistuple))

# Output:
# <class 'str'>

# Because Python treats it
# as a normal string.


# ============================================================
# 6. TUPLE DATA TYPES
# ============================================================

# Tuple of Strings

tuple1 = (
    "apple",
    "banana",
    "cherry"
)

# Tuple of Integers

tuple2 = (
    1,
    5,
    7,
    9,
    3
)

# Tuple of Booleans

tuple3 = (
    True,
    False,
    False
)

# Mixed Data Types

tuple4 = (
    "abc",
    34,
    True,
    40,
    "male"
)

# Tuples can store multiple
# data types together.


# ============================================================
# 7. type() FUNCTION
# ============================================================

mytuple = (
    "apple",
    "banana",
    "cherry"
)

# print(type(mytuple))

# Output:
# <class 'tuple'>


# ============================================================
# 8. tuple() CONSTRUCTOR
# ============================================================

# Another way to create tuples.

# Notice the double parentheses.

thistuple = tuple((
    "apple",
    "banana",
    "cherry"
))

# print(thistuple)

# Output:
# ('apple', 'banana', 'cherry')


# ============================================================
# 9. PYTHON COLLECTIONS OVERVIEW
# ============================================================

# List
# -----------------------------
# Ordered        ✔
# Changeable     ✔
# Duplicates     ✔


# Tuple
# -----------------------------
# Ordered        ✔
# Changeable     ✘
# Duplicates     ✔


# Set
# -----------------------------
# Ordered        ✘
# Changeable     Partially*
# Duplicates     ✘

# *Items cannot be changed,
# but items can be added or removed.


# Dictionary
# -----------------------------
# Ordered        ✔ (Python 3.7+)
# Changeable     ✔
# Duplicate Keys ✘


# ============================================================
# 10. ACCESS TUPLE ITEMS
# ============================================================

# Tuple indexing starts at 0.

thistuple = (
    "apple",
    "banana",
    "cherry"
)

# print(thistuple[1])

# Output:
# banana


# ============================================================
# 11. NEGATIVE INDEXING
# ============================================================

# -1 -> Last Item
# -2 -> Second Last
# -3 -> Third Last

thistuple = (
    "apple",
    "banana",
    "cherry"
)

# print(thistuple[-1])

# Output:
# cherry


# ============================================================
# 12. RANGE OF INDEXES (SLICING)
# ============================================================

thistuple = (
    "apple",
    "banana",
    "cherry",
    "orange",
    "kiwi",
    "melon",
    "mango"
)

# print(thistuple[2:5])

# Output:
# ('cherry', 'orange', 'kiwi')

# Start index included.
# End index excluded.


# ------------------------------------------------------------
# Slice From Beginning
# ------------------------------------------------------------

# print(thistuple[:4])

# Output:
# ('apple', 'banana', 'cherry', 'orange')


# ------------------------------------------------------------
# Slice Until End
# ------------------------------------------------------------

# print(thistuple[2:])

# Output:
# ('cherry', 'orange', 'kiwi',
#  'melon', 'mango')


# ============================================================
# 13. RANGE OF NEGATIVE INDEXES
# ============================================================

# Index Mapping
#
# apple   -> -7
# banana  -> -6
# cherry  -> -5
# orange  -> -4
# kiwi    -> -3
# melon   -> -2
# mango   -> -1

# print(thistuple[-4:-1])

# Output:
# ('orange', 'kiwi', 'melon')


# ============================================================
# 14. CHECK IF ITEM EXISTS
# ============================================================

thistuple = (
    "apple",
    "banana",
    "cherry"
)

if "apple" in thistuple:
    pass
    # print("Yes, 'apple' is in the fruits tuple")

# Output:
# Yes, 'apple' is in the fruits tuple


# ============================================================
# 15. UPDATE TUPLES
# ============================================================

# Tuples CANNOT be changed directly.

# Workaround:
#
# Tuple
#   ↓
# Convert to List
#   ↓
# Modify List
#   ↓
# Convert back to Tuple


# ------------------------------------------------------------
# Change Tuple Value
# ------------------------------------------------------------

x = (
    "apple",
    "banana",
    "cherry"
)
# print(type(x))
y = list(x)
# print(type(y))

y[1] = "kiwi"

x = tuple(y)

# print(x)

# Output:
# ('apple', 'kiwi', 'cherry')


# ============================================================
# 16. ADD ITEMS TO A TUPLE
# ============================================================

# Tuples have NO append() method.

# Workaround 1:
# Convert to list.

thistuple = (
    "apple",
    "banana",
    "cherry"
)

y = list(thistuple)

y.append("orange")

thistuple = tuple(y)

# print(thistuple)

# Output:
# ('apple', 'banana', 'cherry', 'orange')


# ------------------------------------------------------------
# Workaround 2:
# Add Tuple to Tuple
# ------------------------------------------------------------

thistuple = (
    "apple",
    "banana",
    "cherry"
)

# Single item tuple
# Remember the comma!

y = ("orange",)

thistuple += y

# print(thistuple)

# Output:
# ('apple', 'banana',
#  'cherry', 'orange')


# ============================================================
# IMPORTANT:
# SINGLE ITEM TUPLE
# ============================================================

# Correct

single = ("orange",)

# Wrong

not_tuple = ("orange")

# print(type(single))
# Output:
# <class 'tuple'>

# print(type(not_tuple))
# Output:
# <class 'str'>


# ============================================================
# 17. REMOVE ITEMS FROM TUPLE
# ============================================================

# Tuples DO NOT support remove().

# Workaround:
#
# Convert to list
# Remove item
# Convert back

thistuple = (
    "apple",
    "banana",
    "cherry"
)

y = list(thistuple)

y.remove("apple")

thistuple = tuple(y)

# print(thistuple)

# Output:
# ('banana', 'cherry')


# ============================================================
# 18. DELETE ENTIRE TUPLE
# ============================================================

thistuple = (
    "apple",
    "banana",
    "cherry"
)

del thistuple

# print(thistuple)

# Output:
#
# NameError:
# name 'thistuple' is not defined

# Because the tuple
# no longer exists.


# ============================================================
# TUPLE VS LIST
# ============================================================

# LIST
# -----------------------------
# []
# Mutable
# append()
# remove()
# insert()
# pop()
# Faster for modifications


# TUPLE
# -----------------------------
# ()
# Immutable
# No append()
# No remove()
# No insert()
# No pop()
# Faster for reading
# More memory efficient


# ============================================================
# QUICK REVISION
# ============================================================

# Creating
# -----------------------------
# ()
# tuple()


# Accessing
# -----------------------------
# tuple[index]
# tuple[-1]
# tuple[start:end]


# Checking
# -----------------------------
# item in tuple


# Length
# -----------------------------
# len(tuple)


# Data Type
# -----------------------------
# type(tuple)


# Updating
# -----------------------------
# Convert to list
# Modify
# Convert back


# Adding
# -----------------------------
# list() + append()
# OR
# tuple += ("item",)


# Removing
# -----------------------------
# list() + remove()
# Convert back


# Delete Entire Tuple
# -----------------------------
# del tuple_name


# ---------------------------------------------------------------------------------------------------------------------------

# ============================================================
# PYTHON TUPLES - UNPACKING, LOOPING, JOINING & METHODS
# ============================================================
#
# Topics Covered:
# 1. Packing a Tuple
# 2. Unpacking a Tuple
# 3. Using the Asterisk (*) in Unpacking
# 4. Loop Through a Tuple
#    - for loop
#    - for loop with index
#    - while loop
# 5. Join Tuples
# 6. Multiply Tuples
# 7. Tuple Methods
#    - count()
#    - index()
#
#
# ============================================================


# ============================================================
# 1. PACKING A TUPLE
# ============================================================

# When we create a tuple and assign values to it,
# it is called "Packing".

fruits = (
    "apple",
    "banana",
    "cherry"
)

# The tuple now stores three values.


# ============================================================
# 2. UNPACKING A TUPLE
# ============================================================

# Unpacking means extracting tuple values
# into separate variables.

fruits = (
    "apple",
    "banana",
    "cherry",
    
)

(green, yellow, red) = fruits

# Output:
# apple

# print(green)
# print(yellow)
# print(red)
# print(new)
# Output:
# banana

# Output:
# cherry


# ------------------------------------------------------------
# IMPORTANT RULE
# ------------------------------------------------------------

# Number of variables must match
# the number of tuple items.

# Correct

# (a, b, c) = ("x", "y", "z")

# Incorrect

# (a, b) = ("x", "y", "z")

# This raises:
# ValueError:
# too many values to unpack

# Unless you use the * operator.


# ============================================================
# 3. USING ASTERISK (*) IN UNPACKING
# ============================================================

# If there are more tuple values
# than variables,
# use * to collect remaining values.

fruits = (
    "apple",
    "banana",
    "cherry",
    "strawberry",
    "raspberry"
)

(green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)
# Output:
# apple

# Output:
# banana

# Output:
# ['cherry', 'strawberry', 'raspberry']

# Notice:
#
# The starred variable becomes a LIST,
# not a tuple.


# ------------------------------------------------------------
# Asterisk in the Middle
# ------------------------------------------------------------

# The * does NOT have to be the last variable.

# Python automatically assigns enough values
# so that the remaining variables still get values.

fruits = (
    "apple",
    "mango",
    "papaya",
    "pineapple",
    "cherry"
)

(green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)
# Output:
# apple

# Output:
# ['mango', 'papaya', 'pineapple']

# Output:
# cherry


# ============================================================
# SUMMARY OF UNPACKING
# ============================================================

# Normal Unpacking

# (a, b, c) = (1, 2, 3)

# a -> 1
# b -> 2
# c -> 3


# Starred Unpacking

# (a, *b) = (1, 2, 3, 4)

# a -> 1
# b -> [2, 3, 4]


# Middle Star

# (a, *b, c) = (1,2,3,4,5)

# a -> 1
# b -> [2,3,4]
# c -> 5


# ============================================================
# 4. LOOP THROUGH A TUPLE
# ============================================================

# Tuples can be looped through
# exactly like lists.


# ------------------------------------------------------------
# A. Using a for Loop
# ------------------------------------------------------------

thistuple = (
    "apple",
    "banana",
    "cherry"
)

for x in thistuple:
    pass
    # print(x)

# Output:
#
# apple
# banana
# cherry


# ============================================================
# B. LOOP USING INDEX NUMBERS
# ============================================================

# Use:
#
# range(len(tuple))

thistuple = (
    "apple",
    "banana",
    "cherry"
)

for i in range(len(thistuple)):
    pass
    # print(thistuple[i])

# Output:
#
# apple
# banana
# cherry


# Explanation:
#
# len(thistuple) -> 3
#
# range(3) creates:
#
# 0
# 1
# 2


# ============================================================
# C. LOOP USING A WHILE LOOP
# ============================================================

thistuple = (
    "apple",
    "banana",
    "cherry"
)

i = 0

while i < len(thistuple):

    # print(thistuple[i])

    i = i + 1

# Output:
#
# apple
# banana
# cherry


# Explanation:
#
# Initialize:
# i = 0
#
# Condition:
# i < len(tuple)
#
# Increment:
# i = i + 1


# ============================================================
# LOOPING METHODS SUMMARY
# ============================================================

# Method 1

# for item in tuple:


# Method 2

# for i in range(len(tuple)):


# Method 3

# while i < len(tuple):


# ============================================================
# 5. JOIN TUPLES
# ============================================================

# Tuples can be joined using
# the + operator.

tuple1 = (
    "a",
    "b",
    "c"
)

tuple2 = (
    1,
    2,
    3
)

tuple3 = tuple1 + tuple2

# print(tuple3)

# Output:
#
# ('a', 'b', 'c', 1, 2, 3)


# ============================================================
# 6. MULTIPLY TUPLES
# ============================================================

# The * operator repeats
# tuple contents.

fruits = (
    "apple",
    "banana",
    "cherry"
)

mytuple = fruits * 2

# print(mytuple)

# Output:
#
# ('apple',
#  'banana',
#  'cherry',
#  'apple',
#  'banana',
#  'cherry')


# ------------------------------------------------------------
# Another Example
# ------------------------------------------------------------

numbers = (
    1,
    2
)

double = numbers * 3

# print(double)

# Output:
#
# (1, 2, 1, 2, 1, 2)


# ============================================================
# 7. TUPLE METHODS
# ============================================================

# Tuples have only TWO built-in methods:
#
# 1. count()
# 2. index()


# ============================================================
# A. count()
# ============================================================

# count(value)
#
# Counts how many times
# a value appears.

fruits = (
    "apple",
    "banana",
    "apple",
    "cherry",
    "apple"
)

# print(fruits.count("apple"))

# Output:
# 3


# ------------------------------------------------------------
# Another Example
# ------------------------------------------------------------

numbers = (
    1,
    2,
    2,
    2,
    5
)

# print(numbers.count(2))

# Output:
# 3


# ============================================================
# B. index()
# ============================================================

# index(value)
#
# Returns the FIRST occurrence
# of the specified value.

fruits = (
    "apple",
    "banana",
    "cherry"
    "banana",
)

# print(fruits.index("banana"))

# Output:
# 1


# ------------------------------------------------------------
# Duplicate Example
# ------------------------------------------------------------

fruits = (
    "apple",
    "banana",
    "apple",
    "cherry"
)

# print(fruits.index("apple"))

# Output:
# 0

# Only the FIRST occurrence
# is returned.


# ============================================================
# TUPLE METHODS REFERENCE
# ============================================================

# count(value)
# ------------------------------------------------------------
# Returns how many times
# the value appears.
#
# Example:
#
# fruits.count("apple")


# index(value)
# ------------------------------------------------------------
# Returns the first index
# where the value occurs.
#
# Example:
#
# fruits.index("banana")


# ============================================================
# QUICK REVISION
# ============================================================

# Packing
# -----------------------------
# fruits = ("apple", "banana")


# Unpacking
# -----------------------------
# (a, b) = fruits


# Starred Unpacking
# -----------------------------
# (a, *b) = tuple


# Looping
# -----------------------------
# for item in tuple
#
# for i in range(len(tuple))
#
# while loop


# Joining
# -----------------------------
# tuple1 + tuple2


# Multiplication
# -----------------------------
# tuple * 2


# Built-in Methods
# -----------------------------
# count()
# index()


# ============================================================
# DIFFERENCE BETWEEN LISTS & TUPLES
# ============================================================

# LIST
# -----------------------------
# []
# Mutable
# Many built-in methods
# append()
# insert()
# remove()
# pop()
# sort()


# TUPLE
# -----------------------------
# ()
# Immutable
# Only two methods
# count()
# index()

