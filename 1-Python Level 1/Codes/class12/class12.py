
# ==========================================================
# 1. Arguments
# ==========================================================

# Information can be passed into functions as arguments.
# Arguments are specified inside the parentheses when calling a function.

def my_function(fname):
    # print(fname + " Refsnes")
    pass

# Example calls
my_function("Emil")
my_function("Tobias")
my_function("Linus")


# ==========================================================
# 2. Parameters vs Arguments
# ==========================================================

# Parameter = variable in function definition
# Argument = actual value passed during function call

def greet(name):   # name is a parameter
    # print("Hello", name)
    pass

greet("Emil")      # "Emil" is an argument


# ==========================================================
# 3. Number of Arguments
# ==========================================================

# A function must receive the correct number of arguments.

def full_name(fname, lname):
    print(fname + " " + lname)
    pass

# full_name("Emil", "Refsnes")

# Wrong example (will raise TypeError if uncommented)
# full_name("Emil")


# ==========================================================
# 4. Default Parameter Values
# ==========================================================

def hello(name="friend"):
    # print("Hello", name)
    pass

hello("Emil")
hello("Tobias")
hello()
hello("Linus")


def country_info(country="Norway"):
    # print("I am from", country)
    pass

country_info("Sweden")
country_info("India")
country_info()
country_info("Brazil")


# ==========================================================
# 5. Keyword Arguments
# ==========================================================

def pet(animal, name):
    # print("I have a", animal)
    # print("My", animal + "'s name is", name)
    pass

# pet(animal="dog", name="Buddy")
# pet(name="Buddy", animal="dog")


# ==========================================================
# 6. Positional Arguments
# ==========================================================

# pet("dog", "Buddy")

# Order matters
# pet("Buddy", "dog")


# ==========================================================
# 7. Mixing Positional and Keyword Arguments
# ==========================================================

def pet_info(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)
    pass

# pet_info("dog", name="Buddy", age=5)


# ==========================================================
# 8. Passing Different Data Types
# ==========================================================

# Passing a list

def show_fruits(fruits):
    for fruit in fruits:
        # print(fruit)
        pass

my_fruits = ["apple", "banana", "cherry"]
show_fruits(my_fruits)


# Passing a dictionary

def show_person(person):
    # print(person)
    # print("Name:", person["name"])
    # print("Age:", person["age"])
    pass

my_person = {"name": "Emil", "age": 25}
show_person(my_person)


# ==========================================================
# 9. Return Values
# ==========================================================

def add(x, y):
    return x + y

result = add(5, 3)
# print(result)


# ==========================================================
# 10. Returning Different Data Types
# ==========================================================

# Returning a list

def get_fruits():
    return ["apple", "banana", "cherry"]

fruits = get_fruits()
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])


# Returning a tuple

def get_coordinates():
    return (10, 20)

# x, y = get_coordinates()

# print("x:", x)
# print("y:", y)


# ==========================================================
# 11. Positional-Only Arguments
# ==========================================================

def positional_only(name, /):
    # print("Hello", name)
    pass

positional_only("Emil")

# Error if uncommented
# positional_only(name="Emil")


# ==========================================================
# 12. Without Positional-Only
# ==========================================================

def normal_argument(name):
    # print("Hello", name)
    pass

normal_argument(name="Emil")


# ==========================================================
# 13. Keyword-Only Arguments
# ==========================================================

def keyword_only(*, name):
    # print("Hello", name)
    pass

# keyword_only(name="Emil")

# Error if uncommented
# keyword_only("Emil")


# ==========================================================
# 14. Without Keyword-Only
# ==========================================================

def normal_keyword(name):
    # print("Hello", name)
    pass

normal_keyword("Emil")


# ==========================================================
# 15. Combining Positional-Only and Keyword-Only
# ==========================================================

def combined(a, b, /, *, c, d):
    return a + b + c + d

result = combined(5, 10, c=15, d=20)

# print(result)


# ---------------------------------------------------------------------------------------------

# ==========================================================
# 1. Introduction
# ==========================================================

# By default, functions require the correct number of arguments.
# *args and **kwargs allow functions to accept an unknown
# number of arguments.


# ==========================================================
# 2. Arbitrary Arguments - *args
# ==========================================================

def kids_example(*kids):
    
    # print("The youngest child is", kids[2])
    pass

kids_example("Emil", "Tobias", "Linus")


# ==========================================================
# 3. What is *args?
# ==========================================================

def show_args(*args):
    # print("Type:", type(args))
    # print("First argument:", args[0])
    # print("Second argument:", args[1])
    # print("All arguments:", args)
    pass

show_args("Emil", "Tobias", "Linus")


# ==========================================================
# 4. Using *args with Regular Arguments
# ==========================================================

def greet_all(greeting, *names):
    for name in names:
        # print(greeting, name)
        pass

greet_all("Hello", "Emil", "Tobias", "Linus")


# ==========================================================
# 5. Practical Example - Sum Any Number of Values
# ==========================================================

def total_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# print(total_sum(1, 2, 3))
# print(total_sum(10, 20, 30, 40))
# print(total_sum(5))


# ==========================================================
# 6. Practical Example - Maximum Value
# ==========================================================

def maximum(*numbers):
    if len(numbers) == 0:
        return None

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

# print(maximum(3, 7, 2, 9, 1,5,2,4,5,7,5,3,12,21))


# ==========================================================
# 7. Arbitrary Keyword Arguments - **kwargs
# ==========================================================

def kid_info(**kid):
    # print(kid)
    # print("His last name is", kid["lname"])
    pass

kid_info(fname="Tobias", lname="Refsnes", city="kolkata", age=12)


# ==========================================================
# 8. What is **kwargs?
# ==========================================================

def show_kwargs(**myvar):
    # print("Type:", type(myvar))
    # print("Name:", myvar["name"])
    # print("Age:", myvar["age"])
    # print("All data:", myvar)
    pass

show_kwargs(name="Tobias", age=30, city="Bergen")


# ==========================================================
# 9. Using **kwargs with Regular Arguments
# ==========================================================

def user_details(username, **details):
    # print("Username:", username)
    # print("Additional details:")

    for key, value in details.items():
        # print(key + ":", value)
        pass

user_details("emil123", age=25, city="Oslo", hobby="coding")


# ==========================================================
# 10. Combining *args and **kwargs
# ==========================================================

def combined(title, *args, **kwargs):
    # print("Title:", title)
    # print("Positional arguments:", args)
    # print("Keyword arguments:", kwargs)
    pass

combined("User Info", "Emil", "Tobias", age=25, city="Oslo")


# ==========================================================
# 11. Unpacking Lists with *
# ==========================================================

def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
# result = add_three(*numbers)

# print(result)


# ==========================================================
# 12. Unpacking Dictionaries with **
# ==========================================================

def full_name(fname, lname):
    print("Hello", fname, lname)
    pass

person = {
    "fname": "Emil",
    "lname": "Refsnes"
}


# full_name(**person)
# full_name(fname="Emil", lname="Refsnes")

# ==========================================================
# Summary
# ==========================================================

# *args
# -----
# • Collects any number of positional arguments.
# • Stored as a tuple.
# • Used in function definitions.

# **kwargs
# --------
# • Collects any number of keyword arguments.
# • Stored as a dictionary.
# • Used in function definitions.

# Unpacking
# ---------
# *  -> Unpacks lists/tuples into positional arguments.
# ** -> Unpacks dictionaries into keyword arguments.

# Function Definition:
# def func(a, *args, **kwargs):

# Function Call:
# func(*list_values, **dict_values)

# --------------------------------------------------------------------------------------------------------------

# ==========================================================
# 1. Scope
# ==========================================================

# Scope determines where a variable can be accessed.
# A variable is only available inside the region where it is created.


# ==========================================================
# 2. Local Scope
# ==========================================================

# A variable created inside a function belongs to the
# local scope of that function.

def myfunc():
    x = 300

    # print(x)

myfunc()

# Error if uncommented because x only exists inside myfunc()
# print(x)


# ==========================================================
# 3. Function Inside Function
# ==========================================================

# A local variable can also be accessed by functions
# defined inside the same function.

def outer_function():
    x = 300

    def inner_function():
        # print(x)
        pass

    inner_function()

outer_function()


# ==========================================================
# 4. Global Scope
# ==========================================================

# Variables created outside all functions are global variables.

x = 300

def show_global():
    # print(x)
    pass

show_global()

# print(x)


# ==========================================================
# 5. Local and Global Variables with Same Name
# ==========================================================

# Python treats local and global variables with the
# same name as different variables.

x = 300

def myfunc():
    x = 200

    # print("Local x:", x)

myfunc()

# print("Global x:", x)


# ==========================================================
# 6. The global Keyword
# ==========================================================

# Use global to create a global variable from inside
# a function.

def create_global():
    global y
    y = 300

create_global()

# print(y)


# ==========================================================
# 7. Modifying a Global Variable
# ==========================================================

x = 300

def change_global():
    global x
    x = 200

change_global()

# print(x)


# ==========================================================
# 8. The nonlocal Keyword
# ==========================================================

# nonlocal is used inside nested functions.
# It modifies a variable belonging to the outer function.

def outer():
    x = "Jane"

    def inner():
        nonlocal x
        x = "hello"

    inner()

    return x

result = outer()

# print(result)


# ==========================================================
# 9. LEGB Rule
# ==========================================================

# Python searches for variables in this order:
#
# L = Local
# E = Enclosing
# G = Global
# B = Built-in

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"

        # print("Inner:", x)

    inner()

    # print("Outer:", x)

outer()

# print("Global:", x)


# ==========================================================
# 10. LEGB Rule Example (Accessing Enclosing Scope)
# ==========================================================

def first():
    x = "Outer Variable"

    def second():
        # print(x)
        pass

    second()

first()


# ==========================================================
# 11. Built-in Scope Example
# ==========================================================

# Python finally checks the built-in namespace if
# a variable or function is not found elsewhere.

numbers = [5, 2, 8, 1]

largest = max(numbers)
smallest = min(numbers)
length = len(numbers)

# print(largest)
# print(smallest)
# print(length)


# ==========================================================
# Summary
# ==========================================================

# Local Scope
# -----------
# • Variables created inside a function.
# • Accessible only inside that function.

# Enclosing Scope
# ----------------
# • Variables in an outer (enclosing) function.
# • Accessible by nested functions.

# Global Scope
# ------------
# • Variables created outside all functions.
# • Accessible everywhere.

# Built-in Scope
# --------------
# • Python's built-in names like:
#   max(), min(), len(), print(), sum(), etc.

# global Keyword
# --------------
# • Creates or modifies global variables inside functions.

# nonlocal Keyword
# ----------------
# • Modifies variables from the enclosing function.

# LEGB Search Order
# -----------------
# 1. Local
# 2. Enclosing
# 3. Global
# 4. Built-in