# ============================================================
# Python Match Statement
# ============================================================

# ============================================================
# What is the match Statement?
# ============================================================

# The match statement is used to perform
# different actions based on different values.
#
# It is similar to the "switch" statement
# found in many other programming languages.
#
# Instead of writing many if...elif...else
# statements, you can use match for cleaner
# and more readable code.
#
# Note:
# The match statement was introduced in
# Python 3.10.


# ============================================================
# Basic Syntax
# ============================================================

# Syntax:
#
# match expression:
#     case value1:
#         statements
#
#     case value2:
#         statements
#
#     case value3:
#         statements
#
#     case _:
#         default statements


# ============================================================
# How match Works
# ============================================================

# Step 1:
# Python evaluates the expression only ONCE.
#
# Step 2:
# It compares the value with each case.
#
# Step 3:
# When a matching case is found,
# its code block executes.
#
# Step 4:
# The remaining cases are skipped.
#
# If no case matches,
# the default case (_) is executed
# if it exists.


# ============================================================
# Basic Example
# ============================================================

day = 4

match day:

    case 1:
        # print("Monday")
        pass

    case 2:
        # print("Tuesday")
        pass

    case 3:
        # print("Wednesday")
        pass

    case 4:
        # print("Thursday")
        pass

    case 5:
        # print("Friday")
        pass

    case 6:
        # print("Saturday")
        pass

    case 7:
        # print("Sunday")
        pass

# Since day = 4,
# "Thursday" would be printed.


# ============================================================
# Default Case (_)
# ============================================================

# The underscore (_) acts like the
# else block in an if statement.
#
# It runs when NO other case matches.

day = 4

match day:

    case 6:
        # print("Today is Saturday")
        pass

    case 7:
        # print("Today is Sunday")
        pass

    case _:
        # print("Looking forward to the weekend")
        pass

# Since day is neither 6 nor 7,
# the default case executes.


# ============================================================
# Why _ Must Be Last
# ============================================================

# The underscore (_) matches EVERYTHING.
#
# Therefore,
# it should always be the LAST case.

# Incorrect Example

# match value:
#
#     case _:
#         pass
#
#     case 1:
#         pass
#
# The later cases will never execute.


# ============================================================
# Combining Multiple Values
# ============================================================

# Use the pipe operator (|)
# to match multiple values.

day = 4

match day:

    case 1 | 2 | 3 | 4 | 5:
        # print("Today is a weekday")
        pass

    case 6 | 7:
        # print("I love weekends!")
        pass

# The | operator works like OR.


# ============================================================
# Match Guards (if Conditions)
# ============================================================

# A guard is an additional if condition
# attached to a case.
#
# The case matches ONLY if:
#
# ✔ The value matches.
# ✔ The guard condition is True.

month = 5
day = 4

match day:

    case 1 | 2 | 3 | 4 | 5 if month == 4:
        # print("A weekday in April")
        pass

    case 1 | 2 | 3 | 4 | 5 if month == 5:
        # print("A weekday in May")
        pass

    case _:
        # print("No Match")
        pass

# Since:
#
# day = 4
# month = 5
#
# The second case executes.


# ============================================================
# Example - Grade Checker
# ============================================================

grade = "B"

match grade:

    case "A":
        # print("Excellent")
        pass

    case "B":
        # print("Very Good")
        pass

    case "C":
        # print("Good")
        pass

    case "D":
        # print("Needs Improvement")
        pass

    case _:
        # print("Invalid Grade")
        pass


# ============================================================
# Example - Simple Calculator
# ============================================================

operator = "+"

match operator:

    case "+":
        # print("Addition")
        pass

    case "-":
        # print("Subtraction")
        pass

    case "*":
        # print("Multiplication")
        pass

    case "/":
        # print("Division")
        pass

    case _:
        # print("Unknown Operator")
        pass


# ============================================================
# match vs if...elif...else
# ============================================================

# Using if...elif...else

day = 3

if day == 1:
    pass

elif day == 2:
    pass

elif day == 3:
    pass

else:
    pass


# Using match

match day:

    case 1:
        pass

    case 2:
        pass

    case 3:
        pass

    case _:
        pass

# Both approaches produce the same result.
#
# match is usually cleaner when comparing
# one variable against many possible values.


# ============================================================
# When to Use match
# ============================================================

# ✔ Comparing one variable
#   against many fixed values.
#
# ✔ Menu-driven programs.
#
# ✔ Days of the week.
#
# ✔ Months.
#
# ✔ Commands.
#
# ✔ User choices.
#
# ✔ Status codes.


# ============================================================
# When NOT to Use match
# ============================================================

# Avoid match when:
#
# ❌ Conditions involve many comparisons.
#
# ❌ Different variables are involved.
#
# ❌ Complex logical expressions are needed.
#
# In such cases,
# use if...elif...else instead.


# ============================================================
# Flow of a match Statement
# ============================================================

#             Start
#               │
#               ▼
#     Evaluate Expression
#               │
#               ▼
#      Compare With Cases
#               │
#      ┌────────┴────────┐
#      │                 │
#    Match            No Match
#      │                 │
#      ▼                 ▼
# Execute Case     Check Next Case
#                         │
#                         ▼
#                  Default (_)
#                         │
#                         ▼
#                        End


# ============================================================
# match vs if
# ============================================================

# if Statement
# ----------------------------
# ✔ Best for complex conditions.
# ✔ Supports ranges.
# ✔ Supports logical operators.

# match Statement
# ----------------------------
# ✔ Best for matching values.
# ✔ Cleaner for many choices.
# ✔ Easier to read.


# ============================================================
# Important Rules
# ============================================================

# ✔ match evaluates the expression only once.
#
# ✔ Only the FIRST matching case executes.
#
# ✔ Remaining cases are skipped.
#
# ✔ The default case uses "_".
#
# ✔ "_" should always be the LAST case.
#
# ✔ "|" combines multiple values.
#
# ✔ Guards use an additional "if" condition.
#
# ✔ match requires Python 3.10 or later.


# ============================================================
# Quick Summary
# ============================================================

# ✔ match is an alternative to long if...elif...else chains.
# ✔ It compares one expression against multiple values.
# ✔ Only one matching case executes.
# ✔ Use "_" as the default case.
# ✔ Use "|" to combine multiple matching values.
# ✔ Use "if" after a case to create a guard condition.
# ✔ match is ideal for menus, commands, days, months,
#   and other fixed-value comparisons.
# ✔ Use if statements for complex logical conditions.
