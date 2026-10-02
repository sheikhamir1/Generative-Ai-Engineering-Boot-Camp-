# Python Strings
# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# print("Hello")
# print('Hello')

""" Quotes Inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string: """

# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')

# a = "Hello"
# print(a) 

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# a = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a) 

""" Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string. """

# a = "Hello, World!"
# print(a[12])


# Looping Through a String

# for x in "banana":
#   print(x)

# String Length
# a = "Hello, World!"
# print(len(a))
# print(a)

# Check String
# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")


# Check if NOT
# txt = "The best things in life are free!"
# print("expensive" not in txt)

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")


# Python - Slicing Strings
# Get the characters from position 2 to position 5 (not included):

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[7:])


# Negative Indexing
# Use negative indexes to start the slice from the end of the string: 

# b = "Hello, World!"
# print(b[-5:-2])

"""
=========================================
        PYTHON STRING METHODS
=========================================

Strings in Python come with many built-in methods
that help you manipulate and work with text easily.

A string method is a function that belongs to a string
object and performs a specific operation on it.

Commonly Used String Methods:
1. upper()   -> Converts text to uppercase.
2. lower()   -> Converts text to lowercase.
3. strip()   -> Removes extra spaces from beginning/end.
4. replace() -> Replaces part of a string with another.
5. split()   -> Splits a string into a list.

=========================================
1. upper() Method
=========================================

Purpose:
Converts all characters in a string to UPPERCASE.

Syntax:
string.upper()

Example:
"""

# a = "Hello, World!"
# print("Original String:", a)
# print("Uppercase:", a.upper())



"""
=========================================
2. lower() Method
=========================================

Purpose:
Converts all characters in a string to lowercase.

Syntax:
string.lower()

Example:
"""

a = "Hello, World!"
# print("Original String:", a)
# print("Lowercase:", a.lower())



"""
=========================================
3. strip() Method
=========================================

Purpose:
Removes whitespace (spaces, tabs, new lines)
from the beginning and end of a string.

Whitespace means:
- Space (' ')
- Tab ('\\t')
- New line ('\\n')

Syntax:
string.strip()

Example:
"""

a = "   Hello, World!   "
# print("\nBefore strip():", a)
# print("After strip():",a.strip())


"""
=========================================
4. replace() Method
=========================================

Purpose:
Replaces a specified part of a string with
another value.

Syntax:
string.replace(old, new)

Parameters:
old -> Text to be replaced
new -> Replacement text

Example:
"""

# a = "Hello, World!"
# print("\nOriginal String:", a)
# print("After replace():", a.replace("H", "J"))

"""
=========================================
5. split() Method
=========================================

Purpose:
Splits a string into a list based on a separator.

Syntax:
string.split(separator)

The separator determines where the string
should be divided.

Example:
"""

# a = "Hello, World!"
# print("\nOriginal String:", a)
# print("After split():", a.split(","))

a = "Hello"
# print("\nOriginal String:", a)
# print("After split():", a.split(" "))


"""
=========================================
    PYTHON STRING CONCATENATION
    & STRING FORMATTING
=========================================

String Concatenation:
Concatenation means joining or combining
two or more strings together.

Python provides the '+' operator to combine strings.

String Formatting:
String formatting is the process of inserting
variables, values, or expressions into a string.

Common Methods:
1. String Concatenation (+)
2. F-Strings (Recommended)
3. format() Method

=========================================
1. STRING CONCATENATION
=========================================

Purpose:
Combine two or more strings into one string.

Syntax:
string1 + string2

Example:
"""

a = "Hello"
b = "World"

c = a + b

# print("Concatenated String:", c)




"""
=========================================
2. CONCATENATION WITH SPACE
=========================================

Purpose:
Add a space between words while combining strings.

Example:
"""

a = "Hello"
b = "World"

c = a + " " + b

# print("\nWith Space:", c)




"""
=========================================
WHY THIS CAUSES AN ERROR?
=========================================

Python does NOT allow direct concatenation
of strings and integers using '+'.

Example:
"""

# age = 36

# # This would cause an error:
# txt = "My name is John, I am " + age

# TypeError:
# can only concatenate str (not "int") to str


"""
=========================================
3. F-STRINGS (RECOMMENDED)
=========================================

Purpose:
Insert variables directly into a string.

Introduced:
Python 3.6+

Syntax:
f"Text {variable}"

Advantages:
✔ Easy to read
✔ Fast
✔ Preferred method

Example:
"""

age = 36

txt = f"My name is John, I am {age}"

# print("\nF-String Example:")
# print(txt)



"""
=========================================
4. PLACEHOLDERS IN F-STRINGS
=========================================

Purpose:
Insert variables into strings using {}.

Anything inside {} is evaluated and inserted
into the string.

Example:
"""

price = 59

txt = f"The price is {price} dollars"

# print("\nPlaceholder Example:")
# print(txt)



"""
=========================================
5. MODIFIERS IN F-STRINGS
=========================================

Purpose:
Control how values are displayed.

Modifier Syntax:
{value:.2f}

Meaning:
.2f = Fixed-point number with 2 decimal places

Example:
"""

price = 59

txt = f"The price is {price:.2f} dollars"

# print("\nModifier Example:")
# print(txt)




"""
=========================================
6. USING EXPRESSIONS IN F-STRINGS
=========================================

Purpose:
Perform calculations directly inside
the placeholder.

Example:
"""

txt = f"The price is {2 * 5} dollars"

# print("\nMath Expression Example:")
# print(txt)




"""
=========================================
7. USING FUNCTIONS IN F-STRINGS
=========================================

Purpose:
Call Python functions inside placeholders.

Example:
"""

name = "python"

txt = f"The word in uppercase is {name.upper()}"

# print("\nFunction Example:")
# print(txt)



"""
=========================================
8. format() METHOD
=========================================

Purpose:
Insert values into a string using placeholders.

Syntax:
"Text {}".format(value)

Example:
"""

name = "John"
age = 36

txt = "My name is {}, I am {} years old".format(name, age)

# print("\nformat() Method Example:")
# print(txt)



"""
=========================================
SUMMARY TABLE
=========================================

Method/Concept      Purpose
------------------------------------------------
+                   Join strings
" "                 Add spaces while joining
f""                 Modern string formatting
{}                  Placeholder
:.2f                2 decimal places
Expressions         Perform calculations
Functions           Execute functions
format()            Older formatting method
"""


# ------------------------------------------------------------------------------------

"""
=========================================
    PYTHON ESCAPE CHARACTERS
    & STRING METHODS
=========================================

Strings are one of the most commonly used
data types in Python.

In this lesson, we will learn:

1. Escape Characters
2. Why Escape Characters are Needed
3. Common Escape Sequences
4. Python String Methods
5. Categories of String Methods

=========================================
PART 1: ESCAPE CHARACTERS
=========================================

What is an Escape Character?

An escape character is a backslash 
followed by another character.

Purpose:
Allows special characters to be included
inside a string.

Syntax:

\\character

Example:
"""

# This causes an error:
# txt = "We are the so-called "Vikings" from the north."

# Python becomes confused because it thinks
# the string ends before Vikings.

"""
=========================================
USING ESCAPE CHARACTER
=========================================
"""

txt = "We are the so-called \"Vikings\" from the north."

# print(txt)

# Output:
# We are the so-called "Vikings" from the north.


"""
=========================================
COMMON ESCAPE CHARACTERS
=========================================
"""

# print("\n1. Single Quote (\\'):")
# print('It\\\'s Python')

# Output:
# It's Python


# print("\n2. Double Quote (\\\"):")
# print("He said, \"Hello\"")

# Output:
# He said, "Hello"


# print("\n3. Backslash (\\\\):")
# print("C:\\Users\\Rohan")

# Output:
# C:\Users\Rohan


# print("\n4. New Line (\\n):")
# print("Hello\nWorld")

# Output:
# Hello
# World


# print("\n5. Tab (\\t):")
# print("Name\tAge")

# Output:
# Name    Age


# print("\n6. Carriage Return (\\r):")
# print("Hello\rPython")

# Output may vary depending on terminal.


# print("\n7. Backspace (\\b):")
# print("Helloo\b")

# Removes previous character.


# print("\n8. Form Feed (\\f):")
# print("Hello\fWorld")

# Output depends on environment.


"""
=========================================
ADVANCED ESCAPE SEQUENCES
=========================================
"""

# print("\n9. Octal Value (\\101):")
# print("\101")

# Output:
# A


# print("\n10. Hexadecimal Value (\\x41):")
# print("\x41")

# Output:
# A


"""
=========================================
SUMMARY OF ESCAPE CHARACTERS
=========================================

Escape Sequence      Meaning
-----------------------------------------
\\'                  Single Quote
\\"                  Double Quote
\\\\                 Backslash
\\n                  New Line
\\r                  Carriage Return
\\t                  Tab
\\b                  Backspace
\\f                  Form Feed
\\ooo                Octal Value
\\xhh                Hexadecimal Value

=========================================
PART 2: PYTHON STRING METHODS
=========================================

String methods are built-in functions
that perform operations on strings.

IMPORTANT:
String methods DO NOT modify the original
string.

They return a NEW string instead.

Example:
"""

name = "python"

# print("\nOriginal:", name)
# print("Uppercase:", name.upper())

# print("Original Still Exists:", name)

# Output:
# Original: python
# Uppercase: PYTHON
# Original Still Exists: python


"""
=========================================
STRING METHODS BY CATEGORY
=========================================
"""

"""
-----------------------------------------
1. CASE CONVERSION METHODS
-----------------------------------------
"""

text = "python programming"

# print("\nCASE CONVERSION")

# print(text.upper())       # PYTHON PROGRAMMING
# print(text.lower())       # python programming
# print(text.capitalize())  # Python programming
# print(text.title())       # Python Programming
# print(text.swapcase())    # PYTHON PROGRAMMING
# print(text.casefold())    # python programming


"""
-----------------------------------------
2. SEARCHING METHODS
-----------------------------------------
"""

text = "Python is easy to learn"

# print("\nSEARCHING")

# print(text.find("easy"))
# print(text.index("easy"))
# print(text.count("P"))

# find() returns -1 if not found
# index() gives an error if not found


"""
-----------------------------------------
3. CHECKING METHODS
-----------------------------------------
"""

# print("\nCHECKING METHODS")

# print("Python".isalpha())
# print("123".isdigit())
# print("Python123".isalnum())
# print("python".islower())
# print("PYTHON".isupper())
# print(" ".isspace())


"""
Common Checking Methods:

isalnum()
isalpha()
isascii()
isdecimal()
isdigit()
isidentifier()
islower()
isnumeric()
# isprintable()
isspace()
istitle()
isupper()
"""


"""
-----------------------------------------
4. TRIMMING METHODS
-----------------------------------------
"""

text = "   Python   "

# print("\nTRIMMING")

# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

"""
strip()    -> Remove both sides
lstrip()   -> Remove left side
rstrip()   -> Remove right side
"""


"""
-----------------------------------------
5. REPLACEMENT METHODS
-----------------------------------------
"""

text = "I like Java"

# print("\nREPLACEMENT")

# print(text.replace("Java", "Python"))

# Output:
# I like Python


"""
-----------------------------------------
6. SPLITTING METHODS
-----------------------------------------
"""

text = "Apple,Banana,Mango"

# print("\nSPLITTING")

# print(text.split(","))
# print(text.rsplit(",", 1))
# print("Hello\nWorld".splitlines())

"""
split()
rsplit()
splitlines()
"""


"""
-----------------------------------------
7. JOINING METHODS
-----------------------------------------
"""

fruits = ["Apple", "Banana", "Mango"]

# print("\nJOINING")

# print(", ".join(fruits))

# Output:
# Apple, Banana, Mango


"""
-----------------------------------------
8. ALIGNMENT METHODS
-----------------------------------------
"""

text = "Python"

# print("\nALIGNMENT")

# print(text.center(20))
# print(text.ljust(20))
# print(text.rjust(20))

"""
center()
ljust()
rjust()
"""


"""
-----------------------------------------
9. START/END CHECK METHODS
-----------------------------------------
"""

text = "Python Programming"

# print("\nSTART/END CHECK")

# print(text.startswith("Python"))
# print(text.endswith("Programming"))

# Output:
# True
# True


"""
-----------------------------------------
10. ZERO FILLING
-----------------------------------------
"""

num = "25"

# print("\nZERO FILL")
# print(num.zfill(5))

# Output:
# 00025


"""
=========================================
MOST IMPORTANT STRING METHODS
=========================================

Beginner Priority:

1. upper()
2. lower()
3. strip()
4. replace()
5. split()
6. join()
7. find()
8. count()
9. startswith()
10. endswith()

Master these first before learning
all remaining methods.

=========================================
KNOWLEDGE HIERARCHY
=========================================

Python Programming
│
├── Data Types
│   └── String
│
├── String Fundamentals
│   ├── Indexing
│   ├── Slicing
│   ├── Concatenation
│   ├── Formatting
│   └── Escape Characters
│
└── String Methods
    ├── Case Conversion
    ├── Searching
    ├── Validation
    ├── Splitting
    ├── Joining
    ├── Trimming
    ├── Alignment
    └── Formatting

=========================================
REAL-WORLD APPLICATIONS
=========================================

• Cleaning user input
• Form validation
• Processing files
• Chat applications
• Search systems
• Data analysis
• Web development
• AI and NLP projects

"""
