"""
==========================================================
                PYTHON range() FUNCTION
==========================================================

WHAT IS range()?
----------------

The built-in range() function creates
a sequence of numbers.

It is most commonly used with

✔ for loops
✔ Iteration
✔ Counting
✔ Indexing

Unlike a list,

range() DOES NOT store all numbers
in memory.

Instead,

it stores only the information needed
to generate the numbers when required.

Because of this,

range() is memory efficient.

==========================================================

WHAT DOES range() RETURN?

It returns a special object called

range

NOT

list

Example

r = range(5)

This does NOT create

[0,1,2,3,4]

Instead,

it creates

range(0,5)

which generates numbers
only when needed.

==========================================================

range() SYNTAX

range(start, stop, step)

All three arguments have meanings:

start
------

Where counting begins.

stop
-----

Where counting stops.

IMPORTANT

The stop value is NEVER included.

This is called

Exclusive Stop.

step
-----

Difference between consecutive numbers.

Default value

1

==========================================================

Quick Memory Trick

range(start, stop, step)

Start

↓

Move by Step

↓

Stop BEFORE Stop
"""



# ==========================================================
# EXAMPLE 1 : range() WITH ONE ARGUMENT
# ==========================================================

"""
Syntax

range(stop)

Only one argument is supplied.

Python assumes

start = 0

step = 1

Example

range(10)

means

Start

0

Stop

10 (NOT INCLUDED)

Numbers produced

0 1 2 3 4 5 6 7 8 9
"""

x = range(10)

# print(x)
# print(type(x))
# Uncomment to test
# print(list(x))

# Output
# [0,1,2,3,4,5,6,7,8,9]



# ==========================================================
# EXAMPLE 2 : range() WITH TWO ARGUMENTS
# ==========================================================

"""
Syntax

range(start, stop)

Example

range(3,10)

Start

3

Stop

10 (NOT INCLUDED)

Output

3 4 5 6 7 8 9
"""

x = range(3, 10)

# Uncomment to test
# print(tuple(x))

# Output
# [3,4,5,6,7,8,9]



# ==========================================================
# EXAMPLE 3 : range() WITH THREE ARGUMENTS
# ==========================================================

"""
Syntax

range(start, stop, step)

Example

range(3,10,2)

Start

3

Step

2

Numbers

3

↓

5

↓

7

↓

9

Next would be 11

Stop because it exceeds 10.
"""

x = range(3, 10, 2)

# Uncomment to test
# print(list(x))

# Output
# [3,5,7,9]



# ==========================================================
# UNDERSTANDING THE STEP VALUE
# ==========================================================

"""
step

determines how much to move
after every number.

Example

range(0,10,1)

↓

0 1 2 3 4 5 6 7 8 9

----------------------------

range(0,10,2)

↓

0 2 4 6 8

----------------------------

range(0,10,3)

↓

0 3 6 9
"""



# ==========================================================
# EXAMPLE 4 : USING range() IN A for LOOP
# ==========================================================

"""
range()

is most commonly used
inside loops.

Example

for i in range(5)

Flow

0

↓

1

↓

2

↓

3

↓

4
"""

# Uncomment to test
for i in range(5):
    # print(i)
    pass

# Output
# 0
# 1
# 2
# 3
# 4



# ==========================================================
# WHY IS THE STOP VALUE EXCLUDED?
# ==========================================================

"""
Python follows

Start Inclusive

Stop Exclusive

Meaning

Start

Included

Stop

Excluded

Example

range(2,6)

Produces

2

3

4

5

NOT

6

This rule makes slicing
and indexing much easier.
"""



# ==========================================================
# EXAMPLE 5 : CONVERTING range TO A LIST
# ==========================================================

"""
A range object

does not directly display
all numbers.

To see every value,

convert it into a list.
"""

# Uncomment to test
# print(list(range(5)))

# Output
# [0,1,2,3,4]


# Uncomment to test
# print(list(range(1,6)))

# Output
# [1,2,3,4,5]


# Uncomment to test
# print(list(range(5,20,3)))

# Output
# [5,8,11,14,17]



# ==========================================================
# EXAMPLE 6 : ACCESSING INDIVIDUAL ELEMENTS
# ==========================================================

"""
A range object supports indexing.

Example

range(10)

↓

0 1 2 3 4 5 6 7 8 9

Index

0 1 2 3 4 5 6 7 8 9

Index 2

↓

2
"""

r = range(10)

# Uncomment to test
# print(r[2])

# Output
# 2



# ==========================================================
# EXAMPLE 7 : SLICING A RANGE
# ==========================================================

"""
Like lists,

ranges support slicing.

Example

range(10)

↓

0 1 2 3 4 5 6 7 8 9

Slice

[:3]

means

Take first three elements.

Important

Result is

another range object,

NOT a list.
"""

# Uncomment to test
# print(r[:3])

# Output
# range(0,3)

# Uncomment to test
# print(list(r[:3]))

# Output
# [0,1,2]



# ==========================================================
# EXAMPLE 8 : MEMBERSHIP TESTING
# ==========================================================

"""
The

in

operator checks whether
a value exists inside
the range.

Example

range(0,10,2)

Numbers

0

2

4

6

8
"""

r = range(0, 10, 2)

# Uncomment to test
# print(6 in r)

# Output
# True


# Uncomment to test
# print(7 in r)

# Output
# False



# ==========================================================
# EXAMPLE 9 : LENGTH OF A RANGE
# ==========================================================

"""
len()

returns

the total number
of elements
inside the range.

Example

range(0,10,2)

Numbers

0

2

4

6

8

Total

5
"""

r = range(0, 10, 2)

# Uncomment to test
# print(len(r))

# Output
# 5



# ==========================================================
# NEGATIVE STEP
# ==========================================================

"""
range()

can also count backwards.

Example

range(10,0,-1)

Start

10

Step

-1

Output

10

9

8

7

6

5

4

3

2

1

Notice

0

is NOT included
because stop is exclusive.
"""

# Uncomment to test
# print(list(range(10,0,-1)))

# Output
# [10,9,8,7,6,5,4,3,2,1]



# ==========================================================
# COUNTING BACKWARDS BY 2
# ==========================================================

"""
Example

range(20,0,-2)

Output

20

18

16

14

12

10

8

6

4

2
"""

# Uncomment to test
# print(list(range(20,0,-2)))



# ==========================================================
# LIST vs RANGE
# ==========================================================

"""
List

numbers = [0,1,2,3,4]

✔ Stores all values
✔ Uses more memory

-----------------------------------

Range

numbers = range(5)

✔ Stores only

start

stop

step

✔ Generates values when needed

✔ Uses much less memory
"""



# ==========================================================
# WHEN SHOULD YOU USE range()?
# ==========================================================

"""
Use range()

✔ Counting

✔ Loops

✔ Index-based iteration

✔ Creating sequences

✔ Repeating actions

✔ Reverse counting

✔ Mathematical patterns

Example

Print

Hello

10 times

for i in range(10):
    print("Hello")
"""



# ==========================================================
# COMMON MISTAKES
# ==========================================================

"""
Mistake 1

Expecting stop value
to be included.

Wrong

range(5)

Output

0 1 2 3 4

NOT

5

--------------------------------------

Mistake 2

Using step = 0

Wrong

range(1,10,0)

Python raises

ValueError

because step cannot be zero.

--------------------------------------

Mistake 3

Wrong direction

range(1,10,-1)

Produces

Nothing

because

start < stop

but

step is negative.

--------------------------------------

Mistake 4

Printing range directly.

Example

print(range(5))

Output

range(0,5)

To see values,

use

list(range(5))
"""



# ==========================================================
# SUMMARY
# ==========================================================

"""
range()
│
├── Built-in Function
│
├── Returns range Object
│
├── Immutable
│
├── Memory Efficient
│
├── Syntax
│      │
│      ├── range(stop)
│      ├── range(start, stop)
│      └── range(start, stop, step)
│
├── Supports
│      │
│      ├── Indexing
│      ├── Slicing
│      ├── Membership (in)
│      ├── len()
│      └── for Loops
│
├── Positive Step
│
├── Negative Step
│
└── Common Uses
       │
       ├── Counting
       ├── Looping
       ├── Repetition
       ├── Reverse Counting
       └── Index Traversal


Quick Memory Trick

range(start, stop, step)

Example

range(2,10,2)

Start

2

↓

Move

+2

↓

Stop BEFORE

10

Output

2

4

6

8

Remember

✅ Start is INCLUDED

❌ Stop is EXCLUDED
"""

# ----------------------------------------------------------------------------------------------

"""
==========================================================
                PYTHON ITERATORS
==========================================================

WHAT IS AN ITERATOR?
--------------------

An Iterator is an object that allows you
to access one value at a time.

Instead of giving all values together,

it provides them

ONE BY ONE.

Think of an iterator like a TV remote.

You press the

Next

button

↓

You get the next channel.

Press again

↓

Next channel.

Press again

↓

Next channel.

You never receive all channels
at once.

==========================================================

WHAT IS AN ITERABLE?
--------------------

An Iterable is any object that can be
iterated (looped) over.

Examples of Iterables

✔ List

✔ Tuple

✔ String

✔ Dictionary

✔ Set

These objects are NOT iterators.

Instead,

they can CREATE iterators.

==========================================================

ITERABLE vs ITERATOR

Iterable

↓

Can create an iterator

Examples

List
Tuple
String
Dictionary
Set

------------------------------------

Iterator

↓

Actually produces values
one at a time.

Uses

next()

==========================================================

THE ITERATOR PROTOCOL

Every iterator must implement
two special methods.

__iter__()

Returns the iterator object itself.

------------------------------------

__next__()

Returns the next value.

If there are no more values,

raises

StopIteration

==========================================================
"""



# ==========================================================
# EXAMPLE 1 : ITERATOR FROM A TUPLE
# ==========================================================

"""
Tuples are iterable.

To get an iterator,

use

iter()

Flow

Tuple

↓

iter()

↓

Iterator

↓

next()

↓

One value at a time.
"""

mytuple = ("apple", "banana", "cherry")

# Create an iterator from the tuple
# myit = iter(mytuple)
# print(myit)

# Uncomment to test
# print(next(myit))
# print(next(myit))
# print(next(myit))


# Output
# apple
# banana
# cherry



# ==========================================================
# WHAT HAPPENS INTERNALLY?
# ==========================================================

"""
Tuple

("apple","banana","cherry")

↓

iter()

↓

Iterator Created

↓

next()

↓

apple

↓

next()

↓

banana

↓

next()

↓

cherry

↓

next()

↓

StopIteration
"""



# ==========================================================
# EXAMPLE 2 : ITERATOR FROM A STRING
# ==========================================================

"""
Strings are also iterable.

Each character
can be accessed
one by one.
"""

mystr = "banana"

myit = iter(mystr)

# Uncomment to test
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# Output
# b
# a
# n
# a
# n
# a



# ==========================================================
# EXAMPLE 3 : USING A for LOOP
# ==========================================================

"""
Instead of calling

next()

manually,

Python usually uses

for

loops.

Example

for fruit in tuple

Python automatically

creates an iterator

and repeatedly calls

next()

until iteration ends.
"""

mytuple = ("apple", "banana", "cherry")

# Uncomment to test
for fruit in mytuple:
    # print(fruit)
    pass

# Output
# apple
# banana
# cherry



# ==========================================================
# EXAMPLE 4 : LOOPING THROUGH A STRING
# ==========================================================

"""
Exactly the same process
works for strings.
"""

mystr = "banana"

# Uncomment to test
# for letter in mystr:
#     print(letter)

# Output
# b
# a
# n
# a
# n
# a



# ==========================================================
# WHAT DOES A for LOOP REALLY DO?
# ==========================================================

"""
This code

for x in mytuple:
    print(x)

is approximately equivalent to

it = iter(mytuple)

while True:

    try:

        value = next(it)

        print(value)

    except StopIteration:

        break

Python hides all this
for convenience.
"""



# ==========================================================
# CREATING YOUR OWN ITERATOR
# ==========================================================

"""
You can make your own iterator
using a class.

To do this,

implement

__iter__()

and

__next__()

methods.
"""



# ==========================================================
# EXAMPLE 5 : SIMPLE CUSTOM ITERATOR
# ==========================================================

"""
Goal

Generate

1

2

3

4

5

...

forever.
"""


class MyNumbers:

    # ---------------------------------
    # Called when iterator is created.
    # ---------------------------------
    def __iter__(self):

        # Starting value
        self.a = 1

        # Return iterator object
        return self

    # ---------------------------------
    # Called every time next() is used.
    # ---------------------------------
    def __next__(self):

        # Store current value
        x = self.a

        # Increase value
        self.a += 1

        # Return current value
        return x


myclass = MyNumbers()

myiter = iter(myclass)

# Uncomment to test
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# Output
# 1
# 2
# 3
# 4
# 5



# ==========================================================
# HOW DOES THIS ITERATOR WORK?
# ==========================================================

"""
Create Object

↓

__iter__()

↓

a = 1

↓

next()

↓

Return 1

↓

Increase a

↓

next()

↓

Return 2

↓

Increase a

↓

next()

↓

Return 3

...

It never stops.

This is called

an Infinite Iterator.
"""



# ==========================================================
# WHY IS THIS A PROBLEM?
# ==========================================================

"""
Since

__next__()

never stops,

the iterator can continue forever.

Example

for x in myiter:

would run forever.

To stop iteration,

Python provides

StopIteration.
"""



# ==========================================================
# EXAMPLE 6 : StopIteration
# ==========================================================

"""
Stop after

20

numbers.
"""


class MyNumbers:

    def __iter__(self):

        self.a = 1

        return self

    def __next__(self):

        # Base condition

        if self.a <= 20:

            x = self.a

            self.a += 1

            return x

        else:

            # Tell Python
            # iteration has finished.
            raise StopIteration


myclass = MyNumbers()

myiter = iter(myclass)

# Uncomment to test
# for number in myiter:
#     print(number)

# Output
# 1
# 2
# 3
# ...
# 20



# ==========================================================
# WHAT IS StopIteration?
# ==========================================================

"""
StopIteration

is a special exception.

It tells Python

"There are no more values."

When using

for

loops,

Python automatically catches

StopIteration

and exits the loop.

You usually never see
the exception yourself
inside a for loop.
"""



# ==========================================================
# iter() vs next()
# ==========================================================

"""
iter()

Purpose

Creates an iterator.

Example

numbers = [1,2,3]

it = iter(numbers)

---------------------------------------

next()

Purpose

Gets the next value.

Example

next(it)

↓

1

next(it)

↓

2

next(it)

↓

3

next(it)

↓

StopIteration
"""



# ==========================================================
# ITERABLES vs ITERATORS
# ==========================================================

"""
Iterable

✔ Can create iterator

Examples

List

Tuple

String

Dictionary

Set

Range

---------------------------------------

Iterator

✔ Has __next__()

✔ Produces one value at a time

Examples

Result of

iter(list)

Generator

Custom Iterator
"""



# ==========================================================
# ITERATOR vs GENERATOR
# ==========================================================

"""
Iterator

✔ Usually created using classes

✔ Must implement

__iter__()

and

__next__()

------------------------------------

Generator

✔ Easier to write

✔ Uses

yield

✔ Automatically creates
iterator methods

Generators are actually
special iterators.
"""



# ==========================================================
# WHEN SHOULD YOU CREATE CUSTOM ITERATORS?
# ==========================================================

"""
Custom iterators are useful for

✔ Infinite sequences

✔ Reading files

✔ Streaming data

✔ Custom collections

✔ Data pipelines

✔ Pagination

✔ Database records

✔ Network streams

Whenever values should be
generated gradually.
"""



# ==========================================================
# COMMON MISTAKES
# ==========================================================

"""
Mistake 1

Calling

next()

after iteration ends.

Result

StopIteration

--------------------------------------

Mistake 2

Forgetting

__iter__()

Custom iterator won't work.

--------------------------------------

Mistake 3

Forgetting

return self

inside

__iter__()

Python expects
the iterator object itself.

--------------------------------------

Mistake 4

Never raising

StopIteration

Results in

Infinite Iterator

which never ends.
"""



# ==========================================================
# SUMMARY
# ==========================================================

"""
Python Iterators
│
├── Iterable
│      │
│      ├── List
│      ├── Tuple
│      ├── String
│      ├── Dictionary
│      ├── Set
│      └── Range
│
├── Iterator
│      │
│      ├── iter()
│      ├── next()
│      ├── __iter__()
│      └── __next__()
│
├── Custom Iterator
│      │
│      ├── Class
│      ├── __iter__()
│      ├── __next__()
│      └── StopIteration
│
├── for Loop
│      │
│      └── Automatically calls next()
│
├── Generator
│      │
│      └── Special type of Iterator
│
└── Applications
       │
       ├── File Reading
       ├── Streaming Data
       ├── Infinite Sequences
       ├── Pagination
       └── Lazy Evaluation


Quick Memory Trick

Iterable

↓

Can be LOOPED over.

Examples

List
Tuple
String

----------------------------

Iterator

↓

Can give

ONE VALUE

at a time.

Uses

next()

Remember

iter()

creates an iterator.

next()

moves to the next value.

When no values remain,

Python raises

StopIteration.
"""

# ----------------------------------------------------------------------------------------------------------------

"""
==========================================================
                PYTHON MODULES
==========================================================

WHAT IS A MODULE?
-----------------
A module is simply a Python (.py) file that contains
functions, variables, classes, etc., which can be reused
in other Python programs.

Think of a module as a code library.

==========================================================
CREATE A MODULE
==========================================================

Create a Python file named:

mymodule.py
"""

# File: mymodule.py

# def greeting(name):
#     print("Hello, " + name)


"""
==========================================================
USING A MODULE
==========================================================

Import the module using the import keyword.

Syntax:

import module_name

Access functions using:

module_name.function_name()
"""

# import mymodule

# mymodule.greeting("Jonathan")

# Uncomment to test
# mymodule.greeting("Jonathan")



"""
==========================================================
MODULE VARIABLES
==========================================================

A module can contain variables in addition to functions.

Example:

File: mymodule.py
"""

# person1 = {
#     "name": "John",
#     "age": 36,
#     "country": "Norway"
# }


"""
Import the module and access its variables.
"""

# import mymodule

# a = mymodule.person1["age"]

# Uncomment to test
# print(a)



"""
==========================================================
NAMING A MODULE
==========================================================

A module can have any name,

but it MUST end with

.py

Examples:

math_utils.py

student.py

database.py

calculator.py
"""



"""
==========================================================
RENAMING A MODULE (ALIAS)
==========================================================

Use the 'as' keyword to give a module
a shorter or different name.

Syntax:

import module_name as alias
"""

# import mymodule as mx

# a = mx.person1["age"]

# Uncomment to test
# print(a)



"""
==========================================================
BUILT-IN MODULES
==========================================================

Python already provides many built-in modules.

Example:

platform

Used to get information about the system.
"""

# import platform

# x = platform.system()

# # Uncomment to test
# # print(x)



"""
==========================================================
THE dir() FUNCTION
==========================================================

dir(module_name)

Returns all functions, variables,
and attributes available inside a module.
"""

# import platform

# x = dir(platform)

# Uncomment to test
# print(x)



"""
==========================================================
IMPORT SPECIFIC ITEMS
==========================================================

Instead of importing the entire module,

you can import only the required object.

Syntax:

from module_name import object_name
"""

# File: mymodule.py

# def greeting(name):
#     print("Hello, " + name)

# person1 = {
#     "name": "John",
#     "age": 36,
#     "country": "Norway"
# }


"""
Import only the dictionary.
"""

# from mymodule import person1

# Uncomment to test
# print(person1["age"])



"""
==========================================================
IMPORTANT NOTE
==========================================================

When using:

from mymodule import person1

Use:

person1["age"]

NOT

mymodule.person1["age"]

because only person1 was imported.

==========================================================
SUMMARY
==========================================================

Modules
│
├── Create Module (.py file)
├── import module_name
├── module_name.function()
├── Module Variables
├── import module_name as alias
├── Built-in Modules
├── dir(module_name)
└── from module_name import object
"""