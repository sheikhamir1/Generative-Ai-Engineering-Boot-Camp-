"""
==========================================================
            PYTHON OOP (OBJECT-ORIENTED PROGRAMMING)
==========================================================

WHAT IS OOP?
------------

OOP stands for:

Object-Oriented Programming

It is a programming style that uses

✔ Classes
✔ Objects

to organize and reuse code.

Python is an object-oriented language.

==========================================================
ADVANTAGES OF OOP
==========================================================

✔ Better code organization

✔ Easy to reuse code

✔ Easy to maintain

✔ Easy to debug

✔ Follows the DRY principle

DRY = Don't Repeat Yourself

Avoid writing the same code multiple times.
"""



# ==========================================================
# CLASSES AND OBJECTS
# ==========================================================

"""
A Class is a blueprint.

An Object is created from a class.

Examples

Class        Objects
----------------------------
Fruit    ->  Apple, Banana
Car      ->  Volvo, Audi
Student  ->  Alice, Bob

Objects inherit the properties
and methods of their class.
"""



# ==========================================================
# CREATE A CLASS
# ==========================================================

"""
Use the

class

keyword to create a class.
"""

class MyClass:
    x = 5

class Student:
    name1 = "Rohan"


# ==========================================================
# CREATE AN OBJECT
# ==========================================================

"""
Create an object by
calling the class name.
"""

p1 = MyClass()
s1 = Student()
# print(s1.name1)

# Uncomment to test
# print(p1.x)

# Output
# 5



# ==========================================================
# DELETE AN OBJECT
# ==========================================================

"""
Use

del

to delete an object.
"""

# Uncomment to test
# del p1

# print(p1)

# ==========================================================
# CREATE MULTIPLE OBJECTS
# ==========================================================

"""
You can create multiple objects
from the same class.

Each object is independent.
"""

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

# Uncomment to test
# print(p1.x)

# Uncomment to test
# print(p2.x)

# Uncomment to test
# print(p3.x)



# ==========================================================
# EMPTY CLASS
# ==========================================================

"""
A class cannot be empty.

Use

pass

to create an empty class.
"""

class Person:
    pass



"""
==========================================================
SUMMARY
==========================================================

OOP
│
├── Class
│      └── Blueprint
│
├── Object
│      └── Instance of a Class
│
├── Create Class
│      └── class MyClass:
│
├── Create Object
│      └── obj = MyClass()
│
├── Delete Object
│      └── del obj
│
├── Multiple Objects
│
└── pass
       └── Empty Class
"""

# -----------------------------------------------------------------------------------------------------------------------------

"""
==========================================================
            PYTHON __init__() METHOD
==========================================================

WHAT IS __init__()?
-------------------

__init__() is a special method
that is automatically called
when an object is created.

It is mainly used to:

✔ Initialize object properties
✔ Assign initial values
✔ Perform setup operations

==========================================================
BASIC __init__() METHOD
==========================================================
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Rohan", 26)
p2 = Person("Aliya", 20)
# print(p2.name)

# Uncomment to test
# print(p1.name)

# Uncomment to test
# print(p1.age)



# ==========================================================
# AUTOMATICALLY CALLED
# ==========================================================

"""
The __init__() method is called
automatically whenever
a new object is created.

Example:

p1 = Person("Emil", 36)

No need to call __init__() yourself.
"""



# ==========================================================
# WITHOUT __init__()
# ==========================================================

"""
Without __init__(),

you must assign values manually.
"""

class Person:
    pass


p1 = Person()
# print(p1)

p1.name = "Tobias"
p1.age = 25

# Uncomment to test
# print(p1.name)

# Uncomment to test
# print(p1.age)



# ==========================================================
# WITH __init__()
# ==========================================================

"""
Using __init__()

lets you assign values
while creating the object.
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Linus", 28)

# Uncomment to test
# print(p1.name)

# Uncomment to test
# print(p1.age)



# ==========================================================
# DEFAULT VALUES
# ==========================================================

"""
Parameters can have
default values.
"""

class Person:

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


p1 = Person("Emil")
p2 = Person("Tobias", 25)

# Uncomment to test
# print(p1.name, p1.age)

# Uncomment to test
# print(p2.name, p2.age)



# ==========================================================
# MULTIPLE PARAMETERS
# ==========================================================

"""
The __init__() method can have
multiple parameters.
"""

class Person:

    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country


p1 = Person("Linus", 30, "Oslo", "Norway")

# Uncomment to test
# print(p1.name)

# Uncomment to test
# print(p1.age)

# Uncomment to test
# print(p1.city)

# Uncomment to test
# print(p1.country)



"""
==========================================================
SUMMARY
==========================================================

__init__()
│
├── Special Method
├── Runs Automatically
├── Initializes Objects
├── Assigns Properties
├── Default Parameters
└── Multiple Parameters
"""

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
==========================================================
            PYTHON self PARAMETER
==========================================================

WHAT IS self?
--------------

self is a reference to the
current object (instance)
of a class.

It is used to:

✔ Access object properties
✔ Access object methods

==========================================================
USING self
==========================================================
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)


p1 = Person("Rohan", 25)
# print(p1.name, p1.age)

# Uncomment to test
# p1.greet()



# ==========================================================
# self MUST BE THE FIRST PARAMETER
# ==========================================================

"""
For every instance method,

self must be the first parameter.

Example:

def greet(self):
    ...
"""



# ==========================================================
# WHY USE self?
# ==========================================================

"""
self tells Python

which object's data
should be used.
"""

class Person:

    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)


p1 = Person("Tobias")
p2 = Person("Linus")

# Uncomment to test
# p1.printname()

# Uncomment to test
# p2.printname()



# ==========================================================
# self CAN HAVE A DIFFERENT NAME
# ==========================================================

"""
The name

self

is only a convention.

You can use any name,

but it must be
the first parameter.
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)


p1 = Person("Emil", 36)

# Uncomment to test
# p1.greet()

"""
Note:

Using 'self' is recommended
because it is the Python standard.
"""



# ==========================================================
# ACCESSING MULTIPLE PROPERTIES
# ==========================================================

"""
Use self to access
multiple object properties.
"""

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.me = "Its Me"

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} {self.me}")


car1 = Car("Toyota", "Corolla", 2020)

# Uncomment to test
# car1.display_info()



# ==========================================================
# CALLING METHODS USING self
# ==========================================================

"""
A method can call another
method using self.
"""

class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")


p1 = Person("Aliya")

# Uncomment to test
# p1.welcome()



"""
==========================================================
SUMMARY
==========================================================

self
│
├── Refers to Current Object
├── Access Properties
├── Access Methods
├── First Parameter
├── Can Have Another Name
│      └── (Not Recommended)
├── Access Multiple Properties
└── Call Methods Using self
"""
# -------------------------------------------------------------------------------------------------------------

# ==========================================================
# Python Class Properties
# ==========================================================

# ----------------------------------------------------------
# Class Properties
# ----------------------------------------------------------
# Properties are variables that belong to a class.
# They store data for each object (instance) created from the class.


# ==========================================================
# Example 1: Create a class with properties
# ==========================================================

class Person:
    def __init__(self, name, age):
        # Instance properties
        self.name = name
        self.age = age


# Creating an object
p1 = Person("Emil", 36)

# Uncomment to check manually
# print(p1.name)
# print(p1.age)


# ==========================================================
# Access Properties
# ==========================================================
# You can access object properties using dot notation.


# Example: Access the properties of an object

class Car:
    def __init__(self, brand, model):
        # Instance properties
        self.brand = brand
        self.model = model


# Creating an object
car1 = Car("Toyota", "Corolla")

# Uncomment to check manually
# print(car1.brand)
# print(car1.model)


# ==========================================================
# Modify Properties
# ==========================================================
# You can modify the value of properties on objects.


# Example: Change the age property

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating an object
p1 = Person("Tobias", 25)

# Uncomment to check manually
# print(p1.age)

# Modifying the property
p1.age = 26

# Uncomment to check manually
# print(p1.age)


# ==========================================================
# Delete Properties
# ==========================================================
# You can delete properties from objects using the 'del' keyword.


# Example: Delete the age property

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating an object
p1 = Person("Linus", 30)

# print(p1.name , p1.age)
# Deleting the age property
del p1.age
# print(p1.name , p1.age)

# Uncomment to check manually
# print(p1.name)   # This works

# Uncommenting the line below will cause an AttributeError
# because the 'age' property has been deleted.
# print(p1.age)


# ==========================================================
# Class Properties vs Object (Instance) Properties
# ==========================================================
#
# Instance Properties:
# - Defined inside the __init__() method.
# - Every object gets its own separate copy.
#
# Class Properties:
# - Defined directly inside the class but outside methods.
# - Shared among all objects of that class.


# Example: Class property vs Instance property

class Person:
    # Class property (shared by all objects)
    species = "Human"

    def __init__(self, name):
        # Instance property
        self.name = name


# Creating objects
p1 = Person("Emil")
p2 = Person("Tobias")

# Uncomment to check manually
# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)


# ==========================================================
# Modifying Class Properties
# ==========================================================
# When you modify a class property, the change affects
# all objects that use that class property.


# Example: Change a class property

class Person:
    # Class property
    lastname = ""

    def __init__(self, name):
        self.name = name


# Creating objects
p1 = Person("Linus")
p2 = Person("Emil")

# Changing the class property
Person.lastname = "Refsnes"

# Uncomment to check manually
# print(p1.lastname)
# print(p2.lastname)


# ==========================================================
# Add New Properties
# ==========================================================
# You can add new properties to an existing object
# after it has been created.


# Example: Add a new property to an object

class Person:
    def __init__(self, name):
        self.name = name


# Creating an object
p1 = Person("Tobias")

# Adding new properties
p1.age = 25
p1.city = "Oslo"

# Uncomment to check manually
# print(p1.name)
# print(p1.age)
# print(p1.city)


# ==========================================================
# Note
# ==========================================================
#
# Adding properties this way only adds them to
# that specific object.
#
# Other objects of the same class will NOT have
# these new properties unless they are added separately.
#
# Example:
#
# p2 = Person("Emil")
#
# Uncommenting the line below would cause an AttributeError
# because 'age' was only added to p1.
#
# print(p2.age)
#
# To give every object the same property,
# define it inside __init__() or as a class property.
# ==========================================================


# -------------------------------------------------------------------------------------------------------------

# ==========================================================
# Python Class Methods
# ==========================================================

# ----------------------------------------------------------
# Class Methods
# ----------------------------------------------------------
# Methods are functions that belong to a class.
# They define the behavior (actions) of objects created
# from the class.


# ==========================================================
# Example 1: Create a method in a class
# ==========================================================

class Person:
    def __init__(self, name):
        # Instance property
        self.name = name

    # Instance method
    def greet(self):
        print("Hello, my name is " + self.name)


# Creating an object
p1 = Person("Emil")

# Uncomment to check manually
# p1.greet()


# ==========================================================
# Note
# ==========================================================
#
# Every instance method must have 'self'
# as its first parameter.
#
# 'self' refers to the current object that is
# calling the method.


# ==========================================================
# Methods with Parameters
# ==========================================================
# Methods can accept parameters just like
# normal functions.


# Example: Create methods with parameters

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


# Creating an object
calc = Calculator()

# # Uncomment to check manually
# print(calc.add(5, 3))
# print(calc.multiply(4, 7))


# ==========================================================
# Methods Accessing Properties
# ==========================================================
# Methods can access object properties using 'self'.


# Example: A method that accesses object properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"


# Creating an object
p1 = Person("Tobias", 28)

# Uncomment to check manually
# print(p1.get_info())


# ==========================================================
# Methods Modifying Properties
# ==========================================================
# Methods can modify object properties.


# Example: A method that changes a property value

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        # Increase age by 1
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")


# Creating an object
p1 = Person("Linus", 25)

# Uncomment to check manually
# p1.celebrate_birthday()
# p1.celebrate_birthday()



# ==========================================================
# The __str__() Method
# ==========================================================
#
# __str__() is a special method.
#
# It controls what is returned when an object
# is printed using print().
#
# If __str__() is not defined, Python prints
# the default object representation.


# ==========================================================
# Example: Without the __str__() Method
# ==========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating an object
p1 = Person("Emil", 36)

# Uncomment to check manually
# print(p1)

# Output will look similar to:
# <__main__.Person object at 0x...>


# ==========================================================
# Example: With the __str__() Method
# ==========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


# Creating an object
p1 = Person("Rohan", 26)

# Uncomment to check manually
# print(p1)

# Output:
# Tobias (36)


# ==========================================================
# Multiple Methods
# ==========================================================
# A class can contain multiple methods
# that work together.


# Example: Create multiple methods in a class

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []


    def __str__(self):
        return f"Playlist: {self.name} \nSongs: {self.songs}"

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")
        else:
            print(f"{song} - Dose Not Exist!")


    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")


# Creating an object
my_playlist = Playlist("Favorites")
# print(my_playlist)

# Uncomment to check manually
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.add_song("ABCD")
# my_playlist.show_songs()
# my_playlist.remove_song("Bohemian Rhapsody")
# my_playlist.remove_song("Bohemian Rhapsod")


# ==========================================================
# Delete Methods
# ==========================================================
# You can delete methods from a class
# using the 'del' keyword.


# Example: Delete a method from a class

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!"+ self.name)


# Creating an object
p1 = Person("Emil")
p2 = Person("Rahul")

# def sayHi(name):
#     print(f"Hello {name}")

# p1.sayHi = sayHi
# p1.sayHi("aliya")

# Deleting the greet() method from the class
# del Person.greet
# del p1.sayHi

# Uncomment to check manually
# p1.greet()
# p2.greet()
# p1.sayHi("aliya")

# The above line will cause an AttributeError
# because the greet() method no longer exists
# in the Person class.


# ==========================================================
# Summary
# ==========================================================
#
# ✔ Methods are functions inside a class.
# ✔ Methods define what an object can do.
# ✔ Every instance method must have 'self'
#   as its first parameter.
# ✔ Methods can:
#     - Accept parameters
#     - Access object properties
#     - Modify object properties
#     - Return values
# ✔ __str__() customizes how an object is displayed.
# ✔ A class can have multiple methods.
# ✔ Methods can be removed using the 'del' keyword,
#   but calling a deleted method raises an AttributeError.
# ==========================================================