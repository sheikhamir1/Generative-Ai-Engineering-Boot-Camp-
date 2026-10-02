"""
==========================================================
            PYTHON TRY - EXCEPT
==========================================================

WHAT IS EXCEPTION HANDLING?
---------------------------

An Exception is an error that occurs
while a program is running.

Normally,

when an error occurs,

Python stops the program.

Using

try...except

allows you to handle the error
without crashing the program.

==========================================================
try - except STRUCTURE
==========================================================

try:
    # Code that may cause an error

except:
    # Code that runs if an error occurs
"""



# ==========================================================
# BASIC try - except
# ==========================================================

"""
The code inside the try block
is executed first.

If an error occurs,

the except block runs.
"""
# print(x)


# print("Before Start")

# try:
#     print(x)   # x is not defined

# except:
#     print("An exception occurred")

# Uncomment to test
# x = 10
# try:
#     print(x)
# except:
#     print("An exception occurred")

# print("After Start")


# ==========================================================
# WITHOUT try - except
# ==========================================================

"""
Without exception handling,

the program stops immediately.
"""

# Uncomment to test
# print(x)

# Output:
# NameError: name 'x' is not defined



# ==========================================================
# HANDLING SPECIFIC EXCEPTIONS
# ==========================================================

"""
You can handle different
types of errors separately.
"""
# x = "Rohan"
# try:
#     print(x);

# except NameError:
#     print("Variable x is not defined")

# except:
#     print("Something else went wrong")

# Uncomment to test
# try:
    # print(x)
# except NameError:
    # print("Variable x is not defined")
# except:
    # print("Something else went wrong")



# ==========================================================
# ELSE BLOCK
# ==========================================================

"""
The else block runs

ONLY

if no exception occurs.
"""

# try:
#     print("Hello")

# except:
#     print("Something went wrong")

# else:
#     print("Nothing went wrong")

# Uncomment to test
# try:
    # print("Hello")
# except:
    # print("Something went wrong")
# else:
    # print("Nothing went wrong")



# ==========================================================
# FINALLY BLOCK
# ==========================================================

"""
The finally block always runs,

whether an error occurs or not.

Useful for:

✔ Closing files
✔ Closing database connections
✔ Cleaning up resources
"""

# try:
#     print(x)

# except:
#     print("Something went wrong")

# finally:
#     print("The 'try except' is finished")

# Uncomment to test
# try:
#     print("Rohan")
# except:
#     print("Something went wrong")
# finally:
#     print("The 'try except' is finished")



# ==========================================================
# FINALLY WITH FILE HANDLING
# ==========================================================

"""
Always close a file
using the finally block.
"""

# try:

#     f = open("demofile.txt")

#     try:
#         f.write("Lorum Ipsum")

#     except:
#         print("Something went wrong when writing to the file")

#     finally:
#         f.close()

# except:
#     print("Something went wrong when opening the file")

# Uncomment to test
# try:
#     f = open("demofile.txt")
#     try:
#         f.write("Lorum Ipsum")
#     except:
        # print("Something went wrong when writing to the file")
#     finally:
#         f.close()
# except:
    # print("Something went wrong when opening the file")



# ==========================================================
# RAISE AN EXCEPTION
# ==========================================================

"""
Use

raise

to manually generate
an exception.
"""

# x = -1

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# Uncomment to test
# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")



# ==========================================================
# RAISE A SPECIFIC EXCEPTION
# ==========================================================

"""
You can raise specific
exception types.

Example:

TypeError
"""

# x = "hello"
# print(isinstance(x, str))

# if not isinstance(x, int):
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")

# Uncomment to test
# x = "hello"
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")



"""
==========================================================
SUMMARY
==========================================================

Exception Handling
│
├── try
├── except
├── Multiple except Blocks
├── else
├── finally
└── raise

Flow

try
 │
 ├── Error?
 │      │
 │      ├── Yes → except
 │      └── No  → else
 │
 └──────────────→ finally (Always Runs)
"""

# -------------------------------------------------------------------------------------------------------------------

"""
==========================================================
            PYTHON STRING FORMATTING
==========================================================

WHAT IS STRING FORMATTING?
--------------------------

String formatting is used to insert
values into a string.

Python supports:

1. F-Strings (Recommended)
2. format() Method (Older Method)

F-Strings were introduced in Python 3.6
and are the preferred way to format strings.

==========================================================
F-STRINGS
==========================================================

Add the letter

f

before a string to create an f-string.
"""

txt = f"The price is 49 dollars"

# Uncomment to test
# print(txt)



# ==========================================================
# PLACEHOLDERS {}
# ==========================================================

"""
Use curly braces {}

to insert values into a string.
"""

price = 59

txt = f"The price is {price} dollars"

# Uncomment to test
# print(txt)



# ==========================================================
# FORMAT NUMBERS
# ==========================================================

"""
Use

:.2f

to display a number
with 2 decimal places.
"""

price = 59

txt = f"The price is {price:.2f} dollars"

# Uncomment to test
# print(txt)

# Output
# The price is 59.00 dollars



# ==========================================================
# FORMAT A DIRECT VALUE
# ==========================================================

"""
You can format values directly
without using a variable.
"""

txt = f"The price is {95:.2f} dollars"

# Uncomment to test
# print(txt)



# ==========================================================
# MATH OPERATIONS
# ==========================================================

"""
Python expressions can be
written inside {}.
"""

txt = f"The price is {20 * 59} dollars"

# Uncomment to test
# print(txt)



# ==========================================================
# OPERATIONS WITH VARIABLES
# ==========================================================

price = 59
tax = 0.25

txt = f"The price is {price + (price * tax)} dollars"

# Uncomment to test
# print(txt)



# ==========================================================
# IF...ELSE INSIDE F-STRINGS
# ==========================================================

price = 51

txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"

# Uncomment to test
# print(txt)



# ==========================================================
# USING FUNCTIONS
# ==========================================================

"""
Functions can be called
inside {}.
"""

fruit = "apples"

txt = f"I love {fruit.upper()}"

# Uncomment to test
# print(txt)



# ==========================================================
# USER-DEFINED FUNCTION
# ==========================================================

def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at {myconverter(30000)} meter altitude"

# Uncomment to test
# print(txt)



# ==========================================================
# THOUSAND SEPARATOR
# ==========================================================

"""
Use

:,

to display commas.
"""

price = 59000

txt = f"The price is {price:,} dollars"

# Uncomment to test
# print(txt)

# Output
# The price is 59,000 dollars



# ==========================================================
# COMMON FORMAT MODIFIERS
# ==========================================================

"""
Alignment

:<    Left Align

:>    Right Align

:^    Center Align

----------------------------------------------------------

Signs

:+    Show + and -

:-    Show - Only

:=    Sign at Left

:     Space Before Positive

----------------------------------------------------------

Numbers

:,    Comma Separator

:_    Underscore Separator

:b    Binary

:d    Decimal

:o    Octal

:x    Hexadecimal (Lowercase)

:X    Hexadecimal (Uppercase)

----------------------------------------------------------

Scientific

:e    Scientific (e)

:E    Scientific (E)

----------------------------------------------------------

Floating Point

:f    Fixed Point

:F    Fixed Point (Uppercase)

:g    General

:G    General (Uppercase)

----------------------------------------------------------

Others

:c    Unicode Character

:n    Number Format

:%    Percentage
"""



"""
==========================================================
STRING format() METHOD
==========================================================

Before Python 3.6,

format()

was commonly used for
string formatting.
"""

price = 49

txt = "The price is {} dollars"

# Uncomment to test
# print(txt.format(price))



# ==========================================================
# DECIMAL FORMATTING
# ==========================================================

txt = "The price is {:.2f} dollars"

# Uncomment to test
# print(txt.format(price))



# ==========================================================
# MULTIPLE VALUES
# ==========================================================

quantity = 3
itemno = 567
price = 49

myorder = "I want {} pieces of item number {} for {:.2f} dollars."

# Uncomment to test
# print(myorder.format(quantity, itemno, price))



# ==========================================================
# INDEX NUMBERS
# ==========================================================

"""
Use index numbers

{0}
{1}
{2}

to specify the position
of each value.
"""

quantity = 3
itemno = 567
price = 49

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."

# Uncomment to test
# print(myorder.format(quantity, itemno, price))



# ==========================================================
# REUSE THE SAME VALUE
# ==========================================================

age = 36
name = "John"

txt = "His name is {1}. {1} is {0} years old."

# Uncomment to test
# print(txt.format(age, name))



# ==========================================================
# NAMED INDEXES
# ==========================================================

"""
Named placeholders
make the code easier
to read.
"""

myorder = "I have a {carname}, it is a {model}."

# Uncomment to test
# print(myorder.format(carname="Ford", model="Mustang"))



"""
==========================================================
SUMMARY
==========================================================

String Formatting
│
├── F-Strings (Recommended)
│      ├── {}
│      ├── Variables
│      ├── Expressions
│      ├── Functions
│      ├── if...else
│      └── Modifiers
│
├── Common Modifiers
│      ├── :.2f
│      ├── :,
│      ├── :<
│      ├── :>
│      ├── :^
│      ├── :b
│      ├── :x
│      └── :%
│
└── format()
       ├── {}
       ├── Multiple Values
       ├── Index Numbers
       └── Named Indexes
"""

# -------------------------------------------------------------------------------------------------------

# print("Enter your name:")
# name = input()
# print(f"Hello {name}")

# name = input("Enter your name:")
# print(f"Hello {name}")
# fav1 = input("What is your favorite animal:")
# fav2 = input("What is your favorite color:")
# fav3 = input("What is your favorite number:")
# print(fav3)
# print(type(fav3))
# print(f"Do you want a {fav2} {fav1} with {fav3} legs?")
# import math

# x = input("Enter a number:")

# #find the square root of the number:
# y = math.sqrt(float(x))

# print(f"The square root of {x} is {y}")

# y = True
# while y == True:
#   x = input("Enter a number:")
#   try:
#     x = float(x);
#     y = False
#   except:
#     print("Wrong input, please try again.")

# print("Thank you!") 

# -----------------------------------------------------------------------------------------------------

"""
==========================================================
        PYTHON VIRTUAL ENVIRONMENT (venv)
==========================================================

WHAT IS A VIRTUAL ENVIRONMENT?
------------------------------

A Virtual Environment is an isolated
Python environment for a project.

Each virtual environment has:

✔ Its own Python interpreter
✔ Its own installed packages
✔ Separate dependencies
✔ Isolation from other projects

WHY USE A VIRTUAL ENVIRONMENT?

✔ Prevents package conflicts
✔ Keeps system Python clean
✔ Makes projects portable
✔ Allows different package versions

==========================================================
CREATE A VIRTUAL ENVIRONMENT
==========================================================

Python provides the built-in

venv

module.

Command:

python -m venv myfirstproject
"""



# ==========================================================
# PROJECT STRUCTURE
# ==========================================================

"""
After creating the virtual environment,
the folder looks similar to:

myfirstproject/
│
├── Include/
├── Lib/
├── Scripts/
├── .gitignore
└── pyvenv.cfg
"""



# ==========================================================
# ACTIVATE THE VIRTUAL ENVIRONMENT
# ==========================================================

"""
Windows

myfirstproject\Scripts\activate

macOS / Linux

source myfirstproject/bin/activate
"""



# ==========================================================
# ACTIVE ENVIRONMENT
# ==========================================================

"""
After activation,
your terminal changes.

Example:

(myfirstproject) C:\Users\YourName>

The project name in brackets
shows the virtual environment
is active.
"""



# ==========================================================
# INSTALL PACKAGES
# ==========================================================

"""
Use pip to install packages
inside the active environment.

Example:

pip install cowsay
"""



# ==========================================================
# USING AN INSTALLED PACKAGE
# ==========================================================

"""
Example file:

test.py
"""

# import cowsay

# Uncomment to test
# cowsay.cow("Good Mooooorning!")



# ==========================================================
# RUN THE PROGRAM
# ==========================================================

"""
Run the Python file.

Command:

python test.py

If the virtual environment
is active,

the package will work.
"""



# ==========================================================
# DEACTIVATE THE ENVIRONMENT
# ==========================================================

"""
To leave the virtual environment:

deactivate

After deactivation,
the terminal returns
to the normal prompt.
"""



# ==========================================================
# RUNNING OUTSIDE THE ENVIRONMENT
# ==========================================================

"""
If the package was installed
only inside the virtual environment,

running the program outside it
will raise an error.

Example:

ModuleNotFoundError:
No module named 'cowsay'
"""



# ==========================================================
# REACTIVATE THE ENVIRONMENT
# ==========================================================

"""
The virtual environment
is not deleted after deactivation.

Activate it again using
the activate command,

and all installed packages
will be available again.
"""



# ==========================================================
# DELETE A VIRTUAL ENVIRONMENT
# ==========================================================

"""
To permanently remove
a virtual environment,

delete its folder.

Windows Command:

rmdir /s /q myfirstproject

You can also delete the folder
manually from File Explorer.
"""



"""
==========================================================
SUMMARY
==========================================================

Virtual Environment
│
├── python -m venv project_name
├── Activate Environment
│      ├── Windows
│      └── macOS / Linux
├── Install Packages
│      └── pip install package_name
├── Run Python Files
├── deactivate
├── Reactivate Anytime
└── Delete Environment Folder
"""