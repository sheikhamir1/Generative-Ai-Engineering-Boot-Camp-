"""
==========================================================
                PYTHON DATETIME MODULE
==========================================================

WHAT IS datetime?
-----------------

Python does not have a separate built-in Date data type.

To work with dates and times,
Python provides the built-in

datetime

module.

It allows you to work with:

✔ Current Date
✔ Current Time
✔ Year
✔ Month
✔ Day
✔ Hour
✔ Minute
✔ Second
✔ Microsecond

==========================================================
GET CURRENT DATE AND TIME
==========================================================
"""

import datetime

# Get the current date and time
x = datetime.datetime.now()

# Uncomment to test
# print(x)



"""
==========================================================
DATE OUTPUT
==========================================================

datetime.now() returns a datetime object.

Example Output

2026-07-28 22:14:54.654618

This contains:

Year
Month
Day
Hour
Minute
Second
Microsecond
"""



"""
==========================================================
ACCESSING DATE INFORMATION
==========================================================

You can access different parts
of the datetime object.
"""

import datetime

x = datetime.datetime.now()

# Get the current year

# Uncomment to test
# print(x.minute)

# Get the weekday name

# Uncomment to test
# print(x.strftime("%A"))



"""
==========================================================
CREATING A DATE OBJECT
==========================================================

Use the datetime() constructor.

Syntax:

datetime.datetime(year, month, day)
"""

import datetime

x = datetime.datetime(2020, 5, 17)

# Uncomment to test
# print(x)



"""
==========================================================
OPTIONAL TIME PARAMETERS
==========================================================

The datetime() constructor can also accept:

hour
minute
second
microsecond
timezone

Example:

datetime.datetime(
    2020,
    5,
    17,
    10,
    30,
    15
)
"""



"""
==========================================================
strftime() METHOD
==========================================================

strftime()

Formats a datetime object into
a readable string.

Syntax:

date.strftime(format_code)
"""

import datetime

x = datetime.datetime(2018, 6, 1)

# Display full month name

# Uncomment to test
# print(x)


# print(x.strftime("%A"))

"""
==========================================================
COMMON strftime() FORMAT CODES
==========================================================

Date Formats

%a  -> Weekday (Short)         Example: Wed

%A  -> Weekday (Full)          Example: Wednesday

%w  -> Weekday Number          Example: 3

%d  -> Day of Month            Example: 31

%b  -> Month (Short)           Example: Dec

%B  -> Month (Full)            Example: December

%m  -> Month Number            Example: 12

%y  -> Year (2 Digits)         Example: 18

%Y  -> Year (4 Digits)         Example: 2018

----------------------------------------------------------

Time Formats

%H  -> Hour (24-Hour)

%I  -> Hour (12-Hour)

%p  -> AM / PM

%M  -> Minute

%S  -> Second

%f  -> Microsecond

----------------------------------------------------------

Timezone Formats

%z  -> UTC Offset

%Z  -> Timezone Name

----------------------------------------------------------

Other Formats

%j  -> Day of Year

%U  -> Week Number (Sunday First)

%W  -> Week Number (Monday First)

%c  -> Local Date and Time

%x  -> Local Date

%X  -> Local Time

%%  -> Percent Symbol (%)

%G  -> ISO Year

%u  -> ISO Weekday

%V  -> ISO Week Number
"""



"""
==========================================================
EXAMPLE FORMAT CODES
==========================================================
"""

import datetime

x = datetime.datetime.now()

# Full Year

# Uncomment to test
# print(x.strftime("%c"))

# Month Name

# Uncomment to test
# print(x.strftime("%B"))

# Day of Month

# Uncomment to test
# print(x.strftime("%d"))

# Weekday Name

# Uncomment to test
# print(x.strftime("%A"))

# Hour (24-Hour Format)

# Uncomment to test
# print(x.strftime("%H"))

# Minute

# Uncomment to test
# print(x.strftime("%M"))

# Second

# Uncomment to test
# print(x.strftime("%S"))



"""
==========================================================
SUMMARY
==========================================================

datetime Module
│
├── datetime.now()
├── datetime(year, month, day)
├── Current Date & Time
├── Access Date Parts
│      ├── year
│      ├── month
│      ├── day
│      ├── hour
│      ├── minute
│      └── second
└── strftime()
       ├── %Y -> Year
       ├── %B -> Month
       ├── %d -> Day
       ├── %A -> Weekday
       ├── %H -> Hour
       ├── %M -> Minute
       └── %S -> Second
"""

# ----------------------------------------------------------------------------------------------------------------

"""
==========================================================
                PYTHON MATH
==========================================================

WHAT IS THE math MODULE?
------------------------

Python provides:

1. Built-in Math Functions
2. The math Module

The built-in functions are available directly.

The math module provides additional
mathematical functions and constants.

==========================================================
BUILT-IN MATH FUNCTIONS
==========================================================
"""



# ==========================================================
# min() FUNCTION
# ==========================================================

"""
min()

Returns the smallest value.
"""

x = min(5, 10, 25)

# Uncomment to test
# print(x)

# Output
# 5



# ==========================================================
# max() FUNCTION
# ==========================================================

"""
max()

Returns the largest value.
"""

y = max(5, 10, 25)

# Uncomment to test
# print(y)

# Output
# 25



# ==========================================================
# abs() FUNCTION
# ==========================================================

"""
abs()

Returns the absolute (positive) value
of a number.
"""

x = abs(-7.25)

# Uncomment to test
# print(x)

# Output
# 7.25



# ==========================================================
# pow() FUNCTION
# ==========================================================

"""
pow(x, y)

Returns:

x raised to the power of y.

Example:

pow(4, 3)

means

4 × 4 × 4
"""

x = pow(4, 3)

# Uncomment to test
# print(x)

# Output
# 64



"""
==========================================================
THE math MODULE
==========================================================

To use the math module,

first import it.
"""

import math



# ==========================================================
# math.sqrt()
# ==========================================================

"""
math.sqrt()

Returns the square root
of a number.
"""

x = math.sqrt(81)

# Uncomment to test
# print(x)

# Output
# 8.0



# ==========================================================
# math.ceil()
# ==========================================================

"""
math.ceil()

Rounds a number UP
to the nearest integer.
"""

x = math.ceil(1.1)

# Uncomment to test
# print(x)

# Output
# 2



# ==========================================================
# math.floor()
# ==========================================================

"""
math.floor()

Rounds a number DOWN
to the nearest integer.
"""

y = math.floor(1.9)

# Uncomment to test
# print(y)

# Output
# 1



# ==========================================================
# math.pi
# ==========================================================

"""
math.pi

Returns the value of π (Pi).

Approximate value:

3.141592653589793
"""

x = math.pi

# Uncomment to test
# print(x)



"""
==========================================================
SUMMARY
==========================================================

Built-in Functions
│
├── min()
├── max()
├── abs()
└── pow()

math Module
│
├── math.sqrt()
├── math.ceil()
├── math.floor()
└── math.pi
"""

# ------------------------------------------------------------------------------------------------------------

"""
==========================================================
                PYTHON JSON
==========================================================

WHAT IS JSON?
-------------

JSON stands for:

JavaScript Object Notation

It is a text format used for:

✔ Storing data
✔ Exchanging data
✔ Sending data between applications

Python provides the built-in

json

module to work with JSON data.

==========================================================
IMPORT THE JSON MODULE
==========================================================
"""

import json



# ==========================================================
# PARSE JSON (JSON → PYTHON)
# ==========================================================

"""
json.loads()

Converts a JSON string
into a Python object.

Usually,
a JSON object becomes a Python dictionary.
"""

# JSON string
x = '{ "name":"John", "age":30, "city":"New York"}'

dummy =  [{"id":1,"name":"Leanne Graham","username":"Bret","email":"Sincere@april.biz","address":{"street":"Kulas Light","suite":"Apt. 556","city":"Gwenborough","zipcode":"92998-3874","geo":{"lat":"-37.3159","lng":"81.1496"}},"phone":"1-770-736-8031 x56442","website":"hildegard.org","company":{"name":"Romaguera-Crona","catchPhrase":"Multi-layered client-server neural-net","bs":"harness real-time e-markets"}},{"id":2,"name":"Ervin Howell","username":"Antonette","email":"Shanna@melissa.tv","address":{"street":"Victor Plains","suite":"Suite 879","city":"Wisokyburgh","zipcode":"90566-7771","geo":{"lat":"-43.9509","lng":"-34.4618"}},"phone":"010-692-6593 x09125","website":"anastasia.net","company":{"name":"Deckow-Crist","catchPhrase":"Proactive didactic contingency","bs":"synergize scalable supply-chains"}},{"id":3,"name":"Clementine Bauch","username":"Samantha","email":"Nathan@yesenia.net","address":{"street":"Douglas Extension","suite":"Suite 847","city":"McKenziehaven","zipcode":"59590-4157","geo":{"lat":"-68.6102","lng":"-47.0653"}},"phone":"1-463-123-4447","website":"ramiro.info","company":{"name":"Romaguera-Jacobson","catchPhrase":"Face to face bifurcated interface","bs":"e-enable strategic applications"}},{"id":4,"name":"Patricia Lebsack","username":"Karianne","email":"Julianne.OConner@kory.org","address":{"street":"Hoeger Mall","suite":"Apt. 692","city":"South Elvis","zipcode":"53919-4257","geo":{"lat":"29.4572","lng":"-164.2990"}},"phone":"493-170-9623 x156","website":"kale.biz","company":{"name":"Robel-Corkery","catchPhrase":"Multi-tiered zero tolerance productivity","bs":"transition cutting-edge web services"}},{"id":5,"name":"Chelsey Dietrich","username":"Kamren","email":"Lucio_Hettinger@annie.ca","address":{"street":"Skiles Walks","suite":"Suite 351","city":"Roscoeview","zipcode":"33263","geo":{"lat":"-31.8129","lng":"62.5342"}},"phone":"(254)954-1289","website":"demarco.info","company":{"name":"Keebler LLC","catchPhrase":"User-centric fault-tolerant solution","bs":"revolutionize end-to-end systems"}},{"id":6,"name":"Mrs. Dennis Schulist","username":"Leopoldo_Corkery","email":"Karley_Dach@jasper.info","address":{"street":"Norberto Crossing","suite":"Apt. 950","city":"South Christy","zipcode":"23505-1337","geo":{"lat":"-71.4197","lng":"71.7478"}},"phone":"1-477-935-8478 x6430","website":"ola.org","company":{"name":"Considine-Lockman","catchPhrase":"Synchronised bottom-line interface","bs":"e-enable innovative applications"}},{"id":7,"name":"Kurtis Weissnat","username":"Elwyn.Skiles","email":"Telly.Hoeger@billy.biz","address":{"street":"Rex Trail","suite":"Suite 280","city":"Howemouth","zipcode":"58804-1099","geo":{"lat":"24.8918","lng":"21.8984"}},"phone":"210.067.6132","website":"elvis.io","company":{"name":"Johns Group","catchPhrase":"Configurable multimedia task-force","bs":"generate enterprise e-tailers"}},{"id":8,"name":"Nicholas Runolfsdottir V","username":"Maxime_Nienow","email":"Sherwood@rosamond.me","address":{"street":"Ellsworth Summit","suite":"Suite 729","city":"Aliyaview","zipcode":"45169","geo":{"lat":"-14.3990","lng":"-120.7677"}},"phone":"586.493.6943 x140","website":"jacynthe.com","company":{"name":"Abernathy Group","catchPhrase":"Implemented secondary concept","bs":"e-enable extensible e-tailers"}},{"id":9,"name":"Glenna Reichert","username":"Delphine","email":"Chaim_McDermott@dana.io","address":{"street":"Dayna Park","suite":"Suite 449","city":"Bartholomebury","zipcode":"76495-3109","geo":{"lat":"24.6463","lng":"-168.8889"}},"phone":"(775)976-6794 x41206","website":"conrad.com","company":{"name":"Yost and Sons","catchPhrase":"Switchable contextually-based project","bs":"aggregate real-time technologies"}},{"id":10,"name":"Clementina DuBuque","username":"Moriah.Stanton","email":"Rey.Padberg@karina.biz","address":{"street":"Kattie Turnpike","suite":"Suite 198","city":"Lebsackbury","zipcode":"31428-2261","geo":{"lat":"-38.2386","lng":"57.2232"}},"phone":"024-648-3804","website":"ambrose.net","company":{"name":"Hoeger LLC","catchPhrase":"Centralized empowering task-force","bs":"target end-to-end models"}}]


# print(dummy)


# my_json = json.dumps(dummy, indent=2)
# # print(my_json)

# load_my_json = json.loads(my_json)
# print(load_my_json)


# Convert JSON to Python dictionary
# y = json.loads(dummy)

# print(y)
# Uncomment to test
# print(y["age"])

# Output
# 30



# ==========================================================
# CONVERT PYTHON TO JSON
# ==========================================================

"""
json.dumps()

Converts a Python object
into a JSON string.
"""

# Python dictionary
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert to JSON
y = json.dumps(x)

# Uncomment to test
# print(type(y))

# Output
# {"name": "John", "age": 30, "city": "New York"}



# ==========================================================
# PYTHON OBJECTS SUPPORTED BY JSON
# ==========================================================

"""
json.dumps() can convert:

✔ dict
✔ list
✔ tuple
✔ string
✔ int
✔ float
✔ True
✔ False
✔ None
"""

# Uncomment to test
# print(json.dumps({"name": "John", "age": 30}))

# Uncomment to test
# print(json.dumps(["apple", "banana"]))

# Uncomment to test
# print(json.dumps(("apple", "banana")))

# Uncomment to test
# print(json.dumps("hello"))

# Uncomment to test
# print(json.dumps(42))

# Uncomment to test
# print(json.dumps(31.76))

# Uncomment to test
# print(json.dumps(True))

# Uncomment to test
# print(json.dumps(False))

# Uncomment to test
# print(json.dumps(None))



# ==========================================================
# PYTHON TO JSON TYPE CONVERSION
# ==========================================================

"""
Python          JSON
--------------------------
dict      ->    Object
list      ->    Array
tuple     ->    Array
str       ->    String
int       ->    Number
float     ->    Number
True      ->    true
False     ->    false
None      ->    null
"""



# ==========================================================
# COMPLEX PYTHON OBJECT
# ==========================================================

"""
A Python object can contain
multiple data types.
"""

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Uncomment to test
# print(json.dumps(x))



# ==========================================================
# FORMAT JSON OUTPUT
# ==========================================================

"""
Use the

indent

parameter to make JSON
more readable.
"""

# Uncomment to test
# print(json.dumps(x, indent=2))



# ==========================================================
# CUSTOM SEPARATORS
# ==========================================================

"""
Use the

separators

parameter to change
the default separators.

Default:

(", ", ": ")
"""

# Uncomment to test
# print(json.dumps(x, indent=3, separators=(". ", " = ")))



# ==========================================================
# SORT JSON KEYS
# ==========================================================

"""
Use

sort_keys=True

to sort dictionary keys
alphabetically.
"""

# Uncomment to test
# print(json.dumps(x, indent=2, sort_keys=True))



"""
==========================================================
SUMMARY
==========================================================

JSON
│
├── import json
├── json.loads()    # JSON → Python
├── json.dumps()    # Python → JSON
├── Supported Types
│      ├── dict
│      ├── list
│      ├── tuple
│      ├── string
│      ├── int
│      ├── float
│      ├── bool
│      └── None
├── indent
├── separators
└── sort_keys
"""