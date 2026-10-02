"""
==========================================================
                PYTHON RECURSION
==========================================================

WHAT IS RECURSION?
------------------

Recursion is a programming technique where
a function CALLS ITSELF.

Instead of using a loop (for/while),
the function repeatedly solves smaller
versions of the same problem until it
reaches a stopping condition.

Think of recursion like climbing down stairs.

Step 5
 ↓
Step 4
 ↓
Step 3
 ↓
Step 2
 ↓
Step 1
 ↓
Ground Floor (Stop)

Without a stopping point,
the function would continue forever.

==========================================================

EVERY RECURSIVE FUNCTION HAS TWO PARTS

1. Base Case
-------------
The condition that STOPS recursion.

2. Recursive Case
-----------------
The function calling itself with
a smaller or modified input.

Without a Base Case

function()
    ↓
function()
    ↓
function()
    ↓
function()
    ↓
Forever...

Eventually Python runs out of memory
and raises a RecursionError.

==========================================================
"""



# ==========================================================
# EXAMPLE 1: SIMPLE COUNTDOWN
# ==========================================================

"""
Goal

Print numbers from 5 to 1
using recursion.

Flow

countdown(5)

↓

5

↓

countdown(4)

↓

4

↓

countdown(3)

↓

3

↓

countdown(2)

↓

2

↓

countdown(1)

↓

1

↓

countdown(0)

↓

Done!
"""


def countdown(n):

    # -------------------------------
    # BASE CASE
    # -------------------------------
    # Stop when number becomes zero
    if n <= 0:

        print("Done!")

    # -------------------------------
    # RECURSIVE CASE
    # -------------------------------
    else:

        print(n)

        # Function calls itself
        countdown(n - 2)


# Uncomment to test
# countdown(5)



# ==========================================================
# HOW THE FUNCTION CALLS ITSELF
# ==========================================================

"""
Imagine calling:

countdown(3)

Execution

countdown(3)

prints 3

calls countdown(2)

        ↓

prints 2

calls countdown(1)

        ↓

prints 1

calls countdown(0)

        ↓

prints Done!

Then every function finishes
one by one.

This is called

UNWINDING THE RECURSION.
"""



# ==========================================================
# EXAMPLE 2: FACTORIAL
# ==========================================================

"""
Factorial

5!

means

5 × 4 × 3 × 2 × 1

=

120

Recursion is perfect for this because

5!

=

5 × 4!

4!

=

4 × 3!

3!

=

3 × 2!

Eventually

1!

=

1

which becomes our Base Case.
"""


def factorial(n):

    # n = 5  : 1
    # n = 4  : 2
    # n = 3  : 3
    # n = 2  : 4
    # n = 1  : 5

    # -------------------------------
    # BASE CASE
    # -------------------------------
    if n == 0 or n == 1:

        return 1

    # -------------------------------
    # RECURSIVE CASE
    # -------------------------------
    else:

        return n * factorial(n - 1)
        


# Uncomment to test
# print(factorial(5))

# Output
# 120



# ==========================================================
# HOW FACTORIAL WORKS
# ==========================================================

"""
factorial(5)

↓

5 × factorial(4)

↓

5 × 4 × factorial(3)

↓

5 × 4 × 3 × factorial(2)

↓

5 × 4 × 3 × 2 × factorial(1)

↓

5 × 4 × 3 × 2 × 1

↓

120
"""



# ==========================================================
# EXAMPLE 3: FIBONACCI SEQUENCE
# ==========================================================

"""
Fibonacci Sequence

0
1
1
2
3
5
8
13
21
34
...

Rule

Every number

=

Previous Number

+

Number Before That

Example

8

=

5 + 3

13

=

8 + 5
"""


def fibonacci(n):

    # -------------------------------
    # BASE CASE
    # -------------------------------
    if n <= 1:

        return n

    # -------------------------------
    # RECURSIVE CASE
    # -------------------------------
    else:

        return fibonacci(n - 1) + fibonacci(n - 2)
       


# Uncomment to test
# print(fibonacci(7))

# Output
# 13



# ==========================================================
# HOW FIBONACCI WORKS
# ==========================================================

"""
fibonacci(5)

↓

fibonacci(4)
+
fibonacci(3)

↓

Each of those functions
creates TWO MORE function calls.

This is why Fibonacci recursion
becomes very slow for large numbers.

Example

fib(40)

creates millions of recursive calls.
"""



# ==========================================================
# EXAMPLE 4: RECURSION WITH LISTS
# ==========================================================

"""
Goal

Find the sum of every number
inside a list.

Instead of adding everything together,

Recursion does

First Number

+

Sum of Remaining List

Example

[1,2,3,4]

↓

1

+

sum([2,3,4])

↓

2

+

sum([3,4])

↓

3

+

sum([4])

↓

4

+

sum([])

↓

0

(Base Case)
"""


def sum_list(numbers):

    # -------------------------------
    # BASE CASE
    # -------------------------------
    if len(numbers) == 0:

        return 0

    # -------------------------------
    # RECURSIVE CASE
    # -------------------------------
    else:

        return numbers[0] + sum_list(numbers[1:])
        


my_list = [1, 2, 3, 4, 5]

# Uncomment to test
# print(sum_list(my_list))

# Output
# 15



# ==========================================================
# UNDERSTANDING LIST SLICING
# ==========================================================

"""
numbers[0]

means

First element

Example

[10,20,30]

numbers[0]

↓

10

--------------------------------

numbers[1:]

means

Everything except first element

Example

[10,20,30]

↓

[20,30]

Each recursive call makes
the list smaller.

Eventually

[]

Empty List

becomes the Base Case.
"""



# ==========================================================
# EXAMPLE 5: FIND MAXIMUM VALUE
# ==========================================================

"""
Goal

Find the biggest number
inside a list.

Example

[3,7,2,9,1]

↓

Compare first element

with

Maximum of remaining list.
"""


def find_max(numbers):

    # -------------------------------
    # BASE CASE
    # -------------------------------
    if len(numbers) == 1:

        return numbers[0]

    # -------------------------------
    # RECURSIVE CASE
    # -------------------------------
    else:

        # Find largest value
        # in the remaining list
        max_of_rest = find_max(numbers[1:])

        # Compare first value
        # with remaining maximum
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest


my_list = [3, 7, 2, 9, 1]

# Uncomment to test
# print(find_max(my_list))

# Output
# 9



# ==========================================================
# EXAMPLE 6: CHECK RECURSION LIMIT
# ==========================================================

"""
Python prevents infinite recursion.

It has a recursion limit.

Usually

about

1000

recursive calls.

If recursion exceeds this,

Python raises

RecursionError
"""

import sys

# Uncomment to test
# print(sys.getrecursionlimit())

# Example Output
# 1000



# ==========================================================
# EXAMPLE 7: CHANGE RECURSION LIMIT
# ==========================================================

"""
You CAN increase the limit.

But this should be done carefully.

Very deep recursion
can consume large amounts of memory
and may even crash your program.
"""

# Increase recursion limit
# sys.setrecursionlimit(2000)

# Uncomment to test
# print(sys.getrecursionlimit())

# Output
# 2000



# ==========================================================
# WHAT HAPPENS INSIDE MEMORY?
# ==========================================================

"""
Every recursive function call

creates a

STACK FRAME.

Think of a stack like books.

Top
──────────
function(1)
──────────
function(2)
──────────
function(3)
──────────
function(4)
──────────
function(5)
──────────
──────────
function(6)
──────────
──────────
function(7)
──────────
──────────
function(8)
──────────
Bottom

The deeper recursion goes,

the taller the stack becomes.

Once Base Case is reached,

books are removed one by one.

This process is called

CALL STACK UNWINDING.
"""



# ==========================================================
# RECURSION vs ITERATION
# ==========================================================

"""
Recursion

✔ Elegant
✔ Short code
✔ Matches mathematical definitions
✔ Good for trees and graphs

Disadvantages

❌ More memory
❌ Slower
❌ Recursion limit

----------------------------------

Iteration (Loops)

✔ Faster
✔ Uses less memory
✔ No recursion limit

Disadvantages

❌ Sometimes harder to write
"""



# ==========================================================
# WHEN SHOULD YOU USE RECURSION?
# ==========================================================

"""
Recursion is commonly used for

✔ Factorial

✔ Fibonacci

✔ Tree Traversal

✔ Graph Traversal

✔ Binary Search Trees

✔ Divide and Conquer Algorithms

✔ Merge Sort

✔ Quick Sort

✔ Directory/File Traversal

✔ Dynamic Programming Problems
"""



# ==========================================================
# COMMON MISTAKES
# ==========================================================

"""
Mistake 1

No Base Case

Result

Infinite recursion

----------------------------------

Mistake 2

Base Case can never be reached

Example

countdown(n + 1)

instead of

countdown(n - 1)

Result

Infinite recursion

----------------------------------

Mistake 3

Very large recursive depth

Result

RecursionError

----------------------------------

Mistake 4

Using recursion when a loop
would be much simpler.
"""



# ==========================================================
# SUMMARY
# ==========================================================

"""
Recursion Hierarchy

Recursion
│
├── Function Calls Itself
│
├── Base Case
│      │
│      └── Stops Recursion
│
├── Recursive Case
│      │
│      └── Calls Function Again
│
├── Call Stack
│      │
│      ├── Stack Frames
│      └── Unwinding
│
├── Examples
│      │
│      ├── Countdown
│      ├── Factorial
│      ├── Fibonacci
│      ├── Sum List
│      └── Find Maximum
│
├── Recursion Limit
│      │
│      ├── sys.getrecursionlimit()
│      └── sys.setrecursionlimit()
│
└── Applications
       │
       ├── Trees
       ├── Graphs
       ├── Sorting
       ├── Searching
       └── Divide & Conquer


Quick Memory Trick

Every Recursive Function Needs

1️⃣ Base Case
      (Stop)

2️⃣ Recursive Case
      (Call itself)

Without BOTH,
recursion will never work correctly.
"""

# ---------------------------------------------------------------------------------------------------------


"""
==========================================================
                PYTHON GENERATORS
==========================================================

WHAT ARE GENERATORS?
--------------------

A Generator is a special type of function that can:

✔ Pause its execution
✔ Remember its current state
✔ Resume later from where it stopped

Unlike a normal function,
a generator DOES NOT return all values at once.

Instead,

it generates one value at a time.

Because of this,

generators are very memory efficient.

==========================================================

NORMAL FUNCTION

def numbers():
    return [1, 2, 3]

When called,

Entire list is created in memory.

Memory

[1,2,3]

↓

Returned all at once.

==========================================================

GENERATOR FUNCTION

def numbers():
    yield 1
    yield 2
    yield 3

Nothing is generated immediately.

Values are produced

ONE AT A TIME

only when needed.

==========================================================

HOW TO CREATE A GENERATOR?

Simply replace

return

with

yield

If a function contains the keyword

yield

Python automatically treats it
as a Generator Function.

==========================================================
"""



# ==========================================================
# EXAMPLE 1 : SIMPLE GENERATOR
# ==========================================================

"""
Goal

Generate numbers

1

2

3

one at a time.
"""


def my_generator():

    # Pause here and return 1
    yield 1

    # Resume here next time
    yield 2

    # Resume here again
    yield 3


"""
Nothing happens yet!

Calling

my_generator()

DOES NOT execute the function.

Instead,

it creates a Generator Object.
"""

gen = my_generator()
# print(gen)

# Uncomment to test
for value in gen:
    # print(value)
    pass

# Output
# 1
# 2
# 3



# ==========================================================
# WHAT HAPPENS INTERNALLY?
# ==========================================================

"""
Call

gen = my_generator()

↓

Generator object created

↓

No code executed

↓

next(gen)

↓

yield 1

↓

next(gen)

↓

yield 2

↓

next(gen)

↓

yield 3

↓

Generator finished.
"""



# ==========================================================
# EXAMPLE 2 : USING yield
# ==========================================================

"""
yield

is what makes a function
a generator.

Unlike

return

yield DOES NOT end the function.

Instead,

it pauses execution.

Next time,

execution resumes from the same point.
"""


def count_up_to(n):

    count = 1

    while count <= n:

        # Pause and return current number
        yield count

        # This line executes AFTER
        # next() is called again.
        count += 1


# Uncomment to test
for num in count_up_to(5):
    # print(num)
    pass



# gen = count_up_to(5)

# next(gen)

# Output
# 1
# 2
# 3
# 4
# 5



# ==========================================================
# return vs yield
# ==========================================================

"""
return

↓

Returns value

↓

Function Ends

↓

Cannot continue

-----------------------------

yield

↓

Returns value

↓

Function Pauses

↓

Can Resume Later
"""



# ==========================================================
# EXAMPLE 3 : MEMORY EFFICIENCY
# ==========================================================

"""
Suppose we need

1,000,000 numbers.

Using a list

numbers = list(range(1000000))

Python stores ALL numbers
in memory.

Memory

[0,1,2,3,4,...999999]

Huge memory usage.

------------------------------------------------

Generator

Only ONE number exists
at a time.

Memory

0

↓

1

↓

2

↓

3

Much more efficient.
"""


def large_sequence(n):

    for i in range(n):

        yield i


gen = large_sequence(1000000)

# Uncomment to test
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Output
# 0
# 1
# 2



# ==========================================================
# EXAMPLE 4 : next()
# ==========================================================

"""
next()

manually asks
the generator

"Give me the next value."
"""


def simple_gen():

    yield "Emil"

    yield "Tobias"

    yield "Linus"


gen = simple_gen()

# Uncomment to test
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Output
# Emil
# Tobias
# Linus



# ==========================================================
# WHAT HAPPENS AFTER LAST VALUE?
# ==========================================================

"""
Once generator finishes,

calling

next()

again

raises

StopIteration

This tells Python

"There are no more values."
"""


def simple_gen():

    yield 1

    yield 2


gen = simple_gen()

# Uncomment to test
# print(next(gen))
# print(next(gen))
# print(next(gen))   # StopIteration Error



# ==========================================================
# EXAMPLE 5 : GENERATOR EXPRESSIONS
# ==========================================================

"""
Generator Expressions

are similar to

List Comprehensions.

Difference

List

uses

[]

Generator

uses

()
"""



# List Comprehension
list_comp = [x * x for x in range(5)]

# Uncomment to test
# print(list_comp)

# Output
# [0,1,4,9,16]



# Generator Expression

gen_exp = (x * x for x in range(5))

# Uncomment to test
# print(gen_exp)

# Output
# <generator object ...>

# Uncomment to test
# print(list(gen_exp))

# Output
# [0,1,4,9,16]



# ==========================================================
# WHY DOES print(gen_exp) LOOK STRANGE?
# ==========================================================

"""
Generator Expression

does NOT store values.

It stores

instructions

for generating values later.

Only when iterated,

the numbers are created.
"""



# ==========================================================
# EXAMPLE 6 : USING sum() WITH GENERATOR
# ==========================================================

"""
Instead of creating

an entire list

Generator creates values
one by one,

making it memory efficient.
"""

total = sum(x * x for x in range(10))

# Uncomment to test
# print(total)

# Output
# 285



# ==========================================================
# EXAMPLE 7 : FIBONACCI GENERATOR
# ==========================================================

"""
Fibonacci Sequence

0

1

1

2

3

5

8

13

21

...

Instead of storing

all Fibonacci numbers,

generator creates them

one at a time.
"""


def fibonacci():

    a = 0
    b = 1

    while True:

        yield a

        a, b = b, a + b


gen = fibonacci()

# Uncomment to test
# for _ in range(10):
#     print(next(gen))

# Output
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34



# ==========================================================
# WHY while True?
# ==========================================================

"""
The Fibonacci sequence

never ends.

Generator keeps producing values

until

YOU decide to stop.

This is called

an Infinite Generator.
"""



# ==========================================================
# EXAMPLE 8 : send()
# ==========================================================

"""
Normally

Generator

only sends values OUT.

send()

allows us to

send values

INTO

the generator.
"""


def echo_generator():

    while True:

        received = yield

        print("Received:", received)


gen = echo_generator()

"""
Before using send(),

generator must reach
its first yield.

This is called

Priming the Generator.
"""

# Uncomment to test
# next(gen)

# # Uncomment to test
# gen.send("Hello")
# gen.send("World")

# Output
# Received: Hello
# Received: World



# ==========================================================
# WHY PRIME THE GENERATOR?
# ==========================================================

"""
Generator starts

BEFORE

the first yield.

Python needs to reach

yield

before it can receive data.

Therefore

next(gen)

must be called once.
"""



# ==========================================================
# EXAMPLE 9 : close()
# ==========================================================

"""
close()

immediately stops
the generator.

Useful when

generator is no longer needed.
"""


def my_gen():

    try:

        yield 1

        yield 2

        yield 3

    finally:

        print("Generator closed")


gen = my_gen()

# Uncomment to test
# print(next(gen))
# print(next(gen))

# Uncomment to test
# gen.close()

# Output
# 1
# Generator closed



# ==========================================================
# NORMAL FUNCTION vs GENERATOR
# ==========================================================

"""
Normal Function

return

↓

Entire result returned

↓

Function ends

↓

More memory usage

--------------------------------

Generator

yield

↓

One value at a time

↓

Function pauses

↓

Less memory usage
"""



# ==========================================================
# WHEN SHOULD YOU USE GENERATORS?
# ==========================================================

"""
Generators are perfect for

✔ Reading huge files

✔ Processing millions of records

✔ Infinite sequences

✔ Streaming data

✔ Large database queries

✔ Pipelines

✔ Machine Learning datasets

✔ Log processing

✔ Web scraping

✔ Lazy evaluation

Whenever you DON'T want
everything loaded into memory.
"""



# ==========================================================
# COMMON MISTAKES
# ==========================================================

"""
Mistake 1

Expecting generator
to run immediately.

Wrong

gen = my_generator()

Nothing happens.

Need

next()

or

for loop.

-------------------------------------

Mistake 2

Trying to reuse
an exhausted generator.

Once finished,

generator cannot restart.

Create a NEW generator.

-------------------------------------

Mistake 3

Calling

next()

after generator ends.

Result

StopIteration

-------------------------------------

Mistake 4

Using generators for
very small datasets.

Lists are often simpler.
"""



# ==========================================================
# SUMMARY
# ==========================================================

"""
Generators
│
├── Special Functions
│
├── Use yield
│
├── Pause Execution
│
├── Resume Later
│
├── Generator Object
│
├── next()
│      │
│      └── Get Next Value
│
├── yield
│      │
│      └── Pause Function
│
├── send()
│      │
│      └── Send Value Into Generator
│
├── close()
│      │
│      └── Stop Generator
│
├── Generator Expression
│      │
│      └── ( )
│
├── Infinite Generators
│      │
│      └── while True
│
└── Advantages
       │
       ├── Memory Efficient
       ├── Faster for Large Data
       ├── Lazy Evaluation
       └── One Value at a Time


Quick Memory Trick

Normal Function

return

↓

Ends Function

----------------------------

Generator

yield

↓

Pause Function

↓

Resume Later

Think of a generator like a Netflix episode.

▶ Press Play → Runs

⏸ Pause → yield

▶ Play Again → Continues

It DOES NOT start from the beginning;
it resumes exactly where it paused.
"""