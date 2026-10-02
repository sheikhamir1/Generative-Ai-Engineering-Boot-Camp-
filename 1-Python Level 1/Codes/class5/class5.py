# ============================================================
# PYTHON OPERATORS - COMPLETE NOTES & EXAMPLES
# ============================================================
# This file contains:
# 1. Ternary Operator
# 2. Comparison Operators
# 3. Logical Operators
# 4. Identity Operators
# 5. Membership Operators
# 6. Operator Precedence
#
# ============================================================


# ============================================================
# 1. PYTHON TERNARY OPERATOR
# ============================================================

# The ternary operator allows you to assign one value if a
# condition is True and another value if it is False.

# Syntax:
# variable = value_if_true if condition else value_if_false

num = 4

x = "WEEKEND!" if num > 5 else "Workday"

# print(x)
# Output: WEEKEND!


# ------------------------------------------------------------
# Ternary Operator as an alternative to elif
# ------------------------------------------------------------

# Assign:
# - "Fri" if num is 5
# - "Sat" if num is 6
# - "Sun" if num is 7
# - otherwise "weekday"

num = 8

x = (
    "Fri" if num == 5
    else "Sat" if num == 6
    else "Sun" if num == 7
    else "weekday"
)

# print(x)
# Output: Sat



# ============================================================
# 2. PYTHON COMPARISON OPERATORS
# ============================================================

# Comparison operators compare two values and return either
# True or False.

# ==   Equal
# !=   Not Equal
# >    Greater Than
# <    Less Than
# >=   Greater Than or Equal To
# <=   Less Than or Equal To

x = 5
y = 3

# print(x == y)
# Output: False

# print(x != y)
# Output: True

# print(x > y)
# Output: True

# print(x < y)
# Output: False

# print(x >= y)
# Output: True

# print(x <= y)
# Output: False


# ------------------------------------------------------------
# Chaining Comparison Operators
# ------------------------------------------------------------

# Python allows multiple comparisons in a single expression.

x = 5

# print(1 < x < 10)
# Output: True

# Equivalent to:
# print(1 < x and x < 10)
# Output: True


# ============================================================
# 3. PYTHON LOGICAL OPERATORS
# ============================================================

# Logical operators are used to combine conditions.

# and
# Returns True if BOTH conditions are True.

# or
# Returns True if AT LEAST ONE condition is True.

# not
# Reverses the result.


# ------------------------------------------------------------
# AND Operator
# ------------------------------------------------------------

x = 5

# Check if x is greater than 0 AND less than 10

# print(x > 0 and x < 10)
# Output: True


# ------------------------------------------------------------
# OR Operator
# ------------------------------------------------------------

x = 5

# Check if x is less than 5 OR greater than 10

# print(x < 6 or x > 10)
# Output: False


# ------------------------------------------------------------
# NOT Operator
# ------------------------------------------------------------

x = 5

# Reverse the result

# print(not (x > 6 and x < 10))

# Output: False


# ============================================================
# 4. PYTHON IDENTITY OPERATORS
# ============================================================

# Identity operators compare memory locations (objects),
# not just values.

# is
# Returns True if both variables refer to the SAME object.

# is not
# Returns True if both variables refer to DIFFERENT objects.


# ------------------------------------------------------------
# Example: is Operator
# ------------------------------------------------------------

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# print(x is z)
# Output: True
# Both variables point to the same object.

# print(x is y)
# print(x is not y)
# Output: False
# Different objects in memory.

# print(x == y)
# Output: True
# Values are equal.


# ------------------------------------------------------------
# Example: is not Operator
# ------------------------------------------------------------

x = ["apple", "banana"]
y = ["apple", "banana"]

# print(x is not y)
# Output: True


# ------------------------------------------------------------
# Difference Between is and ==
# ------------------------------------------------------------

# is
# Checks whether two variables refer to the same object
# in memory.

# ==
# Checks whether the values are equal.

x = [1, 2, 3]
y = [1, 2, 3]

# print(x == y)
# Output: True

# print(x is y)
# Output: False


# ============================================================
# 5. PYTHON MEMBERSHIP OPERATORS
# ============================================================

# Membership operators check whether a value exists inside
# a sequence such as a list, tuple, string, etc.

# in
# Returns True if value exists.

# not in
# Returns True if value does NOT exist.


# ------------------------------------------------------------
# Example: in Operator
# ------------------------------------------------------------

fruits = ["apple", "Banana", "cherry"]

# print("Banana" in fruits)
# Output: True


# ------------------------------------------------------------
# Example: not in Operator
# ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

# print("pineapple" not in fruits)
# Output: True


# ------------------------------------------------------------
# Membership Operators with Strings
# ------------------------------------------------------------

text = "Hello World"

# print("H" in text)
# Output: True

# print("hello" in text)
# Output: False
# Python string comparisons are case-sensitive.

# print("z" not in text)
# Output: True


# ============================================================
# 6. PYTHON OPERATOR PRECEDENCE
# ============================================================

# Operator precedence determines which operation
# Python performs first.


# ------------------------------------------------------------
# Parentheses Have Highest Precedence
# ------------------------------------------------------------

# print((6 + 3) - (6 + 3))
# Output: 0


# ------------------------------------------------------------
# Multiplication Before Addition
# ------------------------------------------------------------

# print((100 + 5) * 3)
# Output: 115

# Explanation:
# 5 * 3 = 15
# 100 + 15 = 115


# ============================================================
# PRECEDENCE ORDER (Highest to Lowest)
# ============================================================

# 1.  ()                      Parentheses
# 2.  **                      Exponentiation
# 3.  +x, -x, ~x             Unary Plus, Minus, Bitwise NOT
# 4.  *, /, //, %            Multiplication, Division,
#                            Floor Division, Modulus
# 5.  +, -                   Addition, Subtraction
# 6.  <<, >>                 Bitwise Shifts
# 7.  &                      Bitwise AND
# 8.  ^                      Bitwise XOR
# 9.  |                      Bitwise OR
# 10. ==, !=, >, >=, <, <=
#     is, is not,
#     in, not in             Comparisons, Identity,
#                            Membership
# 11. not                    Logical NOT
# 12. and                    Logical AND
# 13. or                     Logical OR


# ============================================================
# LEFT-TO-RIGHT EVALUATION
# ============================================================

# If operators have the same precedence,
# Python evaluates from LEFT to RIGHT.

# print(5 + 4 - 7 + 3)
# Output: 5

# Step-by-step:
# 5 + 4 = 9
# 9 - 7 = 2
# 2 + 3 = 5


# -------------------------------------------------------------------------------------------------

# ============================================================
# PYTHON LISTS - COMPLETE NOTES & EXAMPLES
# ============================================================
#
# Topics Covered:
# 1. What is a List?
# 2. Creating Lists
# 3. List Properties
#    - Ordered
#    - Changeable
#    - Allows Duplicates
# 4. List Length
# 5. List Data Types
# 6. type() Function
# 7. list() Constructor
# 8. Python Collections Overview
# 9. Accessing List Items
# 10. Negative Indexing
# 11. Range of Indexes
# 12. Range of Negative Indexes
# 13. Check if Item Exists

#
# ============================================================


# ============================================================
# 1. WHAT IS A LIST?
# ============================================================

# Lists are used to store multiple items in a single variable.

# A list is one of Python's built-in collection data types.

# Lists are:
# ✔ Ordered
# ✔ Changeable (Mutable)
# ✔ Allow Duplicate Values

# Lists are created using square brackets []

mylist = ["apple", "banana", "cherry"]

# print(mylist)
# Output:
# ['apple', 'banana', 'cherry']


# ============================================================
# 2. CREATING LISTS
# ============================================================

# Creating a simple list

thislist = ["apple", "banana", "cherry"]

# print(thislist)
# Output:
# ['apple', 'banana', 'cherry']


# ============================================================
# 3. LIST PROPERTIES
# ============================================================

# ------------------------------------------------------------
# A. ORDERED
# ------------------------------------------------------------

# Lists maintain the order in which items are added.

fruits = ["apple", "banana", "cherry"]

# Item positions:
# Index 0 -> apple
# Index 1 -> banana
# Index 2 -> cherry

# New items are normally added at the end.


# ------------------------------------------------------------
# B. CHANGEABLE (MUTABLE)
# ------------------------------------------------------------

# After a list is created, items can be:
# - Modified
# - Added
# - Removed

fruits = ["apple", "banana", "cherry"]

# Example:
fruits[1] = "orange"
# print(fruits)
# Result:
# ['apple', 'orange', 'cherry']


# ------------------------------------------------------------
# C. ALLOWS DUPLICATES
# ------------------------------------------------------------

# Lists can contain multiple items with the same value.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]

# print(thislist)
# Output:
# ['apple', 'banana', 'cherry', 'apple', 'cherry']


# ============================================================
# 4. LIST LENGTH
# ============================================================

# Use len() to find the number of items in a list.

thislist = ["apple", "banana", "cherry","new"]

# print(len(thislist))
# Output:
# 3


# ============================================================
# 5. LIST ITEMS - DATA TYPES
# ============================================================

# List items can be of any data type.


# ------------------------------------------------------------
# List of Strings
# ------------------------------------------------------------

list1 = ["apple", "banana", "cherry"]


# ------------------------------------------------------------
# List of Integers
# ------------------------------------------------------------

list2 = [1, 5, 7, 9, 3]


# ------------------------------------------------------------
# List of Booleans
# ------------------------------------------------------------

list3 = [True, False, False]


# ------------------------------------------------------------
# Mixed Data Types
# ------------------------------------------------------------

list4 = ["abc", 34, True, 40, "male"]
# print(list4)

# Lists can store different data types together.


# ============================================================
# 6. type() FUNCTION
# ============================================================

# From Python's perspective, lists are objects
# with the data type 'list'.

mylist = ["apple", "banana", "cherry"]

# print(type(mylist))
# Output:
# <class 'list'>


# ============================================================
# 7. THE list() CONSTRUCTOR
# ============================================================

# Another way to create a list is by using
# the list() constructor.

# Note the double parentheses.

thislist = list(("apple", "banana", "cherry"))

# print(thislist)
# Output:
# ['apple', 'banana', 'cherry']


# ============================================================
# 8. PYTHON COLLECTIONS OVERVIEW
# ============================================================

# Python has four major collection types:

# ------------------------------------------------------------
# LIST
# ------------------------------------------------------------
# Ordered        -> Yes
# Changeable     -> Yes
# Duplicates     -> Yes

# Example:
sample_list = ["apple", "banana", "apple"]


# ------------------------------------------------------------
# TUPLE
# ------------------------------------------------------------
# Ordered        -> Yes
# Changeable     -> No
# Duplicates     -> Yes

# Example:
sample_tuple = ("apple", "banana", "apple")


# ------------------------------------------------------------
# SET
# ------------------------------------------------------------
# Ordered        -> No
# Changeable     -> Partially*
# Duplicates     -> No

# *Items cannot be changed directly,
# but items can be added or removed.

# Example:
sample_set = {"apple", "banana", "cherry"}


# ------------------------------------------------------------
# DICTIONARY
# ------------------------------------------------------------
# Ordered        -> Yes (Python 3.7+)
# Changeable     -> Yes
# Duplicates     -> No duplicate keys

# Example:
sample_dict = {
    "name": "Rohan",
    "age": 22
}


# ============================================================
# 9. ACCESSING LIST ITEMS
# ============================================================

# List items are indexed.

# Indexing starts from 0.

thislist = ["apple", "banana", "cherry"]

# Index Positions:
# 0 -> apple
# 1 -> banana
# 2 -> cherry

# print(thislist[1])
# Output:
# banana


# ============================================================
# 10. NEGATIVE INDEXING
# ============================================================

# Negative indexing starts from the end.

# -1 -> Last item
# -2 -> Second last item
# -3 -> Third last item

thislist = ["apple", "banana", "cherry"]

# print(thislist[-1])
# Output:
# cherry


# ============================================================
# 11. RANGE OF INDEXES (SLICING)
# ============================================================

# Syntax:
# list[start:end]

# Start index is INCLUDED.
# End index is EXCLUDED.

thislist = [
    "apple",
    "banana",
    "cherry",
    "orange",
    "kiwi",
    "melon",
    "mango"
]

# print(thislist[2:6])
# Output:
# ['cherry', 'orange', 'kiwi']

# Explanation:
# Start at index 2 (included)
# Stop before index 5


# ------------------------------------------------------------
# Omitting the Start Index
# ------------------------------------------------------------

# Python starts from index 0

# print(thislist[:4])
# Output:
# ['apple', 'banana', 'cherry', 'orange']


# ------------------------------------------------------------
# Omitting the End Index
# ------------------------------------------------------------

# Python continues until the last item

# print(thislist[2:])
# Output:
# ['cherry', 'orange', 'kiwi', 'melon', 'mango']


# ============================================================
# 12. RANGE OF NEGATIVE INDEXES
# ============================================================

# Negative indexes count from the end.

thislist = [
    "apple",
    "banana",
    "cherry",
    "orange",
    "kiwi",
    "melon",
    "mango"
]

# Index Mapping:
#
# apple   -> -7
# banana  -> -6
# cherry  -> -5
# orange  -> -4
# kiwi    -> -3
# melon   -> -2
# mango   -> -1

# print(thislist[-4:-1])
# Output:
# ['orange', 'kiwi', 'melon']

# Start at -4 (included)
# Stop before -1


# ============================================================
# 13. CHECK IF ITEM EXISTS
# ============================================================

# Use the 'in' keyword to check whether
# an item exists in a list.

thislist = ["apple", "banana", "cherry"]

if "apple" in thislist:
    pass
    # print("Yes, 'apple' is in the fruits list")

# Output:
# Yes, 'apple' is in the fruits list


# ============================================================
# QUICK REVISION
# ============================================================

# List Characteristics:
#
# ✔ Ordered
# ✔ Changeable (Mutable)
# ✔ Allows Duplicates
# ✔ Indexed
# ✔ Can Store Multiple Data Types
#
# Common Functions:
#
# len(list)       -> Length of list
# type(list)      -> Data type
# list()          -> Constructor
#
# Common Operations:
#
# list[index]
# list[-index]
# list[start:end]
# item in list
#
# Example:
#
# fruits = ["apple", "banana", "cherry"]
#
# fruits[0]       -> apple
# fruits[-1]      -> cherry
# fruits[1:3]     -> ['banana', 'cherry']
# len(fruits)     -> 3
#

# -----------------------------------------------------------------------------------------------------

# ============================================================
# PYTHON LISTS - CHANGE, ADD & REMOVE ITEMS
# ============================================================
#
# Topics Covered:
# 1. Change Item Value
# 2. Change a Range of Items
# 3. Replace One Item with Multiple Items
# 4. Replace Multiple Items with One Item
# 5. insert() Method
# 6. append() Method
# 7. extend() Method
# 8. Adding Other Iterables
# 9. remove() Method
# 10. pop() Method
# 11. del Keyword
# 12. clear() Method
# ============================================================


# ============================================================
# 1. CHANGE ITEM VALUE
# ============================================================

# To change a specific item, use its index number.

thislist = ["apple", "banana", "cherry"]

# Change the second item (index 1)

thislist[1] = "blackcurrant"

# print(thislist)
# Output:
# ['apple', 'blackcurrant', 'cherry']


# ============================================================
# 2. CHANGE A RANGE OF ITEM VALUES
# ============================================================

# Syntax:
# list[start:end] = [new_values]

# Start index is included.
# End index is excluded.

thislist = [
    "apple",
    "banana",
    "cherry",
    "orange",
    "kiwi",
    "mango"
]

# Replace banana and cherry

thislist[1:3] = [
    "blackcurrant",
    "watermelon"
]

# print(thislist)
# Output:
# ['apple', 'blackcurrant', 'watermelon',
#  'orange', 'kiwi', 'mango']


# ============================================================
# 3. REPLACE ONE ITEM WITH MULTIPLE ITEMS
# ============================================================

# You can insert more items than you replace.

thislist = ["apple", "banana", "cherry"]

# Replace one item with two items

thislist[1:2] = [
    "blackcurrant",
    "watermelon"
]

# print(thislist)
# Output:
# ['apple', 'blackcurrant',
#  'watermelon', 'cherry']

# Notice:
# List length increases because
# 1 item was replaced by 2 items.


# ============================================================
# 4. REPLACE MULTIPLE ITEMS WITH ONE ITEM
# ============================================================

# You can also replace multiple items
# with fewer items.

thislist = ["apple", "banana", "cherry"]

# Replace banana and cherry
# with watermelon

thislist[1:3] = ["watermelon"]

# print(thislist)
# Output:
# ['apple', 'watermelon']

# Notice:
# List length decreases because
# 2 items were replaced by 1 item.


# ============================================================
# 5. INSERT ITEMS USING insert()
# ============================================================

# Syntax:
# list.insert(index, value)

# insert() adds an item at a specific position
# WITHOUT replacing existing items.

thislist = ["apple", "banana", "cherry"]

# Insert watermelon at index 2

thislist.insert(2, "watermelon")

# print(thislist)
# Output:
# ['apple', 'banana', 'watermelon', 'cherry']

# Existing items shift to the right.


# ============================================================
# 6. ADD ITEMS USING append()
# ============================================================

# append() adds an item to the END of the list.

# Syntax:
# list.append(value)

thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

# print(thislist)
# Output:
# ['apple', 'banana', 'cherry', 'orange']


# ============================================================
# 7. ADD ITEMS USING insert()
# ============================================================

# insert() can also be used to add items.

# Difference:
# append() -> adds at end
# insert() -> adds at specified position

thislist = ["apple", "banana", "cherry"]

# Insert orange at index 1

thislist.insert(1, "orange")

# print(thislist)
# Output:
# ['apple', 'orange', 'banana', 'cherry']


# ============================================================
# 8. EXTEND LIST USING extend()
# ============================================================

# extend() adds all elements from another iterable.

# Syntax:
# list.extend(iterable)

thislist = [
    "apple",
    "banana",
    "cherry"
]

tropical = [
    "mango",
    "pineapple",
    "papaya"
]

thislist.extend(tropical)

# print(thislist)
# Output:
# ['apple', 'banana', 'cherry',
#  'mango', 'pineapple', 'papaya']

# New items are added at the end.


# ============================================================
# 9. ADD ANY ITERABLE USING extend()
# ============================================================

# extend() works with:
# ✔ Lists
# ✔ Tuples
# ✔ Sets
# ✔ Dictionaries
# ✔ Strings
# ✔ Any iterable object

thislist = [
    "apple",
    "banana",
    "cherry"
]

thistuple = (
    "kiwi",
    "orange"
)

thislist.extend(thistuple)

# print(thislist)
# Output:
# ['apple', 'banana', 'cherry',
#  'kiwi', 'orange']


# ============================================================
# 10. REMOVE ITEMS USING remove()
# ============================================================

# Syntax:
# list.remove(value)

# Removes the FIRST matching value.

thislist = [
    "apple",
    "banana",
    "cherry"
]

thislist.remove("banana")

# print(thislist)
# Output:
# ['apple', 'cherry']


# ------------------------------------------------------------
# remove() Removes Only the First Occurrence
# ------------------------------------------------------------

thislist = [
    "apple",
    "banana",
    "cherry",
    "banana",
    "kiwi"
]

thislist.remove("banana")

# print(thislist)
# Output:
# ['apple', 'cherry', 'banana', 'kiwi']

# Only the first "banana" is removed.


# ============================================================
# 11. REMOVE ITEMS USING pop()
# ============================================================

# Syntax:
# list.pop(index)

# Removes item at a specified index.

thislist = [
    "apple",
    "banana",
    "cherry"
]

thislist.pop(1)

# print(thislist)
# Output:
# ['apple', 'cherry']


# ------------------------------------------------------------
# pop() Without an Index
# ------------------------------------------------------------

# Removes the LAST item.

thislist = [
    "apple",
    "banana",
    "cherry"
]

thislist.pop()

# print(thislist)
# Output:
# ['apple', 'banana']


# ============================================================
# 12. REMOVE ITEMS USING del
# ============================================================

# del removes an item using its index.

thislist = [
    "apple",
    "banana",
    "cherry"
]

del thislist[0]

# print(thislist)
# Output:
# ['banana', 'cherry']


# ------------------------------------------------------------
# Delete Entire List
# ------------------------------------------------------------

thislist = [
    "apple",
    "banana",
    "cherry"
]

# Delete the whole list

del thislist

# print(thislist)
# This would raise:
# NameError
#
# Because the variable no longer exists.


# ============================================================
# 13. CLEAR A LIST USING clear()
# ============================================================

# clear() removes all items
# but keeps the list itself.

thislist = [
    "apple",
    "banana",
    "cherry"
]

thislist.clear()

# print(thislist)
# Output:
# []

# List still exists.
# It is just empty.


# ============================================================
# QUICK COMPARISON OF LIST METHODS
# ============================================================

# append(item)
# ------------------------------------------------------------
# Adds ONE item to the end.
#
# Example:
# fruits.append("orange")


# insert(index, item)
# ------------------------------------------------------------
# Inserts an item at a specific position.
#
# Example:
# fruits.insert(1, "orange")


# extend(iterable)
# ------------------------------------------------------------
# Adds multiple items from another iterable.
#
# Example:
# fruits.extend(other_list)


# remove(value)
# ------------------------------------------------------------
# Removes first matching value.
#
# Example:
# fruits.remove("banana")


# pop(index)
# ------------------------------------------------------------
# Removes item by index.
#
# Example:
# fruits.pop(1)


# del
# ------------------------------------------------------------
# Deletes item or entire list.
#
# Example:
# del fruits[0]
# del fruits


# clear()
# ------------------------------------------------------------
# Removes all items but keeps list.
#
# Example:
# fruits.clear()


# ============================================================
# QUICK REVISION TABLE
# ============================================================

# Change Item:
# list[index] = value

# Change Range:
# list[start:end] = values

# Add at End:
# append()

# Add at Position:
# insert()

# Add Multiple Items:
# extend()

# Remove by Value:
# remove()

# Remove by Index:
# pop()

# Delete Item/List:
# del

# Empty List:
# clear()


# ---------------------------------------------------------------------------------------------------------

# ============================================================
# PYTHON LISTS - LOOPING & LIST COMPREHENSION
# ============================================================
#
# Topics Covered:
# 1. Loop Through a List (for loop)
# 2. Loop Through Index Numbers
# 3. Loop Using while Loop
# 4. Loop Using List Comprehension
# 5. What is List Comprehension?
# 6. List Comprehension Syntax
# 7. Using Conditions
# 8. Using Different Iterables
# 9. Using range()
# 10. Manipulating Output
# 11. Conditional Expressions Inside Comprehension
#
# ============================================================


# ============================================================
# 1. LOOP THROUGH A LIST USING A FOR LOOP
# ============================================================

# A for loop is the most common way
# to iterate through a list.

thislist = [
    "apple",
    "banana",
    "cherry"
]

for x in thislist:
    pass
#     print(x)
#     print("In")
# print("Out")

# Output:
#
# apple
# banana
# cherry


# Explanation:
# x takes one item at a time from the list.


# ============================================================
# 2. LOOP THROUGH INDEX NUMBERS
# ============================================================

# Instead of directly accessing items,
# we can loop through index numbers.

# len(list)
# returns the number of items.

# range(len(list))
# generates index numbers.

thislist = [
    "apple",
    "banana",
    "cherry"
]


for i in range(len(thislist)):
    pass
    # print("Value of I: ",i)
    # print(thislist[i])

# Output:
#
# apple
# banana
# cherry


# Explanation:
#
# len(thislist) -> 3
#
# range(3) creates:
# [0, 1, 2]
#
# Iterations:
#
# thislist[0] -> apple
# thislist[1] -> banana
# thislist[2] -> cherry


# ============================================================
# 3. LOOP THROUGH A LIST USING A WHILE LOOP
# ============================================================

# A while loop requires:
#
# 1. Initialization
# 2. Condition
# 3. Increment/Update

thislist = [
    "apple",
    "banana",
    "cherry"
]

i = 0

while i < len(thislist):
    pass
    # print(thislist[i])

    i = i + 1

# Output:
#
# apple
# banana
# cherry


# Explanation:
#
# Start:
# i = 0
#
# Loop continues while:
# i < len(thislist)
#
# i increases by 1 each iteration.


# ============================================================
# 4. LOOP USING LIST COMPREHENSION
# ============================================================

# List comprehension can also be used
# as a short form of looping.

thislist = [
    "apple",
    "banana",
    "cherry"
]

# print([x for x in thislist])

# Equivalent to:
#
# for x in thislist:
#     print(x)

# Output:
#
# apple
# banana
# cherry

# NOTE:
# Using list comprehension only for printing
# is generally not recommended.
#
# It is mainly used to CREATE NEW LISTS.


# ============================================================
# 5. WHAT IS LIST COMPREHENSION?
# ============================================================

# List comprehension provides a shorter
# way to create new lists from existing data.

# Instead of writing multiple lines,
# you can create a new list in one line.


# ------------------------------------------------------------
# Traditional Method
# ------------------------------------------------------------

fruits = [
    "apple",
    "banana",
    "cherry",
    "kiwi",
    "mango"
]

newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

# print(newlist)

# Output:
# ['apple', 'banana', 'mango']


# ------------------------------------------------------------
# List Comprehension Version
# ------------------------------------------------------------

fruits = [
    "apple",
    "banana",
    "cherry",
    "kiwi",
    "mango"
]

newlist = [
    x
    for x in fruits
    if "a" in x
]
# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# Output:
# ['apple', 'banana', 'mango']


# ============================================================
# 6. LIST COMPREHENSION SYNTAX
# ============================================================

# General Syntax:
#
# newlist = [
#     expression
#     for item in iterable
#     if condition
# ]
#
#
# expression
#     What gets added to the new list
#
# item
#     Current element
#
# iterable
#     Source collection
#
# condition
#     Optional filter


# ============================================================
# 7. CONDITIONS IN LIST COMPREHENSION
# ============================================================

# Conditions act like filters.

# Only items that satisfy the condition
# are included in the new list.

fruits = [
    "apple",
    "banana",
    "cherry",
    "kiwi",
    "mango"
]

newlist = [
    x
    for x in fruits
    if x != "cherry"
]

# print(newlist)

# Output:
# ['banana', 'cherry', 'kiwi', 'mango']


# Explanation:
#
# "apple" is excluded.


# ------------------------------------------------------------
# No Condition
# ------------------------------------------------------------

newlist = [
    x
    for x in fruits
]

# print(newlist)

# Output:
# ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# Copies every item.


# ============================================================
# 8. ITERABLES IN LIST COMPREHENSION
# ============================================================

# The iterable can be:
#
# ✔ List
# ✔ Tuple
# ✔ Set
# ✔ String
# ✔ Range
# ✔ Any iterable object


# Example with a Tuple

numbers = (
    1,
    2,
    3,
    4,
    5
)

# print(numbers)
newlist = [
    x
    for x in numbers
]

# print(newlist)

# Output:
# [1, 2, 3, 4, 5]


# ============================================================
# 9. USING range() IN LIST COMPREHENSION
# ============================================================

# range() generates a sequence of numbers.

newlist = [
    x
    for x in range(100)
]

# print(newlist)
# print(len(newlist))

# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# ------------------------------------------------------------
# range() With Condition
# ------------------------------------------------------------

newlist = [
    x
    for x in range(10)
    if x < 5
]

# print(newlist)

# Output:
# [0, 1, 2, 3, 4]


# Explanation:
#
# Only numbers less than 5
# are accepted.


# ============================================================
# 10. EXPRESSION IN LIST COMPREHENSION
# ============================================================

# The expression determines
# what gets added to the new list.


# ------------------------------------------------------------
# Convert Items to Uppercase
# ------------------------------------------------------------

fruits = [
    "apple",
    "banana",
    "cherry"
]

newlist = [
    x.upper()
    for x in fruits
]

# print(newlist)

# Output:
# ['APPLE', 'BANANA', 'CHERRY']


# ------------------------------------------------------------
# Replace Every Value
# ------------------------------------------------------------

newlist = [
    "hello"
    for x in fruits
]

# print(newlist)

# Output:
# ['hello', 'hello', 'hello']


# Explanation:
#
# Regardless of x,
# every item becomes "hello".


# ============================================================
# 11. CONDITIONAL EXPRESSIONS
# ============================================================

# The expression itself can contain
# an if-else condition.

fruits = [
    "apple",
    "banana",
    "cherry"
]

newlist = [
    x 
    if x != "cherry"
    else "orange"
    for x in fruits
]

# print(newlist)

# Output:
# ['apple', 'orange', 'cherry']


# Explanation:
#
# If item is NOT banana:
#     keep original item
#
# Else:
#     replace banana with orange


# ------------------------------------------------------------
# Equivalent Traditional Code
# ------------------------------------------------------------

newlist = []

for x in fruits:

    if x != "banana":
        newlist.append(x)

    else:
        newlist.append("orange")

# print(newlist)

# Output:
# ['apple', 'orange', 'cherry']


# ============================================================
# LIST COMPREHENSION STRUCTURE BREAKDOWN
# ============================================================

# Example:
#
# newlist = [
#     x.upper()
#     for x in fruits
#     if "a" in x
# ]
#
#
# Parts:
#
# x.upper()
#     Expression
#
# x
#     Current item
#
# fruits
#     Iterable
#
# if "a" in x
#     Condition


# ============================================================
# QUICK REVISION
# ============================================================

# Loop Methods:
#
# 1. for loop
# 2. for loop with indexes
# 3. while loop
# 4. list comprehension
#
#
# List Comprehension Syntax:
#
# [
#     expression
#     for item in iterable
#     if condition
# ]
#
#
# Common Examples:
#
# [x for x in fruits]
#
# [x for x in fruits if "a" in x]
#
# [x.upper() for x in fruits]
#
# ["hello" for x in fruits]
#
# [x if x != "banana"
#  else "orange"
#  for x in fruits]
#
#
# Benefits:
#
# ✔ Shorter Code
# ✔ Cleaner Syntax
# ✔ Faster to Write
# ✔ Widely Used in Python
#

