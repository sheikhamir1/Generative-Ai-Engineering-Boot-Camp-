"""
=========================================
            PYTHON BOOLEANS
=========================================

Booleans represent one of two values:

1. True
2. False

Boolean values are used for:

✔ Conditions
✔ Comparisons
✔ Decision Making
✔ Loops
✔ Functions

=========================================
PART 1: BOOLEAN VALUES
=========================================

When Python evaluates a condition,
it returns either:

True
or
False

=========================================
COMPARISON EXAMPLES
=========================================
"""

# print(10 > 9)
# # Output: True

# print(10 == 9)
# # Output: False

# print(10 < 9)
# # Output: False


"""
Explanation:

10 > 9   → True
10 == 9  → False
10 < 9   → False

Comparisons always return a Boolean value.

=========================================
COMMON COMPARISON OPERATORS
=========================================

>    Greater Than
<    Less Than
==   Equal To
!=   Not Equal To
>=   Greater Than or Equal To
<=   Less Than or Equal To

=========================================
PART 2: BOOLEANS IN IF STATEMENTS
=========================================
"""

a = 200
b = 33

if b > a:
    pass
    # print("b is greater than a")
else:
    pass
    # print("b is not greater than a")

"""
Output:

b is not greater than a

Explanation:

33 > 200

False

Therefore the else block runs.

=========================================
PART 3: THE bool() FUNCTION
=========================================

The bool() function converts a value
into either True or False.

Syntax:

bool(value)

=========================================
EXAMPLE
=========================================
"""

# print(bool("Hello"))
# Output: True

# print(bool(15))
# Output: True


"""
Explanation:

"Hello" contains text → True

15 is non-zero → True

=========================================
PART 4: EVALUATING VARIABLES
=========================================
"""

x = "Hello"
y = 15

# print(bool(x))
# Output: True

# print(bool(y))
# Output: True


"""
Explanation:

x contains text
y contains a non-zero number

Therefore both evaluate to True.

=========================================
PART 5: MOST VALUES ARE TRUE
=========================================

In Python, almost everything is True
if it contains some data.

=========================================
STRINGS
=========================================
"""

# print(bool("abc"))
# Output: True

# print(bool("Python"))
# Output: True


"""
=========================================
NUMBERS
=========================================
"""

# print(bool(123))
# # Output: True

# print(bool(-50))
# # Output: True

# print(bool(3.14))
# Output: True


"""
=========================================
LISTS
=========================================
"""

# print(bool(["apple", "banana", "cherry"]))
# Output: True


"""
=========================================
TUPLES
=========================================
"""

# print(bool(("apple", "banana")))
# Output: True


"""
=========================================
SETS
=========================================
"""

# print(bool({"apple", "banana"}))
# Output: True


"""
=========================================
DICTIONARIES
=========================================
"""

# print(bool({"name": "Rohan"}))
# Output: True


"""
=========================================
RULE
=========================================

If a value contains data,
it is usually True.

=========================================
PART 6: VALUES THAT ARE FALSE
=========================================

Python considers some values False.

These are called Falsy Values.

=========================================
BOOLEAN FALSE
=========================================
"""

# print(bool(False))
# Output: False


"""
=========================================
NONE
=========================================
"""

# print(bool(None))
# Output: False


"""
=========================================
ZERO
=========================================
"""

# print(bool(0))
# Output: False

# print(bool(0.0))
# Output: False


"""
=========================================
EMPTY STRING
=========================================
"""

# print(bool(""))
# Output: False


"""
=========================================
EMPTY TUPLE
=========================================
"""

# print(bool(()))
# Output: False


"""
=========================================
EMPTY LIST
=========================================
"""

# print(bool([]))
# Output: False


"""
=========================================
EMPTY SET
=========================================
"""

# print(bool(set()))
# Output: False


"""
=========================================
EMPTY DICTIONARY
=========================================
"""

# print(bool({}))
# Output: False


"""
=========================================
SUMMARY OF FALSY VALUES
=========================================

False
None
0
0.0
""
[]
()
{}
set()

All evaluate to False.

=========================================
PART 7: CUSTOM OBJECTS
=========================================

Objects can control their Boolean value
using the __len__() method.

If __len__() returns 0,
the object becomes False.

=========================================
EXAMPLE
=========================================
"""


class MyClass:

    def __len__(self):
        return 0


myobj = MyClass()

# print(bool(myobj))
# Output: False


"""
Explanation:

__len__() returns 0

Python interprets this object as False.

=========================================
PART 8: FUNCTIONS RETURNING BOOLEANS
=========================================

Functions can return:

True
or
False

=========================================
EXAMPLE
=========================================
"""


def my_function():
    return True


# print(my_function())
# Output: True


"""
Explanation:

The function explicitly returns True.

=========================================
PART 9: USING BOOLEAN FUNCTIONS
=========================================
"""


def is_logged_in():
    return True


if is_logged_in():
    pass
    # print("YES!")
else:
    pass
    # print("NO!")


"""
Output:

YES!

Explanation:

Function returns True,
so the if block executes.

=========================================
PART 10: isinstance()
=========================================

isinstance() checks whether an object
belongs to a specific data type.

Syntax:

isinstance(object, datatype)

Returns:

True
or
False

=========================================
EXAMPLE
=========================================
"""

x = 200

# print(isinstance(x, int))
# Output: True


"""
More Examples:
"""

# print(isinstance("Hello", str))
# Output: True

# print(isinstance(3.14, float))
# Output: True

# print(isinstance([1, 2, 3], list))
# Output: True

# print(isinstance(100, str))
# Output: False


"""
=========================================
REAL-WORLD BOOLEAN EXAMPLES
=========================================
"""


age = 20

# print(age >= 18)
# Output: True


temperature = 45

# print(temperature > 30)
# Output: True


password = "python123"

# print(bool(password))
# Output: True


shopping_cart = []

# print(bool(shopping_cart))
# Output: False


"""
=========================================
KNOWLEDGE HIERARCHY
=========================================

Python
│
├── Data Types
│   ├── int
│   ├── float
│   ├── str
│   ├── list
│   ├── tuple
│   ├── dict
│   └── bool
│
├── Comparisons
│   ├── >
│   ├── <
│   ├── ==
│   ├── !=
│   ├── >=
│   └── <=
│
├── Boolean Logic
│   ├── True
│   ├── False
│   ├── bool()
│   └── isinstance()
│
└── Decision Making
    ├── if
    ├── elif
    └── else

=========================================
REAL-WORLD APPLICATIONS
=========================================

Booleans are used in:

✔ Login Systems
✔ Authentication
✔ Form Validation
✔ Access Control
✔ Shopping Carts
✔ Search Filters
✔ AI Applications
✔ Web Development

Examples:

isLoggedIn → True / False
isAdmin → True / False
hasPermission → True / False
isEmailVerified → True / False

=========================================
QUICK REVISION
=========================================

bool(value)
    ↓
Converts value to True/False

Non-empty String
    ↓
True

Non-zero Number
    ↓
True

Empty String ""
    ↓
False

Zero (0)
    ↓
False

Empty List []
    ↓
False

Empty Dictionary {}
    ↓
False

None
    ↓
False

isinstance()
    ↓
Checks Data Type

=========================================
END OF FILE
=========================================
"""

# ---------------------------------------------------------------------------------------------------

"""
=========================================
            PYTHON OPERATORS
=========================================

Operators are special symbols used to
perform operations on variables and values.

Examples:

+
-
*
/
%
**
//

Operators are one of the most important
concepts in Python because they allow us
to perform calculations and manipulate data.

=========================================
PART 1: WHAT ARE OPERATORS?
=========================================

Operators perform actions on operands.

Example:

10 + 5

Operator:
+

Operands:
10 and 5

Result:
15

=========================================
BASIC EXAMPLE
=========================================
"""

# print(10 + 5)
# Output: 15


"""
=========================================
OPERATORS WITH VARIABLES
=========================================
"""

sum1 = 100 + 50      # 150
sum2 = sum1 + 250    # 400
sum3 = sum2 + sum2   # 800

# print(sum1)
# Output: 150

# print(sum2)
# Output: 400

# print(sum3)
# Output: 800


"""
Explanation:

sum1 = 100 + 50
     = 150

sum2 = 150 + 250
     = 400

sum3 = 400 + 400
     = 800

=========================================
PART 2: ARITHMETIC OPERATORS
=========================================

Arithmetic operators perform mathematical
calculations.

=========================================
LIST OF ARITHMETIC OPERATORS
=========================================

+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus
**  Exponentiation
//  Floor Division

=========================================
PART 3: ADDITION (+)
=========================================
"""

x = 15
y = 4

# print(x + y)
# Output: 19


"""
Explanation:

15 + 4
= 19

=========================================
PART 4: SUBTRACTION (-)
=========================================
"""

# print(x - y)
# Output: 11


"""
Explanation:

15 - 4
= 11

=========================================
PART 5: MULTIPLICATION (*)
=========================================
"""

# print(x * y)
# Output: 60


"""
Explanation:

15 × 4
= 60

=========================================
PART 6: DIVISION (/)
=========================================
"""

# print(x / y)
# Output: 3.75

# print(10/2)

"""
Explanation:

15 ÷ 4
= 3.75

IMPORTANT:

Division always returns a FLOAT.

Even when the answer looks like a whole number.

Example:
"""

# print(10 / 2)
# Output: 5.0


"""
Notice:

Result is 5.0

Not 5

=========================================
PART 7: MODULUS (%)
=========================================

Modulus returns the remainder after division.

Syntax:

x % y

=========================================
"""

# print(x % y)
# Output: 3


"""
Explanation:

15 ÷ 4

Quotient = 3
Remainder = 3

Therefore:

15 % 4
= 3

=========================================
REAL-WORLD USE OF MODULUS
=========================================

Check if a number is even:

"""

number = 10

# print(number % 2)
# Output: 0

"""
If remainder = 0

Number is even.

=========================================
PART 8: EXPONENTIATION (**)
=========================================

Exponentiation means power.

Syntax:

base ** exponent

=========================================
"""

# print(x ** y)
# Output: 50625


"""
Explanation:

15 ** 4

= 15 × 15 × 15 × 15

= 50625

More Examples:
"""

# print(2 ** 3)
# Output: 8

# print(5 ** 2)
# Output: 25


"""
=========================================
PART 9: FLOOR DIVISION (//)
=========================================

Floor Division returns the whole number
part only.

It always rounds DOWN.

Syntax:

x // y

=========================================
"""

# print(x // y)
# Output: 3


"""
Explanation:

15 ÷ 4

= 3.75

Floor Division removes decimal part.

Result:

3

=========================================
PART 10: DIVISION VS FLOOR DIVISION
=========================================
"""

a = 12
b = 5

# print(a / b)
# Output: 2.4

# print(a // b)
# Output: 2


"""
Comparison:

12 / 5
= 2.4

12 // 5
= 2

=========================================
IMPORTANT RULE
=========================================

/   → Returns Float

//  → Returns Integer

=========================================
MORE EXAMPLES
=========================================
"""

# print(20 / 4)
# Output: 5.0

# print(20 // 4)
# Output: 5

# print(25 / 4)
# Output: 6.25

# print(25 // 4)
# Output: 6


"""
=========================================
NEGATIVE NUMBER EXAMPLES
=========================================

Floor Division always rounds DOWN,
not toward zero.

=========================================
"""

# print(-7 // 2)
# Output: -4

"""
Explanation:

-7 / 2

= -3.5

Rounded DOWN:

= -4

This surprises many beginners.

=========================================
PART 11: OPERATOR PRECEDENCE
=========================================

Python follows mathematical order.

Priority:

1. ()
2. **
3. * / // %
4. + -

=========================================
EXAMPLE
=========================================
"""

# print(10 + 5 * 2)
# Output: 20

"""
Explanation:

5 * 2 = 10

10 + 10 = 20

=========================================
USING PARENTHESES
=========================================
"""

# print((10 + 5) * 2)
# Output: 30

"""
Explanation:

10 + 5 = 15

15 * 2 = 30

=========================================
REAL-WORLD APPLICATIONS
=========================================
"""

price = 100
quantity = 5

total = price * quantity

# print(total)
# Output: 500


"""
Area of Rectangle
"""

length = 10
width = 5

area = length * width

# print(area)
# Output: 50


"""
Simple Interest Example
"""

principal = 1000
rate = 5

interest = principal * rate / 100

# print(interest)
# Output: 50.0


"""
=========================================
KNOWLEDGE HIERARCHY
=========================================

Python
│
├── Variables
│
├── Data Types
│   ├── int
│   ├── float
│   └── bool
│
├── Operators
│   ├── Arithmetic Operators
│   │   ├── +
│   │   ├── -
│   │   ├── *
│   │   ├── /
│   │   ├── %
│   │   ├── **
│   │   └── //
│   │
│   ├── Comparison Operators
│   ├── Logical Operators
│   └── Assignment Operators
│
└── Expressions

=========================================
REAL-WORLD APPLICATIONS
=========================================

Arithmetic Operators are used in:

✔ Banking Systems
✔ E-Commerce Websites
✔ AI Models
✔ Data Science
✔ Scientific Calculations
✔ Accounting Software
✔ Games
✔ School Management Systems

=========================================
QUICK REVISION TABLE
=========================================

Operator    Name             Example
----------------------------------------
+           Addition         10 + 5
-           Subtraction      10 - 5
*           Multiplication   10 * 5
/           Division         10 / 5
%           Modulus          10 % 5
**          Exponent         10 ** 5
//          Floor Division   10 // 5

=========================================
EXPECTED OUTPUTS
=========================================

15 + 4     = 19
15 - 4     = 11
15 * 4     = 60
15 / 4     = 3.75
15 % 4     = 3
15 ** 4    = 50625
15 // 4    = 3

"""
# --------------------------------------------------------------------------------------------

"""
=========================================
      PYTHON ASSIGNMENT OPERATORS
=========================================

Assignment operators are used to assign
values to variables.

They help write shorter and cleaner code.

Instead of writing:

x = x + 3

we can write:

x += 3

Both produce the same result.

=========================================
PART 1: BASIC ASSIGNMENT (=)
=========================================

The = operator assigns a value to a variable.

Syntax:

variable = value

=========================================
EXAMPLE
=========================================
"""

x = 5

# print(x)
# Output: 5


"""
Explanation:

x now stores the value 5.

=========================================
PART 2: ADDITION ASSIGNMENT (+=)
=========================================

Syntax:

x += 3

Same As:

x = x + 3

=========================================
"""

x = 5

x += 3

# print(x)
# Output: 8


"""
Step-by-Step:

x = 5

x += 3

x = 5 + 3

x = 8

=========================================
PART 3: SUBTRACTION ASSIGNMENT (-=)
=========================================

Syntax:

x -= 3

Same As:

x = x - 3

=========================================
"""

x = 10

x -= 3

# print(x)
# Output: 7


"""
Step-by-Step:

10 - 3 = 7

=========================================
PART 4: MULTIPLICATION ASSIGNMENT (*=)
=========================================

Syntax:

x *= 3

Same As:

x = x * 3

=========================================
"""

x = 5

x *= 3

# print(x)
# Output: 15


"""
Step-by-Step:

5 × 3 = 15

=========================================
PART 5: DIVISION ASSIGNMENT (/=)
=========================================

Syntax:

x /= 3

Same As:

x = x / 3

=========================================
"""

x = 15

x /= 3

# print(x)
# Output: 5.0


"""
IMPORTANT:

Division always returns a float.

=========================================
PART 6: MODULUS ASSIGNMENT (%=)
=========================================

Syntax:

x %= 3

Same As:

x = x % 3

Returns the remainder.

=========================================
"""

x = 10

x %= 3

# print(x)
# Output: 1


"""
Explanation:

10 % 3

Remainder = 1

=========================================
PART 7: FLOOR DIVISION ASSIGNMENT (//=)
=========================================

Syntax:

x //= 3

Same As:

x = x // 3

=========================================
"""

x = 10

x //= 3

# print(x)
# Output: 3


"""
Explanation:

10 // 3

= 3

=========================================
PART 8: EXPONENT ASSIGNMENT (**=)
=========================================

Syntax:

x **= 3

Same As:

x = x ** 3

=========================================
"""

x = 2

x **= 3

# print(x)
# Output: 8


"""
Explanation:

2³

= 8

=========================================
PART 9: BITWISE AND ASSIGNMENT (&=)
=========================================

Syntax:

x &= 3

Same As:

x = x & 3

Bitwise operators work at the binary level.

=========================================
"""

x = 5

x &= 3

# print(x)
# Output: 1


"""
Binary Representation:

5 = 101
3 = 011

AND
--------
    001

Result = 1

=========================================
PART 10: BITWISE OR ASSIGNMENT (|=)
=========================================

Syntax:

x |= 3

Same As:

x = x | 3

=========================================
"""

x = 5

x |= 3

# print(x)
# Output: 7


"""
Binary:

5 = 101
3 = 011

OR
--------
    111

Result = 7

=========================================
PART 11: BITWISE XOR ASSIGNMENT (^=)
=========================================

Syntax:

x ^= 3

Same As:

x = x ^ 3

=========================================
"""

x = 5

x ^= 3

# print(x)
# Output: 6


"""
Binary:

5 = 101
3 = 011

XOR
--------
    110

Result = 6

=========================================
PART 12: RIGHT SHIFT ASSIGNMENT (>>=)
=========================================

Syntax:

x >>= 3

Same As:

x = x >> 3

Moves bits to the right.

=========================================
"""

x = 16

x >>= 2

# print(x)
# Output: 4


"""
Binary:

16 = 10000

Shift Right by 2

10000 → 01000 → 00100

Result = 4

=========================================
PART 13: LEFT SHIFT ASSIGNMENT (<<=)
=========================================

Syntax:

x <<= 3

Same As:

x = x << 3

Moves bits to the left.

=========================================
"""

x = 4

x <<= 2

# print(x)
# Output: 16


"""
Binary:

4 = 00100

Shift Left by 2

00100 → 01000 → 10000

Result = 16

=========================================
PART 14: WALRUS OPERATOR (:=)
=========================================

Introduced In:

Python 3.8

Nickname:

Walrus Operator

Symbol:

:=

Purpose:

Assign a value and use it in the same
expression.

=========================================
BASIC EXAMPLE
=========================================
"""

# print(x := 3)

# print(x)

"""
Output:

3
3

Explanation:

Assigns 3 to x
and immediately prints it.

Equivalent To:

x = 3
print(x)

=========================================
PART 15: WALRUS OPERATOR WITH IF
=========================================
"""

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    pass
    # print(f"List has {count} elements")

"""
Output:

List has 5 elements

Explanation:

Step 1:

count = len(numbers)

count = 5

Step 2:

5 > 3

True

Step 3:

if block runs

=========================================
WITHOUT WALRUS OPERATOR
=========================================
"""

numbers = [1, 2, 3, 4, 5]

count = len(numbers)

if count > 3:
    pass
    # print(f"List has {count} elements")


"""
Same Result.

Walrus Operator simply makes the code shorter.

=========================================
WHEN TO USE WALRUS OPERATOR
=========================================

Useful For:

✔ Loops
✔ Conditions
✔ Input Processing
✔ Data Validation

Avoid overusing it because it can
reduce readability.

=========================================
REAL-WORLD EXAMPLE
=========================================
"""

user_input = "Python"

if (length := len(user_input)) > 5:
    pass
    # print(f"Input contains {length} characters")


"""
Output:

Input contains 6 characters

=========================================
SUMMARY TABLE
=========================================

Operator     Meaning
-----------------------------------
=            Assignment
+=           Add and Assign
-=           Subtract and Assign
*=           Multiply and Assign
/=           Divide and Assign
%=           Modulus and Assign
//=          Floor Divide and Assign
**=          Power and Assign
&=           Bitwise AND and Assign
|=           Bitwise OR and Assign
^=           Bitwise XOR and Assign
>>=          Right Shift and Assign
<<=          Left Shift and Assign
:=           Walrus Operator

=========================================
KNOWLEDGE HIERARCHY
=========================================

Python
│
├── Variables
│
├── Operators
│   ├── Arithmetic Operators
│   ├── Assignment Operators
│   ├── Comparison Operators
│   ├── Logical Operators
│   └── Bitwise Operators
│
└── Expressions

=========================================
MOST IMPORTANT ASSIGNMENT OPERATORS
=========================================

Focus on these first:

=
+=
-=
*=
/=
%=
**=
:=

These are used daily in Python.

Bitwise assignment operators are
important later for advanced topics.

=========================================
REAL-WORLD APPLICATIONS
=========================================

Assignment operators are used in:

✔ Counters
✔ Score Systems
✔ Banking Applications
✔ AI Models
✔ Data Analysis
✔ Games
✔ Loops
✔ Calculators

Example:

score = 0

score += 10

score += 20

score -= 5

Final Score = 25

=========================================
QUICK REVISION
=========================================

x += 3
↓
x = x + 3

x -= 3
↓
x = x - 3

x *= 3
↓
x = x * 3

x /= 3
↓
x = x / 3

x %= 3
↓
x = x % 3

x **= 3
↓
x = x ** 3

x := 3
↓
Assign and use immediately

"""