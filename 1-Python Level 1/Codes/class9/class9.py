# ============================================================
# Python If Statements
# ============================================================

# ============================================================
# What is an If Statement?
# ============================================================

# An if statement is used to make decisions in Python.
#
# It executes a block of code ONLY if a specified
# condition evaluates to True.
#
# Syntax:
#
# if condition:
#     statement(s)
#

# If the condition is False,
# the code block is skipped.


# ============================================================
# Comparison (Relational) Operators
# ============================================================

# Python supports the following comparison operators:

# ==   Equal to
# !=   Not equal to
# <    Less than
# <=   Less than or equal to
# >    Greater than
# >=   Greater than or equal to

# These operators return either:
#
# True
# False


# ============================================================
# Basic If Statement
# ============================================================

a = 33
b = 200

if b > a:
    # print("b is greater than a")
    pass

# Since 200 > 33,
# the condition is True,
# so the code inside the if block executes.


# ============================================================
# How If Statements Work
# ============================================================

# Step 1:
# Evaluate the condition.
#
# Step 2:
# If True →
# Execute the indented block.
#
# Step 3:
# If False →
# Skip the block.

number = 15

if number > 0:
    # print("The number is positive")
    pass


# ============================================================
# Indentation
# ============================================================

# Python uses indentation to define code blocks.
#
# Unlike many programming languages,
# Python does NOT use {} braces.

# Correct Example

age = 20

if age >= 18:
    # print("Adult")
    pass


# Incorrect Example (Will Raise IndentationError)

# if age >= 18:
#     print("Adult")


# Important:
#
# ✔ Use spaces or tabs.
# ✔ Be consistent.
# ✔ Standard practice is 4 spaces.


# ============================================================
# Multiple Statements Inside an If Block
# ============================================================

age = 20

if age >= 18:
    # print("You are an adult.")
    # print("You can vote.")
    # print("You have full legal rights.")
    pass

# Every statement inside the block
# must have the same indentation level.


# ============================================================
# Using Boolean Variables
# ============================================================

# Boolean variables can be used directly
# in an if statement.

is_logged_in = True

if is_logged_in:
    # print("Welcome back!")
    pass

# No comparison is needed because
# is_logged_in already contains
# either True or False.


# ============================================================
# Truthy and Falsy Values
# ============================================================

# Python automatically treats many values
# as either True or False.

# Falsy Values
# ----------------------
# False
# None
# 0
# 0.0
# ""
# ''
# []
# ()
# {}
# set()

# Truthy Values
# ----------------------
# True
# Any non-zero number
# Any non-empty string
# Any non-empty list
# Any non-empty tuple
# Any non-empty dictionary
# Any non-empty set

# Example

name = "Rohan"

if name:
    # print("Name exists.")
    pass

# Since the string is not empty,
# it is considered True.


# ============================================================
# Python Elif Statement
# ============================================================

# elif means:
#
# "If the previous condition was False,
# then check this condition."

# Syntax
#
# if condition1:
#     ...
# elif condition2:
#     ...
# elif condition3:
#     ...


# ============================================================
# Basic Elif Example
# ============================================================

a = 33
b = 33

if b > a:
    # print("b is greater than a")
    pass

elif a == b:
    # print("a and b are equal")
    pass

# Since the first condition is False,
# Python checks the elif condition.


# ============================================================
# Multiple Elif Statements
# ============================================================

score = 95

if score >= 90:
    # print("Grade: A")
    pass

elif score >= 80:
    # print("Grade: B")
    pass

elif score >= 70:
    # print("Grade: C")
    pass

elif score >= 60:
    # print("Grade: D")
    pass

# Since score is 75,
# "Grade C" would be printed.


# ============================================================
# How Elif Works
# ============================================================

# Python checks conditions
# from TOP to BOTTOM.
#
# As soon as one condition becomes True:
#
# ✔ Execute that block.
# ✔ Ignore all remaining elif statements.


# ============================================================
# Example - Age Categories
# ============================================================

age = 25

if age < 13:
    # print("Child")
    pass

elif age < 20:
    # print("Teenager")
    pass

elif age < 65:
    # print("Adult")
    pass

elif age >= 65:
    # print("Senior")
    pass


# ============================================================
# Example - Day of Week
# ============================================================

day = 3

if day == 1:
    # print("Monday")
    pass

elif day == 2:
    # print("Tuesday")
    pass

elif day == 3:
    # print("Wednesday")
    pass

elif day == 4:
    # print("Thursday")
    pass

elif day == 5:
    # print("Friday")
    pass

elif day == 6:
    # print("Saturday")
    pass

elif day == 7:
    # print("Sunday")
    pass


# ============================================================
# Python Else Statement
# ============================================================

# else executes when ALL previous conditions
# are False.

# Syntax
#
# if condition:
#     ...
# else:
#     ...


# ============================================================
# Basic Else Example
# ============================================================

a = 200
b = 33

if b > a:
    # print("b is greater than a")
    pass

elif a == b:
    # print("a and b are equal")
    pass

else:
    # print("a is greater than b")
    pass


# ============================================================
# Else Without Elif
# ============================================================

a = 200
b = 33

if b > a:
    # print("b is greater than a")
    pass

else:
    # print("b is not greater than a")
    pass

# This creates a simple
# True / False decision.


# ============================================================
# How Else Works
# ============================================================

# else acts as the DEFAULT block.
#
# It runs only when every
# previous condition is False.

# Important:
#
# ✔ else must always come LAST.
#
# ❌ elif cannot appear after else.


# ============================================================
# Example - Even or Odd
# ============================================================

number = 6

if number % 2 == 0:
    # print("Even")
    pass

else:
    # print("Odd")
    pass


# ============================================================
# Complete if-elif-else Chain
# ============================================================

temperature = 22

if temperature > 30:
    # print("It's hot outside!")
    pass

elif temperature > 20:
    # print("It's warm outside.")
    pass

elif temperature > 10:
    # print("It's cool outside.")
    pass

else:
    # print("It's cold outside!")
    pass


# ============================================================
# Example - User Validation
# ============================================================

username = "Emil"

if len(username) > 0:
    # print(f"Welcome, {username}!")
    pass

else:
    # print("Error: Username cannot be empty.")
    pass


# ============================================================
# Flow of if-elif-else
# ============================================================

#                Start
#                  │
#                  ▼
#          Check if condition
#                  │
#          ┌───────┴────────┐
#          │                │
#        True             False
#          │                │
#          ▼                ▼
#   Execute if block    Check elif
#                           │
#                    ┌──────┴──────┐
#                    │             │
#                  True          False
#                    │             │
#                    ▼             ▼
#          Execute elif block   else block
#
# Only ONE block executes.


# ============================================================
# if vs elif vs else
# ============================================================

# if
# --------------------------
# Starts a decision.

# elif
# --------------------------
# Checks another condition
# only if previous ones failed.

# else
# --------------------------
# Executes when every previous
# condition is False.


# ============================================================
# Important Rules
# ============================================================

# ✔ Every if statement starts with "if".
#
# ✔ elif is optional.
#
# ✔ You can have multiple elif statements.
#
# ✔ else is optional.
#
# ✔ There can only be ONE else.
#
# ✔ else must always be the LAST block.
#
# ✔ Python executes only the FIRST matching condition.


# ============================================================
# Quick Summary
# ============================================================

# ✔ if executes code when a condition is True.
# ✔ Comparison operators return True or False.
# ✔ Python uses indentation instead of {} braces.
# ✔ Boolean variables can be used directly in if statements.
# ✔ Empty values are considered False (Falsy).
# ✔ Non-empty values are considered True (Truthy).
# ✔ elif checks another condition if previous ones fail.
# ✔ Multiple elif statements are allowed.
# ✔ Python stops checking after the first True condition.
# ✔ else executes when all previous conditions are False.
# ✔ Only ONE block from an if-elif-else chain executes.

# ------------------------------------------------------------------------------

# ============================================================
# Python Shorthand If, Logical Operators,
# Nested If, and Pass Statement
# ============================================================

# ============================================================
# Python Shorthand If
# ============================================================

# A shorthand if is a one-line version of an if statement.
#
# It is useful when there is only ONE statement
# inside the if block.

# Syntax:
#
# if condition: statement


# ============================================================
# Basic Shorthand If
# ============================================================

a = 5
b = 2

if a > b:
    # print("a is greater than b")
    pass

# Equivalent shorthand version:
#
# if a > b: print("a is greater than b")
#
# Note:
# The colon (:) is still required.


# ============================================================
# Shorthand If...Else (Ternary Operator)
# ============================================================

# When there is only ONE statement
# for both if and else,
# you can write them on one line.

a = 2
b = 330

# print("A") if a < b else print("B")


# This is called a:
#
# ✔ Conditional Expression
# ✔ Ternary Operator


# ============================================================
# Assigning Values Using Shorthand If
# ============================================================

a = 10
b = 20

bigger = a if a < b else b

# print("Bigger is:", bigger)

# General Syntax:
#
# variable = value_if_true if condition else value_if_false


# ============================================================
# Multiple Conditions on One Line
# ============================================================

# You can chain conditional expressions,
# but avoid making them too complex.

a = 330
b = 330

# print("A") if a > b else print("=") if a == b else print("B")

# Output:
# =


# ============================================================
# Practical Example - Maximum Value
# ============================================================

x = 15
y = 20

max_value = x if x > y else y

# print("Maximum Value:", max_value)


# ============================================================
# Practical Example - Default Value
# ============================================================

username = ""

display_name = username if username else "Guest"

# print("Welcome,", display_name)

# Since username is empty,
# "Guest" is assigned.


# ============================================================
# When to Use Shorthand If
# ============================================================

# ✔ Simple conditions
# ✔ One-line assignments
# ✔ Return values
# ✔ Small print statements

# Avoid shorthand if:
#
# ❌ Complex conditions
# ❌ Multiple statements
# ❌ Long expressions

# In such cases,
# use a normal if-else block.


# ============================================================
# Python Logical Operators
# ============================================================

# Logical operators combine multiple conditions.

# Python has three logical operators:
#
# and
# or
# not


# ============================================================
# AND Operator
# ============================================================

# Both conditions must be True.

a = 200
b = 33
c = 500

if a > b and c > a:
    # print("Both conditions are True")
    pass

# Truth Table
#
# True  and True  → True
# True  and False → False
# False and True  → False
# False and False → False


# ============================================================
# OR Operator
# ============================================================

# At least ONE condition must be True.

a = 200
b = 33
c = 500

if a > b or a > c:
    # print("At least one condition is True")
    pass

# Truth Table
#
# True  or True  → True
# True  or False → True
# False or True  → True
# False or False → False


# ============================================================
# NOT Operator
# ============================================================

# not reverses a Boolean value.

a = 33
b = 200

if not a > b:
    # print("a is NOT greater than b")
    pass

# Example:
#
# not True  → False
# not False → True


# ============================================================
# Combining Logical Operators
# ============================================================

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    # print("Discount Applies!")
    pass

# Operator precedence:
#
# 0. ()
# 1. not
# 2. and
# 3. or


# ============================================================
# Parentheses for Clarity
# ============================================================

# Parentheses improve readability
# and control evaluation order.

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    # print("Great day for outdoor activities!")
    pass


# ============================================================
# Example - User Authentication
# ============================================================

username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
    # print("Login Successful")
    pass

else:
    # print("Login Failed")
    pass


# ============================================================
# Example - Range Checking
# ============================================================

score = 85

if score >= 0 and score <= 100:
    # print("Valid Score")
    pass

else:
    # print("Invalid Score")
    pass


# ============================================================
# Python Nested If Statements
# ============================================================

# An if statement inside another if statement
# is called a Nested If.

# Syntax:
#
# if condition1:
#     if condition2:
#         ...


# ============================================================
# Basic Nested If Example
# ============================================================

x = 41

if x > 10:
    # print("Above Ten")

    if x > 20:
        # print("And also above 20!")
        pass

    else:
        # print("But not above 20.")
        pass


# ============================================================
# Example - Driving Eligibility
# ============================================================

age = 25
has_license = True

if age >= 18:

    if has_license:
        # print("You can drive.")
        pass

    else:
        # print("You need a license.")
        pass

else:
    # print("Too young to drive.")
    pass


# ============================================================
# Multiple Levels of Nesting
# ============================================================

score = 85
attendance = 90
submitted = True

if score >= 60:

    if attendance >= 80:

        if submitted:
            # print("Pass with good standing.")
            pass

        else:
            # print("Pass but assignment missing.")
            pass

    else:
        # print("Pass but low attendance.")
        pass

else:
    # print("Fail")
    pass


# ============================================================
# Nested If vs Logical Operators
# ============================================================

# Nested If

temperature = 25
is_sunny = True

if temperature > 20:

    if is_sunny:
        # print("Perfect beach weather!")
        pass


# Same Logic Using AND

if temperature > 20 and is_sunny:
    # print("Perfect beach weather!")
    pass

# Use:
#
# Nested if
# ----------
# ✔ Complex logic
# ✔ Multiple actions
#
# AND
# ----
# ✔ Simple conditions
# ✔ Cleaner code


# ============================================================
# Example - Login Validation
# ============================================================

username = "Emil"
password = "python123"
is_active = True

if username:

    if password:

        if is_active:
            # print("Login Successful")
            pass

        else:
            # print("Account is inactive.")
            pass

    else:
        # print("Password required.")
        pass

else:
    # print("Username required.")
    pass


# ============================================================
# Example - Grade Calculation
# ============================================================

score = 92
extra_credit = 5

if score >= 90:

    if extra_credit > 0:
        # print("A+ Grade")
        pass

    else:
        # print("A Grade")
        pass

elif score >= 80:
    # print("B Grade")
    pass

else:
    # print("C Grade or below")
    pass


# ============================================================
# Python pass Statement
# ============================================================

# The pass statement does NOTHING.
#
# It is used when Python expects a statement,
# but you have nothing to write yet.


# ============================================================
# Basic Example
# ============================================================

a = 33
b = 200

if b > a:
    pass

# No error occurs,
# even though the block is empty.


# ============================================================
# Why Use pass?
# ============================================================

# ✔ Placeholder for future code
# ✔ During development
# ✔ Empty functions
# ✔ Empty classes
# ✔ Empty loops
# ✔ Empty if blocks


# ============================================================
# Example - Future Implementation
# ============================================================

age = 16

if age < 18:
    pass      # TODO: Add underage logic

else:
    # print("Access Granted")
    pass


# ============================================================
# pass vs Comments
# ============================================================

# Incorrect Example

# if score > 90:
#     # Excellent student

# The above causes an IndentationError because
# comments are ignored by Python.


# Correct Example

score = 85

if score > 90:
    pass

# print("Score Processed")


# ============================================================
# pass Inside if-elif-else
# ============================================================

value = 50

if value < 0:
    # print("Negative")
    pass

elif value == 0:
    pass

else:
    # print("Positive")
    pass


# ============================================================
# pass with Functions
# ============================================================

def calculate_discount(price):
    pass

# Function exists,
# but no logic has been written yet.


# ============================================================
# Flow of an if Statement
# ============================================================

#              Start
#                │
#                ▼
#       Evaluate Condition
#                │
#        ┌───────┴────────┐
#        │                │
#      True            False
#        │                │
#        ▼                ▼
# Execute Block      Skip Block


# ============================================================
# Flow of Nested If
# ============================================================

#          Condition 1
#               │
#      ┌────────┴────────┐
#      │                 │
#    True             False
#      │                 │
#      ▼                 ▼
# Condition 2         Skip
#      │
# ┌────┴─────┐
# │          │
# True     False
# │          │
# ▼          ▼
# Execute   Else


# ============================================================
# Quick Comparison
# ============================================================

# Normal If
# -----------------------
# Multiple lines
# Easier to read

# Shorthand If
# -----------------------
# One line
# Good for simple logic

# Nested If
# -----------------------
# If inside another if

# pass
# -----------------------
# Placeholder
# Does nothing


# ============================================================
# Quick Summary
# ============================================================

# ✔ Shorthand if is used for one-line conditions.
# ✔ Ternary operators assign values in one line.
# ✔ and requires ALL conditions to be True.
# ✔ or requires AT LEAST ONE condition to be True.
# ✔ not reverses a Boolean value.
# ✔ Parentheses improve readability and control evaluation order.
# ✔ Nested if statements allow multiple levels of decision-making.
# ✔ Simple nested conditions can often be replaced with "and".
# ✔ pass is a placeholder statement that performs no action.
# ✔ pass prevents syntax errors when a code block is intentionally empty.