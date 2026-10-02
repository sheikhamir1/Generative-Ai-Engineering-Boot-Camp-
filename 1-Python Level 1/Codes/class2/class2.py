# Python Data Types
# Built-in Data Types
""" 
Text Type     : 	str
Numeric Types : 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type  : 	dict
Set Types     : 	set, frozenset
Boolean Type  : 	bool
Binary Types  : 	bytes, bytearray, memoryview
None Type     : 	NoneType
 
"""
# x = 5
# print(type(x))

# ==========================================
# Python Data Types - Complete Examples
# ==========================================

# ==========================================
# 1. str (String)
# Used to store text
# ==========================================
# x = "Hello World"

# print("String Value:", x)
# print("Type:", type(x))
# print()

# # ==========================================
# # 2. int (Integer)
# # Used to store whole numbers
# # ==========================================

# x = 20

# print("Integer Value:", x)
# print("Type:", type(x))
# print()


# # ==========================================
# # 3. float
# # Used to store decimal numbers
# # ==========================================
# x = 20.5

# print("Float Value:", x)
# print("Type:", type(x))
# print()

# # ==========================================
# # 4. complex
# # Used for complex numbers
# # ==========================================

# x = 1j

# print("Complex Value:", x)
# print("Type:", type(x))
# print()

# # ==========================================
# # 5. list
# # Ordered, changeable collection
# # ==========================================
# x = ["apple", "banana", "cherry"]

# print("List Value:", x)
# print("Type:", type(x))
# print()

# # ==========================================
# # 6. tuple
# # Ordered, unchangeable collection
# # ==========================================
# x = ("apple", "banana", "cherry")

# print("Tuple Value:", x)
# print("Type:", type(x))
# print()


# # ==========================================
# # 7. range
# # Generates a sequence of numbers
# # ==========================================
# x = range(6)

# print(x)
# print("Range Value:", list(x))
# print("Type:", type(x))
# print()


# # ==========================================
# # 8. dict (Dictionary)
# # Stores data as key-value pairs
# # ==========================================
# x = {
#     "name": "John",
#     "age": 36
# }

# print("Dictionary Value:", x)
# print("Type:", type(x))
# print()


# # ==========================================
# # 9. set
# # Unordered collection of unique values
# # ==========================================
# x = {"apple", "banana", "cherry"}

# print("Set Value:", x)
# print("Type:", type(x))
# print()


# # ==========================================
# # 10. frozenset
# # Immutable (unchangeable) set
# # ==========================================
# x = frozenset({"apple", "banana", "cherry"})

# print("FrozenSet Value:", x)
# print("Type:", type(x))
# print()


# # ==========================================
# # 11. bool
# # Represents True or False
# # ==========================================
# x = False

# print("Boolean Value:", x)
# print("Type:", type(x))
# print()


# # ==========================================
# # 12. bytes
# # Immutable sequence of bytes
# # ==========================================
# x = b"Hello"

# print("Bytes Value:", x)
# print("Type:", type(x))
# print()

# # ==========================================
# # 13. bytearray
# # Mutable sequence of bytes
# # ==========================================
# x = bytearray(5)

# print("ByteArray Value:", x)
# print("Type:", type(x))
# print()


# # ==========================================
# # 14. memoryview
# # Provides memory access without copying
# # ==========================================
# x = memoryview(bytes(5))

# print("MemoryView Value:", x)
# print("Type:", type(x))
# print()



# # ==========================================
# # 15. NoneType
# # Represents absence of a value
# # ==========================================
# x = None

# print("None Value:", x)
# print("Type:", type(x))
# print()


# # Setting the Specific Data Type
# x = str("Hello World")

# ---------------------------------------------------------------------------------------------------

# Python Numbers
#INT - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

# x = 1
# y = 35656222554887711
# z = -3255522

# print(type(x))
# print(type(y))
# print(type(z)) 

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

# x = 1.10
# y = 1.0
# z = -35.59

# print(type(x))
# print(type(y))
# print(type(z)) 

# Float can also be scientific numbers with an "e" to indicate the power of 10.
# x = 35e3
# y = 12E4
# z = -87.7e100

# print(x)
# print(y)
# print(z)

# print(type(x))
# print(type(y))
# print(type(z)) 

# Complex numbers are written with a "j" as the imaginary part:

# x = 3+5j
# y = 5j
# z = -5j

# print(type(x))
# print(type(y))
# print(type(z)) 

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

# x = 1    # int
# y = 2.88  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c)) 


# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# import random
# print(random.randrange(1, 100)) 

# -----------------------------------------------------------------------------------------------
# Python Casting
""" 
Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:
    int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
    float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
    str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""
# x = int(1)
# y = int(2.8)
# z = int("2354567")
# print(x)
# print(y)
# print(z)

# x = float(1)
# y = float(2.8)
# z = float("3")
# w = float("4.2")
# print(x)
# print(y)
# print(z)
# print(w)

# x = str("s1") # x will be 's1'
# y = str(2)    # y will be '2'
# z = str(3.0)  # z will be '3.0' 
# print(x)
# print(y)
# print(z)

