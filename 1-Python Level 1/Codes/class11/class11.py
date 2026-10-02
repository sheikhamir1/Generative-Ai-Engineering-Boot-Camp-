# ============================================================
# Python While Loops and For Loops
# ============================================================

# ============================================================
# What are Loops?
# ============================================================

# Loops are used to execute a block of code repeatedly.
#
# Instead of writing the same code multiple times,
# we can use loops.
#
# Python provides two main loop types:
#
# 1. while loop
# 2. for loop


# ============================================================
# Python While Loop
# ============================================================

# A while loop executes a block of code
# as long as its condition remains True.
#
# Syntax:
#
# while condition:
#     statements


# ============================================================
# Basic While Loop
# ============================================================

i = 1

while i < 6:
    # print(i)
    i += 1

# Output:
# 1
# 2
# 3
# 4
# 5

# The loop stops when i becomes 6.


# ============================================================
# Why Increment is Important
# ============================================================

# Always update the loop variable.
#
# Otherwise,
# the condition may never become False,
# causing an infinite loop.

# Incorrect Example

# i = 1
#
# while i < 6:
#     # print(i)
#
# i never changes,
# so the loop runs forever.


# ============================================================
# Flow of a While Loop
# ============================================================

#          Start
#            │
#            ▼
#   Check Condition
#            │
#     ┌──────┴──────┐
#     │             │
#   True         False
#     │             │
#     ▼             ▼
# Execute Block    End
#     │
#     ▼
# Update Variable
#     │
#     └─────────────►


# ============================================================
# break Statement
# ============================================================

# break immediately stops the loop,
# even if the condition is still True.

i = 1

while i < 6:

    # print(i)

    if i == 4:
        break

    i += 1

# Output:
#
# 1
# 2
# 3


# ============================================================
# continue Statement
# ============================================================

# continue skips the current iteration
# and moves to the next one.

i = 0

while i < 6:

    i += 1

    if i == 3:
        continue

    # print(i)

# Output:
#
# 1
# 2
# 4
# 5
# 6


# ============================================================
# else with While Loop
# ============================================================

# The else block executes
# when the while loop finishes normally.

i = 1

while i < 6:

    # print(i)

    i += 1

else:
    # print("i is no longer less than 6")
    pass


# ============================================================
# break vs else
# ============================================================

# If break is used,
# the else block will NOT execute.

i = 1

while i < 6:

    if i == 3:
        break

    i += 1

else:
    # print("Loop Finished")
    pass

# Since break stops the loop,
# else is skipped.


# ============================================================
# Python For Loop
# ============================================================

# A for loop is used to iterate
# over a sequence.
#
# A sequence can be:
#
# ✔ List
# ✔ Tuple
# ✔ Dictionary
# ✔ Set
# ✔ String

# Syntax:
#
# for variable in sequence:
#     statements


# ============================================================
# Loop Through a List
# ============================================================

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    # print(fruit)
    pass

# Output:
#
# apple
# banana
# cherry


# ============================================================
# Loop Through a String
# ============================================================

for letter in "banana":
    # print(letter)
    pass

# Output:
#
# b
# a
# n
# a
# n
# a


# ============================================================
# break in For Loop
# ============================================================

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:

    # print(fruit)

    if fruit == "banana":
        break

# Output:
#
# apple
# banana


# ============================================================
# break Before print()
# ============================================================

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:

    if fruit == "banana":
        break

    # print(fruit)

# Output:
#
# apple


# ============================================================
# continue in For Loop
# ============================================================

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:

    if fruit == "banana":
        continue

    # print(fruit)

# Output:
#
# apple
# cherry


# ============================================================
# range() Function
# ============================================================

# range() generates a sequence of numbers.

# Syntax:
#
# range(stop)
#
# range(start, stop)
#
# range(start, stop, step)


# ============================================================
# range(stop)
# ============================================================

for x in range(6):
    # print(x)
    pass

# Output:
#
# 0
# 1
# 2
# 3
# 4
# 5

# Note:
# 6 is NOT included.


# ============================================================
# range(start, stop)
# ============================================================

for x in range(2, 7):
    # print(x)
    pass

# Output:
#
# 2
# 3
# 4
# 5


# ============================================================
# range(start, stop, step)
# ============================================================

for x in range(2, 30, 3):
    # print(x)
    pass

# Output:
#
# 2
# 5
# 8
# 11
# ...


# ============================================================
# else with For Loop
# ============================================================

# else executes when the loop
# finishes normally.

for x in range(6):

    # print(x)
    pass

else:
    # print("Finally Finished!")
    pass


# ============================================================
# break with else
# ============================================================

# If break is used,
# else will NOT execute.

for x in range(6):

    if x == 3:
        break

    # print(x)

else:
    print("Finally Finished!")
    pass


# ============================================================
# Nested Loops
# ============================================================

# A nested loop is a loop
# inside another loop.

adj = ["red", "big", "tasty"]

fruits = ["apple", "banana", "cherry"]

for adjective in adj:

    # print(adjective)
    for fruit in fruits:

        # print( fruit)
        # print(adjective, fruit)
        pass

# Output:
#
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry


# ============================================================
# How Nested Loops Work
# ============================================================

# Outer Loop
# ----------
# red
#    apple
#    banana
#    cherry
#
# big
#    apple
#    banana
#    cherry
#
# tasty
#    apple
#    banana
#    cherry

# The inner loop completes ALL its iterations
# before the outer loop moves to the next item.


# ============================================================
# pass in a For Loop
# ============================================================

# Python does not allow empty loops.

# Use pass as a placeholder.

for x in [0, 1, 2]:
    pass

# This loop does nothing,
# but it avoids a syntax error.


# ============================================================
# While vs For Loop
# ============================================================

# While Loop
# -------------------------
# Runs while a condition is True.
#
# Requires manual updating
# of the loop variable.
#
# Best when the number of
# iterations is unknown.

# Example:
#
# while balance > 0:
#     ...


# For Loop
# -------------------------
# Iterates over a sequence.
#
# Automatically moves
# to the next item.
#
# Best when iterating through
# lists, strings, tuples, etc.

# Example:
#
# for item in items:
#     ...


# ============================================================
# break vs continue
# ============================================================

# break
# -------------------------
# Stops the loop completely.

# continue
# -------------------------
# Skips the current iteration
# and continues with the next.


# ============================================================
# range() Summary
# ============================================================

# range(stop)
# -------------------------
# Starts from 0.

# Example:
#
# range(5)
#
# Result:
# 0 1 2 3 4


# range(start, stop)
# -------------------------
#
# Example:
#
# range(2, 6)
#
# Result:
# 2 3 4 5


# range(start, stop, step)
# -------------------------
#
# Example:
#
# range(2, 20, 2)
#
# Result:
# 2 4 6 8 10 ...


# ============================================================
# Important Rules
# ============================================================

# ✔ while loops use conditions.
#
# ✔ for loops iterate over sequences.
#
# ✔ break immediately exits a loop.
#
# ✔ continue skips the current iteration.
#
# ✔ else executes only if the loop
#   finishes normally.
#
# ✔ break prevents else from executing.
#
# ✔ range() does NOT include the stop value.
#
# ✔ Nested loops execute the inner loop
#   completely for each outer iteration.
#
# ✔ pass is used as a placeholder
#   for empty loops.


# ============================================================
# Quick Summary
# ============================================================

# ✔ Python has two main loops:
#     • while
#     • for
#
# ✔ while loops run while a condition is True.
# ✔ Always update the loop variable to avoid infinite loops.
# ✔ for loops iterate over sequences like lists and strings.
# ✔ break exits the loop immediately.
# ✔ continue skips the current iteration.
# ✔ else executes only when the loop ends normally.
# ✔ range() generates a sequence of numbers.
# ✔ Nested loops execute one loop inside another.
# ✔ pass creates an empty loop without causing an error.

# ------------------------------------------------------------------------------------------------------

# ============================================================
# Python Functions
# ============================================================

# ============================================================
# What is a Function?
# ============================================================

# A function is a reusable block of code
# that performs a specific task.
#
# A function runs ONLY when it is called.
#
# Functions help:
#
# ✔ Reduce code repetition
# ✔ Make programs easier to read
# ✔ Make code reusable
# ✔ Organize large programs
#
# A function can also return a value.


# ============================================================
# Creating a Function
# ============================================================

# Functions are created using
# the def keyword.
#
# Syntax:
#
# def function_name():
#     statements

def my_function():
    # print("Hello from a function")
    pass

# The function is only defined here.
# It has NOT executed yet.


# ============================================================
# Calling a Function
# ============================================================

# To execute a function,
# write its name followed by parentheses.

def my_function():
    print("Hello from a function")
    pass

# my_function()

# The function body runs only
# when it is called.


# ============================================================
# Calling a Function Multiple Times
# ============================================================

def my_function():
    print("Hello from a function")
    pass

# my_function()
# my_function()
# my_function()

# The same function can be reused
# as many times as needed.


# ============================================================
# Function Structure
# ============================================================

# Every function has three parts:
#
# 1. def keyword
# 2. Function name
# 3. Function body

# Example:
#
# def greet():
#     print("Hello")
#
# def  → Keyword
# greet → Function name
# print(...) → Function body


# ============================================================
# Function Names
# ============================================================

# Function names follow the same rules
# as variable names.
#
# Rules:
#
# ✔ Must begin with a letter or underscore (_)
#
# ✔ Can contain:
#     Letters
#     Numbers
#     Underscores
#
# ✔ Cannot contain spaces.
#
# ✔ Cannot begin with a number.
#
# ✔ Function names are case-sensitive.

# Valid Examples

def calculate_sum():
    pass

def _private_function():
    pass

def myFunction2():
    pass

# Invalid Examples

# def 2sum():
#     pass

# def my function():
#     pass


# ============================================================
# Naming Convention

# myNameCall
# MyNameCall
# my_name_call
# ============================================================

# Python recommends using
# snake_case for function names.

# Good Examples

def calculate_average():
    pass

def convert_temperature():
    pass

def print_student_details():
    pass

# Avoid unclear names like:
#
# def a():
# def test():
# def xyz():


# ============================================================
# Why Use Functions?
# ============================================================

# Without functions,
# the same code must be written repeatedly.

# Example (Without Functions)

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9

# print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9

# print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9

# print(celsius3)

# Notice the same formula
# is written three times.


# ============================================================
# Using a Function Instead
# ============================================================

# Functions let us write the code ONCE
# and reuse it many times.

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(95))
# print(fahrenheit_to_celsius(50))

# Much cleaner and easier to maintain.


# ============================================================
# Return Statement
# ============================================================

# The return statement sends
# a value back to the caller.
#
# As soon as Python executes return:
#
# ✔ The function immediately stops.
# ✔ The returned value is sent back.

def get_greeting():
    return "Hello from a function"

# message = get_greeting()

# print(message)


# ============================================================
# Using the Returned Value Directly
# ============================================================

def get_greeting():
    return "Hello from a function"

# print(get_greeting())

# The returned value can be:
#
# ✔ Printed
# ✔ Stored in a variable
# ✔ Used in calculations
# ✔ Passed to another function


# ============================================================
# Functions Without return
# ============================================================

# If a function has NO return statement,
# Python automatically returns None.

def greet():
    print("Hello")
    pass

# result = greet()

# print(result)

# Output:
# None


# ============================================================
# Difference Between print() and return
# ============================================================

# print()
# ---------------------------
# Displays output on the screen.
#
# Does NOT send a value back.

# return
# ---------------------------
# Sends a value back
# to the caller.
#
# The returned value can be reused.

# Example

def square(number):
   
    return number * number
    

result = square(5)

# print(result)


# ============================================================
# pass Statement in Functions
# ============================================================

# Python does not allow
# an empty function body.
#
# Use pass as a placeholder.

def my_function():
    pass

# This function exists,
# but currently does nothing.


# ============================================================
# Why Use pass?
# ============================================================

# pass is useful when:
#
# ✔ Planning program structure
# ✔ Developing large projects
# ✔ Writing placeholder functions
# ✔ Implementing features later


# ============================================================
# Example - Placeholder Function
# ============================================================

def calculate_discount(price):
    pass

# TODO:
# Add discount calculation later.


# ============================================================
# Function Execution Flow
# ============================================================

#            Program Starts
#                  │
#                  ▼
#        Function Definition
#                  │
#                  ▼
#        Function is Stored
#                  │
#                  ▼
#         Function is Called
#                  │
#                  ▼
#      Execute Function Body
#                  │
#        ┌─────────┴─────────┐
#        │                   │
#     return             No return
#        │                   │
#        ▼                   ▼
# Return Value            Return None


# ============================================================
# Function vs Repeated Code
# ============================================================

# Without Function
# ---------------------------
#
# Formula
# Formula
# Formula
# Formula
#
# Lots of repeated code.

# With Function
# ---------------------------
#
# Write Once
#
# Call Many Times
#
# Cleaner and reusable.


# ============================================================
# Important Rules
# ============================================================

# ✔ Functions are created using def.
#
# ✔ A function runs only when called.
#
# ✔ Function names follow variable naming rules.
#
# ✔ Python recommends snake_case names.
#
# ✔ Functions reduce code duplication.
#
# ✔ return sends a value back to the caller.
#
# ✔ A function stops executing after return.
#
# ✔ Functions without return automatically return None.
#
# ✔ pass is used as a placeholder
#   for empty functions.


# ============================================================
# Quick Summary
# ============================================================

# ✔ A function is a reusable block of code.
# ✔ Use the def keyword to define a function.
# ✔ Call a function using its name followed by ().
# ✔ Functions can be called multiple times.
# ✔ Use descriptive snake_case names for functions.
# ✔ Functions reduce repetition and improve readability.
# ✔ return sends a value back and ends the function.
# ✔ Functions without return return None by default.
# ✔ print() displays output, while return sends data back.
# ✔ Use pass as a placeholder for unfinished functions.
