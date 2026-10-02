# print("hello world")
# print("next Step")

# if 5 > 2:
#     print("Five is greater than two!")


# print("Hello"); print("How are you?"); print("Bye bye!") 
# print("Hello World!", end=" ")
# print("I will print on the same line.")

# print(3)
# print(358)
# print(50000)

# print("3 + 3")
# print(2 * 5)

# print("I am", 35, "years old.")

# x = 5
# y = "rohan"
# print(y )
# print(x )

# x = "R"
# print(x )


# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0 
# # print(x)
# # print(type(x))
# # print(y)
# # print(type(y)) 
# # print(z)
# # print(type(z)) 

# x = str(300)
# print(x)
# print(type(x))


# x = "John"
# print(x)
# #double quotes are the same as single quotes:
# x = 'John'
# print(x)

# a = 4
# A = "Sally"

# print(a)
# print(A)

# descriptive name (age, carname, total_volume)

# Rules for Python variables:

#     A variable name must start with a letter or the underscore character
#     A variable name cannot start with a number
#     A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#     Variable names are case-sensitive (age, Age and AGE are three different variables)
#     A variable name cannot be any of the Python keywords.

# a12 = 12
# print(a12)

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"


# print(myvar)
# print(my_var)
# print(_my_var)
# print(myVar)
# print(MYVAR)
# print(myvar2)


""" 
Multi Words Variable Names

Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:
Camel Case

Each word, except the first, starts with a capital letter:
myVariableName = "John"
Pascal Case

Each word starts with a capital letter:
MyVariableName = "John"
Snake Case

Each word is separated by an underscore character:
my_variable_name = "John"
"""

# Python Variables - Assign Multiple Values
# x, y, z, zz = "Orange", "Banana", "Cherry" , "test"
# print(x)
# print(y)
# print(z)
# print(zz)

# One Value to Multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# Unpack a Collection
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)


# x = "Python is awesome"
# print(x)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = 5
# y = 10
# print(x + y)

# x = 5
# y = "John"
# print(x + y)

# x = 5
# y = "John"
# print(x, y)

# Global Variables

# Variables that are created outside of a function (as in all of the examples in the previous Section) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc() 

# x = "awesome"
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x) 

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x) 

# Also, use the global keyword if you want to change a global variable inside a function.
# x = "awesome"
# def myfunc():
# #   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x) 


