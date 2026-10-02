"""
==========================================================
                PYTHON DECORATORS
==========================================================

WHAT IS A DECORATOR?
--------------------
A decorator is a special function that adds extra functionality
to another function WITHOUT modifying the original function.

Think of it like this:

Original Function
       │
       ▼
Decorator
       │
       ▼
New Function (with extra behavior)

Syntax:

@decorator_name
def my_function():
    pass

is the same as writing:

my_function = decorator_name(my_function)

==========================================================
"""

# ==========================================================
# EXAMPLE 1: BASIC DECORATOR
# ==========================================================

"""
Goal:
Convert the returned string into UPPERCASE.

Flow:

myfunction()
      │
      ▼
decorator (changecase)
      │
      ▼
myinner()
      │
      ▼
func() → "Hello Sally"
      │
      ▼
.upper()
      │
      ▼
"HELLO SALLY"
"""


# def changecase(func):
#     """
#     This is the decorator.

#     It accepts another function as an argument.
#     """

#     def myinner():
#         """
#         Wrapper function.

#         Instead of directly calling myfunction(),
#         Python actually calls this wrapper.
#         """

#         # Call original function
#         text = func()

#         # Convert to uppercase
#         return text.upper()

#     # Return the wrapper
#     return myinner


# @changecase
# def myfunction():
#     return "Hello Sally"

# result = changecase(myfunction)
# print(result())

# Uncomment to test
# print(myfunction())



# ==========================================================
# EXAMPLE 2: SAME DECORATOR USED MULTIPLE TIMES
# ==========================================================

"""
One decorator can decorate many functions.

        changecase
         /      \
        /        \
myfunction()  otherfunction()
"""


# def changecase(func):

#     def myinner():
#         return func().upper()

#     return myinner


# @changecase
# def myfunction():
#     return "Hello Sally"


# @changecase
# def otherfunction():
#     return "I am speed!"


# Uncomment to test
# print(myfunction())
# print(otherfunction())



# ==========================================================
# EXAMPLE 3: DECORATOR WITH FUNCTION ARGUMENTS
# ==========================================================

"""
Problem:

Our wrapper currently accepts NO arguments.

def myinner():

But our function needs one argument:

myfunction("John")

So wrapper must also accept one argument.
"""


def changecase(func):

    def myinner(name):
        return func(name).upper()

    return myinner


# @changecase
def myfunction(name):
    return "Hello " + name

newfunc = changecase(myfunction)
# print(newfunc("Rohan"))

# Uncomment to test
# print(myfunction("John"))



# ==========================================================
# EXAMPLE 4: USING *args AND **kwargs
# ==========================================================

"""
Problem:

What if decorated function has:

1 argument?
2 arguments?
10 arguments?
keyword arguments?

Instead of writing:

def myinner(a,b,c,d):

Python provides:

*args
**kwargs

*args
------
Collects ALL positional arguments into a tuple.

Example:
func(1,2,3)

args becomes:
(1,2,3)

--------------------------------------------

**kwargs
---------
Collects ALL keyword arguments into a dictionary.

Example:
func(name="John", age=20)

kwargs becomes:

{
    "name":"John",
    "age":20
}

This makes the decorator work with ANY function.
"""


def changecase(func):

    def myinner(*args, **kwargs):
        print("I am Coming Form Inner Func")
        return func(*args, **kwargs).upper()

    return myinner


# @changecase
def myfunction(name, name2):
    return f"{name}, {name2}"

result = changecase(myfunction)
# print(result("Rohan", "Rahul\n"))

# Uncomment to test
# print(myfunction("John"))

def newfunc(*names):
    return f"{names}"

new_fun_result = changecase(newfunc)
# print(new_fun_result("Rohan", "Rahul","Aliya","Alisha"))


# ==========================================================
# EXAMPLE 5: DECORATOR WITH ITS OWN ARGUMENTS
# ==========================================================

"""
Sometimes the DECORATOR itself needs arguments.

Example:

@changecase(1)

Notice:

1 is NOT passed to myfunction().

Instead,

it is passed to the decorator.

Because of this we need THREE functions.

Level 1
--------
Receives decorator argument

Level 2
--------
Receives original function

Level 3
--------
Runs whenever function is called
"""


def changecase(mode):
    """
    mode is the decorator argument.

    mode = 1 → lowercase

    mode = anything else → uppercase
    """

    def decorator(func):

        def myinner():

            if mode == 1:
                return func().lower()

            else:
                return func().upper()

        return myinner

    return decorator


@changecase(0)
def myfunction():
    return "Hello Linus"


# Uncomment to test
# print(myfunction())



# ==========================================================
# EXAMPLE 6: MULTIPLE DECORATORS
# ==========================================================

"""
You can stack decorators.

Python applies them from bottom to top.

Example:

@changecase
@addgreeting
def myfunction():

Execution:

Step 1

myfunction()

returns

"Tobias"

↓

Step 2

addgreeting()

returns

"Hello Tobias Have a good day!"

↓

Step 3

changecase()

returns

"HELLO TOBIAS HAVE A GOOD DAY!"
"""


def changecase(func):

    def myinner(name):
        return func(name).upper()

    return myinner


def addgreeting(func):

    def myinner(name):
        return "Hello " + func(name) + " Have a good day!"

    return myinner


@changecase
@addgreeting
def myfunction(name):
    return name


# Uncomment to test
# print(myfunction("Rohan"))



# ==========================================================
# EXAMPLE 7: FUNCTION METADATA
# ==========================================================

"""
Every Python function has metadata.

Common metadata:

__name__
---------
Function name

__doc__
--------
Documentation string (docstring)

Let's see function name.
"""


def myfunction():
    """Simple function"""
    return "Have a great day!"


# Uncomment to test
# print(myfunction.__doc__)

# Output:
# myfunction



# ==========================================================
# EXAMPLE 8: METADATA LOST AFTER DECORATION
# ==========================================================

"""
Problem:

After decoration,

myfunction

becomes

myinner

because decorator returned myinner.

So metadata changes.

Result:

print(myfunction.__name__)

prints

myinner

instead of

myfunction
"""


def changecase(func):

    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Have a great day!"

# result = changecase(myfunction)
# print(result.__name__)

# Uncomment to test
# print(myfunction.__name__)

# Output:
# myinner



# ==========================================================
# EXAMPLE 9: PRESERVING METADATA USING functools.wraps
# ==========================================================

"""
Solution:

Use functools.wraps

It copies metadata from original function
to wrapper.

Without wraps:

__name__ = myinner

With wraps:

__name__ = myfunction
"""

import functools
# print(functools)

def changecase(func):

    # @functools.wraps(func)
    def myinner():
        """Inner docstring"""
        return func().upper()

    return myinner


@changecase
def myfunction():
    """Original docstring"""
    return "Have a great day!"


# Uncomment to test
# print(myfunction.__name__)
# print(myfunction.__doc__)

# Output:
# myfunction

# Uncomment to test
# print(myfunction.__doc__)

# Output:
# Original docstring



# ==========================================================
# SUMMARY
# ==========================================================

"""
Decorator Hierarchy

Decorator
│
├── Basic Decorator
│
├── Multiple Decorator Usage
│
├── Decorating Functions with Arguments
│
├── Using *args and **kwargs
│
├── Decorator with Arguments (Decorator Factory)
│
├── Multiple Decorators
│
└── functools.wraps
        │
        ├── Preserve __name__
        └── Preserve __doc__


Remember:

@decorator

is equivalent to

function = decorator(function)

Decorator = accepts a function
Wrapper   = runs before/after original function
Original Function = remains unchanged

This is why decorators are heavily used in:

✔ Flask
✔ Django
✔ FastAPI
✔ Logging
✔ Authentication
✔ Authorization
✔ Performance Timing
✔ Caching
✔ Validation
✔ Access Control
✔ Retry Mechanisms

They allow you to add behavior without modifying the original code.
"""

# ---------------------------------------------------------------------------------------------------------------

"""
==========================================================
                PYTHON LAMBDA FUNCTIONS
==========================================================

WHAT IS A LAMBDA FUNCTION?
--------------------------

A lambda function is a SMALL anonymous function.

Anonymous means:
It has NO function name.

Normal Function:

def add(a, b):
    return a + b

Lambda Function:

lambda a, b: a + b

Both do the same thing.

The main difference is:

Normal Function
---------------
✔ Has a name
✔ Can contain multiple statements
✔ Can have loops
✔ Can have conditions
✔ Can have multiple return paths

Lambda Function
---------------
✔ No name
✔ Only ONE expression
✔ Automatically returns the result
✔ Best for short operations

==========================================================

GENERAL SYNTAX

lambda arguments : expression

Example:

lambda x : x + 10

Breakdown

lambda
    Keyword used to create lambda function

x
    Input argument

:
    Separates arguments from expression

x + 10
    Expression
    The value of this expression is automatically returned.

Equivalent Normal Function

def addTen(x):
    return x + 10

==========================================================
"""


# ==========================================================
# EXAMPLE 1: SIMPLE LAMBDA FUNCTION
# ==========================================================

"""
Goal:
Add 10 to the given number.

Lambda:

lambda a : a + 10

Equivalent Normal Function

def addTen(a):
    return a + 10
"""

# Store lambda function inside a variable
x = lambda a: a + 10

# Uncomment to test
# print(x(5))

# Output:
# 15



# ==========================================================
# EXAMPLE 2: LAMBDA WITH MULTIPLE ARGUMENTS
# ==========================================================

"""
Lambda functions can accept ANY number of arguments.

Example:

lambda a, b : a * b

Equivalent Normal Function

def multiply(a, b):
    return a * b
"""

x = lambda a, b: a * b

# Uncomment to test
# print(x(5, 6))

# Output:
# 30



# ==========================================================
# EXAMPLE 3: THREE ARGUMENTS
# ==========================================================

"""
Lambda can also take three or more arguments.

Equivalent Normal Function

def add(a, b, c):
    return a + b + c
"""

x = lambda a, b, c: a + b + c

# Uncomment to test
# print(x(5, 6, 2))

# Output:
# 13



# ==========================================================
# WHY USE LAMBDA FUNCTIONS?
# ==========================================================

"""
Lambda functions become powerful when returned
from another function.

Example:

myfunc(2)

returns

lambda a : a * 2

This technique is called a:

Function Factory

because one function creates another function.

Flow

myfunc(2)
      │
      ▼
returns

lambda a : a * 2

Store it

mydoubler

Later

mydoubler(10)

↓

20
"""



# ==========================================================
# EXAMPLE 4: FUNCTION RETURNING A LAMBDA
# ==========================================================

"""
Normal Function

Receives one number

Returns a lambda function.
"""


def myfunc(n):

    """
    n becomes fixed inside the returned lambda.
    """

    return lambda a: a * n


# Create a function that always doubles numbers
mydoubler = myfunc(2)

# Uncomment to test
# print(mydoubler(11))

# Output:
# 22



# ==========================================================
# EXAMPLE 5: CREATE A TRIPLER
# ==========================================================

"""
Now we create another function.

Instead of multiplying by 2,

it multiplies by 3.
"""

mytripler = myfunc(3)

# Uncomment to test
# print(mytripler(11))

# Output:
# 33



# ==========================================================
# EXAMPLE 6: CREATE MULTIPLE FUNCTIONS
# ==========================================================

"""
Same function factory

creates many functions.

myfunc(2)
↓

Multiply by 2

myfunc(3)
↓

Multiply by 3

myfunc(5)
↓

Multiply by 5

No need to rewrite the multiplication logic.
"""

mydoubler = myfunc(2)
mytripler = myfunc(3)

# Uncomment to test
# print(mydoubler(11))
# print(mytripler(11))

# Output
# 22
# 33



# ==========================================================
# LAMBDA WITH BUILT-IN FUNCTIONS
# ==========================================================

"""
Lambda functions are commonly used with:

1. map()
2. filter()
3. sorted()

These functions expect another function as input.

Instead of defining a normal function,

we often use lambda.
"""



# ==========================================================
# EXAMPLE 7: LAMBDA WITH map()
# ==========================================================

"""
map()

Purpose
-------

Apply a function to EVERY element
of an iterable.

Example List

[1,2,3,4,5]

Lambda

lambda x : x * 2

Result

[2,4,6,8,10]

Flow

Original List
      │
      ▼
map()
      │
      ▼
Lambda runs on every item
      │
      ▼
New List
"""

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))


# numbers ─────────► [1,2,3,4,5]
# doubled ─────────► [2,4,6,8,10]


# Uncomment to test
# print(doubled)

# Output
# [2,4,6,8,10]
# map(Function, list)



# ==========================================================
# EXAMPLE 8: LAMBDA WITH filter()
# ==========================================================

"""
filter()

Purpose
-------

Keep only elements
for which lambda returns True.

Lambda

lambda x : x % 2 != 0

Meaning

Keep only ODD numbers.

Flow

Original List
      │
      ▼
Lambda checks every number

True

↓

Keep

False

↓

Discard
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

odd_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Uncomment to test
# print(odd_numbers)

# Output
# [1,3,5,7]



# ==========================================================
# EXAMPLE 9: LAMBDA WITH sorted()
# ==========================================================

"""
sorted()

Purpose
-------

Sort data.

Normally

sorted()

sorts naturally.

But

key=

lets us define HOW to sort.

Lambda acts as the sorting key.
"""



"""
Each tuple

(Name, Age)

Lambda

lambda x : x[1]

means

Sort using

Age

because

index 1

is the second element.
"""

students = [

    ("Emil", 25),

    ("Tobias", 22),

    ("Linus", 28)

]

sorted_students = sorted(
    students,
    key=lambda x: x[1]
)

# Uncomment to test
# print(sorted_students)

# Output
# [('Tobias',22),('Emil',25),('Linus',28)]



# ==========================================================
# EXAMPLE 10: SORT STRINGS BY LENGTH
# ==========================================================

"""
Normally

sorted(words)

↓

Alphabetical order

But

key=len

or

key=lambda x : len(x)

Sorts according to length.
"""

words = [

    "apple",

    "pie",

    "banana",

    "cherry"

]

sorted_words = sorted(
    words,
    key=lambda x: len(x)
)

# Uncomment to test
# print(sorted_words)

# Output
# ['pie', 'apple', 'banana', 'cherry']



# ==========================================================
# NORMAL FUNCTION vs LAMBDA
# ==========================================================

"""
Normal Function

def square(x):
    return x * x

Lambda

lambda x : x * x

Both produce the same result.

Use Normal Function when:

✔ Function is long
✔ Multiple statements are needed
✔ Loops are required
✔ Better readability is important

Use Lambda when:

✔ Function is very small
✔ Used only once
✔ Passed into another function
✔ Working with map(), filter(), sorted()
"""



# ==========================================================
# LIMITATIONS OF LAMBDA
# ==========================================================

"""
A lambda function can have:

✔ Multiple arguments

Example

lambda a,b,c : a+b+c

--------------------------------------------------

A lambda function CANNOT contain:

❌ Multiple expressions

Wrong

lambda x:
    print(x)
    return x

--------------------------------------------------

❌ Loops

❌ Multiple return statements

❌ Complex logic

For these cases,
use a normal function.
"""



# ==========================================================
# SUMMARY
# ==========================================================

"""
Lambda Function Hierarchy

Lambda Functions
│
├── Anonymous Function
│
├── One Expression Only
│
├── Any Number of Arguments
│
├── Automatically Returns Value
│
├── Function Factory
│      │
│      ├── Return Lambda
│      ├── mydoubler
│      └── mytripler
│
├── Built-in Functions
│      │
│      ├── map()
│      ├── filter()
│      └── sorted()
│
└── Best Used For
       │
       ├── Small Functions
       ├── Temporary Functions
       ├── Short Calculations
       └── Functional Programming


Quick Memory Trick

Normal Function
---------------
Many lines
Has a name

Lambda
-------
One line
No name

Remember:

lambda arguments : expression

Everything after the colon (:) is evaluated,
and its result is automatically returned.
"""