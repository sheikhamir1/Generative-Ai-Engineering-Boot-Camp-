# ==========================================================
# Python Inheritance
# ==========================================================

# ----------------------------------------------------------
# What is Inheritance?
# ----------------------------------------------------------
#
# Inheritance allows one class to reuse the properties
# and methods of another class.
#
# Instead of writing the same code again and again,
# we create a parent class and let child classes
# inherit its features.
#
# Parent Class
#   ↓
# Child Class
#
# The child class automatically gets everything
# from the parent class unless it overrides them.
#
#
# Terminology
# --------------------
# Parent Class
#     Also called:
#     - Base Class
#     - Super Class
#
# Child Class
#     Also called:
#     - Derived Class
#     - Sub Class


# ==========================================================
# Example 1: Create a Parent Class
# ==========================================================

class Person:
    def __init__(self, fname, lname):
        # Instance properties
        self.firstname = fname
        self.lastname = lname

    # Instance method
    def printname(self):
        print(self.firstname, self.lastname)


# Creating an object of Person
x = Person("John", "Doe")

# Uncomment to check manually
# x.printname()


# ==========================================================
# Create a Child Class
# ==========================================================
#
# Syntax:
#
# class ChildClass(ParentClass):
#     pass
#
# By writing ParentClass inside parentheses,
# the child automatically inherits everything
# from the parent.


# Example

class Student(Person):
    pass


# Creating an object
x = Student("Mike", "Olsen")

# Uncomment to check manually
# x.printname()


# ==========================================================
# What does "pass" mean?
# ==========================================================
#
# "pass" is a placeholder.
#
# It tells Python:
#
# "Don't add anything right now."
#
# Since Student has no code of its own,
# it simply inherits everything from Person.


# ==========================================================
# Add the __init__() Function
# ==========================================================
#
# Sometimes the child class needs its own constructor.
#
# If we write our own __init__(),
# Python DOES NOT automatically call
# the parent's __init__().
#
# This is one of the most confusing parts
# for beginners.


# Example

class Student(Person):

    def __init__(self, fname, lname):
        # Child constructor
        pass


# ----------------------------------------------------------
# Important Concept
# ----------------------------------------------------------
#
# Once the child has its own __init__(),
# the parent's __init__() is NOT executed.
#
# That means:
#
# self.firstname
# self.lastname
#
# are never created unless we call
# the parent's constructor manually.


# ==========================================================
# Calling the Parent Constructor
# ==========================================================

class Student(Person):

    def __init__(self, fname, lname):

        # Call Parent constructor
        Person.__init__(self, fname, lname)


# Creating an object
x = Student("Mike", "Olsen")

# Uncomment to check manually
# x.printname()


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Why do we write:
#
# Person.__init__(self, fname, lname)
#
# instead of
#
# self.__init__(...)
#
#
# Because:
#
# self.__init__()
#
# would call Student's constructor AGAIN,
# creating an infinite loop.
#
# We specifically want to execute the
# constructor of the PARENT class.
#
# Therefore we call:
#
# Person.__init__(...)
#
#
# Memory Flow
#
# Student()
#      │
#      ▼
# Student.__init__()
#      │
#      ▼
# Person.__init__()
#      │
#      ▼
# firstname created
# lastname created


# ==========================================================
# Using super()
# ==========================================================
#
# Python provides an easier way.
#
# Instead of writing:
#
# Person.__init__(...)
#
# we simply write:
#
# super().__init__(...)
#
#
# super() automatically refers to
# the parent class.


# Example

class Student(Person):

    def __init__(self, fname, lname):

        # Calls Person.__init__()
        super().__init__(fname, lname)


# Creating an object
x = Student("Mike", "Olsen")

# Uncomment to check manually
# x.printname()


# ==========================================================
# Difficult Concept:
# Why use super()?
# ==========================================================
#
# Old way:
#
# Person.__init__(self, ...)
#
# Modern Python:
#
# super().__init__(...)
#
#
# Advantages of super():
#
# ✔ Cleaner code
#
# ✔ If the parent class name changes,
#   you don't need to update every child.
#
# ✔ Works correctly in multiple inheritance
#   (very important in advanced Python).
#
#
# Today you can remember:
#
# super() == "Call my parent."


# ==========================================================
# Add Properties
# ==========================================================
#
# Child classes can have their own properties
# in addition to inherited ones.


# Example

class Student(Person):

    def __init__(self, fname, lname):

        super().__init__(fname, lname)

        # New property
        self.graduationyear = 2019


# Creating an object
x = Student("Rohan", "Ali")

# Uncomment to check manually
# print(x.firstname)
# print(x.lastname)
# print(x.graduationyear)


# ==========================================================
# Passing Property as a Parameter
# ==========================================================
#
# Instead of always using 2019,
# let the user choose the graduation year.


# Example

class Student(Person):

    def __init__(self, fname, lname, year):

        super().__init__(fname, lname)

        self.graduationyear = year


# Creating an object
x = Student("Aliya", "Olsen", 2020)

# Uncomment to check manually
# print(x.firstname)
# print(x.lastname)
# print(x.graduationyear)


# ==========================================================
# Add Methods
# ==========================================================
#
# Child classes can also have their own methods.


# Example

class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)


        self.graduationyear = year

    def welcome(self):

        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduationyear,
        )


# Creating an object
x = Student("Mike", "Olsen", 2019)

# Uncomment to check manually
# x.welcome()


# ==========================================================
# Method Overriding
# ==========================================================
#
# A child class can replace (override)
# a method inherited from the parent.
#
# This is called:
#
# Method Overriding


# Example

class Person:

    def speak(self):
        print("I am a person.")


class Student(Person):

    # Overrides Person.speak()
    def speak(self):
        print("I am a student.")
    pass


x = Student()

# Uncomment to check manually
# x.speak()


# ==========================================================
# Difficult Concept Explained:
# Method Overriding
# ==========================================================
#
# Parent Class
#
# speak()
#      ↓
# "I am a person."
#
#
# Child Class
#
# speak()
#      ↓
# "I am a student."
#
#
# Since Student has its own speak(),
# Python ignores the parent's version.
#
#
# Search Order
#
# Student Object
#      │
#      ▼
# Does Student have speak()?
#      │
#    Yes
#      │
#      ▼
# Execute Student.speak()
#
# Parent's speak() is ignored.


# ==========================================================
# Parent Method + Child Method Together
# ==========================================================
#
# Sometimes we don't want to replace
# the parent's method.
#
# We want BOTH:
#
# Parent method
# +
# Child method
#
# We can use super().


# Example

class Person:

    def speak(self):
        print("I am a person.")


class Student(Person):

    def speak(self):

        # Call parent method first
        super().speak()
        print("I am also a student.")



x = Student()

# Uncomment to check manually
# x.speak()

#
# Output:
#
# I am a person.
# I am also a student.


# ==========================================================
# Real-Life Analogy
# ==========================================================
#
# Person
#
# Properties:
#     firstname
#     lastname
#
# Methods:
#     printname()
#
#
# Student
#
# Inherits:
#     firstname
#     lastname
#     printname()
#
# Adds:
#     graduationyear
#     welcome()
#
#
# So Student gets everything from Person
# PLUS its own features.


# ==========================================================
# Summary
# ==========================================================
#
# ✔ Inheritance lets one class reuse another class.
#
# ✔ Parent Class
#      ↓
#   Child Class
#
# ✔ Child inherits:
#     - Properties
#     - Methods
#
# ✔ pass means "do nothing."
#
# ✔ If child defines __init__(),
#   parent __init__() is NOT called automatically.
#
# ✔ Call parent constructor using:
#
#       Person.__init__(...)
#
#   or preferably:
#
#       super().__init__(...)
#
# ✔ Child classes can add:
#     - New properties
#     - New methods
#
# ✔ Child methods can override
#   parent methods.
#
# ✔ super() can also call
#   parent methods after overriding.
#
# ==========================================================

# ------------------------------------------------------------------------------------------------

# ==========================================================
# Python Polymorphism
# ==========================================================

# ----------------------------------------------------------
# What is Polymorphism?
# ----------------------------------------------------------
#
# The word "Polymorphism" comes from:
#
# Poly  = Many
# Morph = Forms
#
# Meaning:
#
# "One interface, many forms."
#
# In Python, polymorphism means the SAME method,
# function, or operator can behave differently
# depending on the object it is used with.
#
# In simple words:
#
# Same Name
#      ↓
# Different Behavior
#
#
# Example:
#
# move()
#
# Car     -> Drive
# Boat    -> Sail
# Plane   -> Fly
#
# Same method name.
# Different outputs.


# ==========================================================
# Function Polymorphism
# ==========================================================
#
# Some Python functions work with many different
# types of objects.
#
# One of the best examples is:
#
# len()
#
# It works on strings, lists, tuples,
# dictionaries, and many other objects.


# ==========================================================
# Example 1: len() with String
# ==========================================================

x = "Hello World!"

# Uncomment to check manually
# print(len(x))

# Output:
# 12

#
# len() returns the number of characters
# in the string.
#


# ==========================================================
# Example 2: len() with Tuple
# ==========================================================

mytuple = ("apple", "banana", "cherry")

# Uncomment to check manually
# print(len(mytuple))

# Output:
# 3

#
# len() returns the number of items
# inside the tuple.
#


# ==========================================================
# Example 3: len() with Dictionary
# ==========================================================

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}

# Uncomment to check manually
# print(len(thisdict))

# Output:
# 3

#
# len() returns the number of key-value pairs.
#


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Wait...
#
# How can ONE function work for
# completely different objects?
#
#
# Python internally checks the object type.
#
#
# len("Hello")
#
# Python knows it is a string
# and counts characters.
#
#
# len((1,2,3))
#
# Python knows it is a tuple
# and counts elements.
#
#
# len({"a":1})
#
# Python knows it is a dictionary
# and counts keys.
#
#
# SAME function.
#
# DIFFERENT behavior.
#
# That is polymorphism.


# ==========================================================
# Class Polymorphism
# ==========================================================
#
# Different classes can have methods
# with the SAME name.
#
# Each class decides what that method does.
#
#
# Example:
#
# move()
#
# Car
# Boat
# Plane
#
# Every class has move(),
# but every class behaves differently.


# ==========================================================
# Example: Different Classes with Same Method
# ==========================================================

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


# Creating objects
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")


# Same loop...
# Same method...
# Different behavior.

# Uncomment to check manually
#
# for x in (car1, boat1, plane1):
#     x.move()


# Output:
#
# Drive!
# Sail!
# Fly!


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Why does this work?
#
# We never asked:
#
# if object is Car:
#     ...
#
# if object is Boat:
#     ...
#
# if object is Plane:
#     ...
#
#
# Instead we simply wrote:
#
# x.move()
#
#
# Python automatically calls
# the correct move() method
# depending on the object's type.
#
#
# Loop
#   │
#   ▼
# Car Object
#   │
#   ▼
# Car.move()
#
#
# Boat Object
#   │
#   ▼
# Boat.move()
#
#
# Plane Object
#   │
#   ▼
# Plane.move()


# ==========================================================
# Inheritance + Polymorphism
# ==========================================================
#
# Polymorphism becomes even more useful
# when inheritance is involved.
#
# We create one parent class
# and multiple child classes.


# ==========================================================
# Example: Parent Class
# ==========================================================

class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


# ==========================================================
# Child Classes
# ==========================================================

class Car(Vehicle):
    # Inherits everything from Vehicle
    pass


class Boat(Vehicle):

    # Override move()
    def move(self):
        print("Sail!")


class Plane(Vehicle):

    # Override move()
    def move(self):
        print("Fly!")


# Creating objects
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")


# Uncomment to check manually
#
# for x in (car1, boat1, plane1):

#     print(x.brand)
#     print(x.model)

#     x.move()
#     print()


# Output:
#
# Ford
# Mustang
# Move!
#
# Ibiza
# Touring 20
# Sail!
#
# Boeing
# 747
# Fly!


# ==========================================================
# Why does Car print "Move!"?
# ==========================================================
#
# Car does NOT have its own move().
#
# Python searches like this:
#
# Car Object
#      │
#      ▼
# Does Car have move()?
#      │
#     No
#      │
#      ▼
# Look inside Vehicle
#      │
#      ▼
# Found move()
#      │
#      ▼
# Execute Vehicle.move()
#
#
# Therefore:
#
# Car -> Move!


# ==========================================================
# Why do Boat and Plane behave differently?
# ==========================================================
#
# Boat has its own move().
#
# So Python stops searching.
#
#
# Boat Object
#      │
#      ▼
# Boat.move() exists?
#      │
#     Yes
#      ▼
# Execute Boat.move()
#
#
# Parent method is ignored.
#
#
# Same happens for Plane.


# ==========================================================
# Method Overriding
# ==========================================================
#
# Child class method
#
# replaces
#
# Parent class method.
#
# This is called:
#
# Method Overriding.


# ==========================================================
# Real-Life Analogy
# ==========================================================
#
# Imagine a remote control.
#
# It has one button:
#
# START
#
#
# Car
# -----
# START
# ↓
# Engine starts.
#
#
# Boat
# -----
# START
# ↓
# Boat engine starts.
#
#
# Plane
# -----
# START
# ↓
# Aircraft engines start.
#
#
# Same button.
#
# Different machines.
#
# Different behavior.
#
# This is exactly what
# polymorphism means.


# ==========================================================
# Difference Between Inheritance and Polymorphism
# ==========================================================
#
# Inheritance
# -------------------------
#
# Purpose:
# Reuse code.
#
#
# Parent
#      ↓
# Child
#
#
# Example:
#
# Student inherits Person.
#
#
#
# Polymorphism
# -------------------------
#
# Purpose:
# Same method name,
# different behavior.
#
#
# move()
#
# Car
# Boat
# Plane
#
#
# Inheritance is about
# "getting features."
#
# Polymorphism is about
# "using the same interface
# with different behavior."


# ==========================================================
# Summary
# ==========================================================
#
# ✔ Polymorphism means "many forms."
#
# ✔ Same function can work
#   with many object types.
#
# ✔ len() is an example of
#   function polymorphism.
#
# ✔ Different classes can have
#   methods with the same name.
#
# ✔ Python automatically calls
#   the correct method based on
#   the object's type.
#
# ✔ Polymorphism works perfectly
#   with inheritance.
#
# ✔ Child classes can override
#   parent methods.
#
# ✔ If a child doesn't override
#   a method, Python uses the
#   parent's version.
#
# ==========================================================

# ---------------------------------------------------------------------------------------

# ==========================================================
# Python Encapsulation
# ==========================================================

# ----------------------------------------------------------
# What is Encapsulation?
# ----------------------------------------------------------
#
# Encapsulation means:
#
# Keeping data (properties) and methods together
# inside a class while controlling how the data
# can be accessed or modified.
#
# In simple words:
#
# "Hide important data and only allow safe access."
#
#
# Real-Life Analogy
# -------------------------
#
# Think about an ATM.
#
# You can:
# ✔ Deposit money
# ✔ Withdraw money
# ✔ Check balance
#
# But you CANNOT directly open the ATM
# and change the amount of money inside.
#
# The ATM protects its internal data.
#
# Encapsulation works the same way.


# ==========================================================
# Private Properties
# ==========================================================
#
# In Python, adding TWO underscores (__)
# before a property makes it private.
#
# Syntax:
#
# self.__property
#
#
# Private properties should only be
# accessed inside the class.


# ==========================================================
# Example: Private Property
# ==========================================================

class Person:

    def __init__(self, name, age):
        self.name = name

        # Private property
        self.__age = age


# Creating an object
p1 = Person("Emil", 25)

# Uncomment to check manually
# print(p1.name)

# Uncommenting this will cause an error
# because __age is private.
#
# print(p1.__age)


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Why does this give an error?
#
# Because Python hides __age
# from code outside the class.
#
#
# Outside the class
#
# Person
#   │
#   ├── name      ✔ Accessible
#   │
#   └── __age     ✖ Hidden
#
#
# Only methods INSIDE Person
# can directly use __age.


# ==========================================================
# Getter Method
# ==========================================================
#
# Since private properties cannot be
# accessed directly, we create
# a getter method.
#
# Getter = Read data safely.


# ==========================================================
# Example: Getter Method
# ==========================================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age


# Creating an object
p1 = Person("Tobias", 25)

# Uncomment to check manually
# print(p1.get_age())


# ==========================================================
# Setter Method
# ==========================================================
#
# A setter changes a private property.
#
# It also allows us to validate
# the value before saving it.
#
# Setter = Change data safely.


# ==========================================================
# Example: Setter Method
# ==========================================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):

        if age > 0:
            self.__age = age

        else:
            print("Age must be positive")


# Creating an object
p1 = Person("Tobias", 25)

# Uncomment to check manually
# print(p1.get_age())

# Change age
# p1.set_age(35)

# Uncomment to check manually
# print(p1.get_age())

# Invalid value
# p1.set_age(-5)


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Why not allow:
#
# p1.__age = -100
#
# ?
#
# Because someone could accidentally
# store invalid data.
#
#
# Using a setter lets us check:
#
# Is the value valid?
#
# Yes
#   │
#   ▼
# Save it
#
#
# No
#   │
#   ▼
# Reject it
#
#
# This is one of the biggest advantages
# of encapsulation.


# ==========================================================
# Why Use Encapsulation?
# ==========================================================
#
# Encapsulation provides:
#
# ✔ Data Protection
#
# Prevents accidental modification.
#
#
# ✔ Validation
#
# Check values before saving.
#
#
# ✔ Flexibility
#
# Internal code can change without
# affecting outside code.
#
#
# ✔ Control
#
# Decide who can read
# and who can modify data.


# ==========================================================
# Example: Protect and Validate Data
# ==========================================================

class Student:

    def __init__(self, name):
        self.name = name

        # Private property
        self.__grade = 0
        print("New student created " + self.name)


    def set_grade(self, grade):

        if 0 <= grade <= 100:
            self.__grade = grade
            print("Grade set to", self.__grade)

        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
        print("Getting grade...")
        return self.__grade


    def get_status(self):

        if self.__grade >= 60:
            return f"Passed with {self.__grade}" 

        else:
            return "Failed with {self.__grade}"


# Creating an object
# student = Student("Rohan")

# # Setting grade
# student.set_grade(85)

# # Uncomment to check manually
# print(student.get_grade())
# print(student.get_status())


# ==========================================================
# Protected Properties
# ==========================================================
#
# A SINGLE underscore (_)
# means "protected."
#
# Syntax:
#
# self._property
#
#
# IMPORTANT:
#
# This is ONLY a convention.
#
# Python does NOT enforce it.
#
# Other programmers are expected
# not to access it directly.


# ==========================================================
# Example: Protected Property
# ==========================================================

class Person:

    def __init__(self, name, salary):
        self.name = name

        # Protected property
        self._salary = salary


# Creating an object
p1 = Person("Linus", 50000)

# Uncomment to check manually
# print(p1.name)

# This works...
# but it is discouraged.
#
# print(p1._salary)


# ==========================================================
# Difference Between Public, Protected, and Private
# ==========================================================
#
# Public
# -----------------------
#
# self.name
#
# ✔ Accessible everywhere.
#
#
# Protected
# -----------------------
#
# self._salary
#
# ✔ Accessible
#
# But programmers should
# treat it as internal.
#
#
# Private
# -----------------------
#
# self.__age
#
# ✖ Cannot be accessed directly
# outside the class.


# ==========================================================
# Private Methods
# ==========================================================
#
# Methods can also be private.
#
# Use TWO underscores.
#
# Syntax:
#
# def __method():
#
#
# Private methods can only be
# called inside the class.


# ==========================================================
# Example: Private Method
# ==========================================================

class Calculator:

    def __init__(self):
        self.result = 0

    # Private method
    def __validate(self, num):

       
        if not isinstance(num, (int, float)):
            return False

        return True

    def add(self, num):

        if self.__validate(num):
            self.result += num

        else:
            print("Invalid number")


# Creating an object
calc = Calculator()

# calc.add(10)
# calc.add(5)
# calc.add("ABc")

# Uncomment to check manually
# print(calc.result)

# Uncommenting below will cause an error
#
# calc.__validate(5)


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Why make __validate() private?
#
# Because validation is only
# an INTERNAL task.
#
# Users should only call:
#
# add()
#
# NOT
#
# __validate()
#
#
# User
#   │
#   ▼
# add()
#   │
#   ▼
# __validate()
#   │
#   ▼
# Add number
#
#
# This hides unnecessary details.


# ==========================================================
# Name Mangling
# ==========================================================
#
# This is one of the MOST confusing
# Python concepts.
#
# IMPORTANT:
#
# Python does NOT truly make
# variables private.
#
# Instead...
#
# Python secretly RENAMES them.
#
#
# Example:
#
# __age
#
# becomes
#
# _Person__age
#
#
# This process is called:
#
# Name Mangling


# ==========================================================
# Example: Name Mangling
# ==========================================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age


# Creating an object
p1 = Person("Emil", 30)

# Uncomment to check manually
#
# print(p1.__age)
# print(p1._Person__age)


# Output:
#
# 30


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Wait...
#
# Didn't Python say __age
# is private?
#
# Yes...
#
# But internally Python renamed it.
#
#
# You SHOULD NOT access it this way.
#
# Why?
#
# Because it breaks encapsulation.
#
#
# Instead use:
#
# get_age()
#
# and
#
# set_age()
#
#
# Think of _Person__age
# as an emergency back door,
# not the main entrance.


# ==========================================================
# Summary
# ==========================================================
#
# ✔ Encapsulation protects data.
#
# ✔ Public Property
#
#     self.name
#
#     Accessible everywhere.
#
#
# ✔ Protected Property
#
#     self._salary
#
#     Accessible but intended
#     for internal use.
#
#
# ✔ Private Property
#
#     self.__age
#
#     Hidden from outside code.
#
#
# ✔ Getter
#
#     Read private data safely.
#
#
# ✔ Setter
#
#     Modify private data safely
#     with validation.
#
#
# ✔ Private methods use
#     double underscores.
#
#
# ✔ Python implements privacy
#     using Name Mangling.
#
#
# ✔ __age becomes:
#
#     _Person__age
#
#
# ✔ Accessing the mangled name
#   is possible but NOT recommended.
#
# ==========================================================

# -------------------------------------------------------------------------------------------------

# ==========================================================
# Python Inner Classes
# ==========================================================

# ----------------------------------------------------------
# What is an Inner Class?
# ----------------------------------------------------------
#
# An Inner Class is simply a class
# defined inside another class.
#
# Syntax:
#
# class Outer:
#
#     class Inner:
#         ...
#
#
# Think of it as:
#
# Outer Class
# ├── Properties
# ├── Methods
# └── Inner Class
#
#
# Inner classes are useful when
# the inner class only makes sense
# inside the outer class.
#
#
# Real-Life Analogy
# -------------------------
#
# Think about a Car.
#
# A car has:
#
# Car
# ├── Engine
# ├── Wheels
# └── Battery
#
# The Engine is closely related
# to the Car.
#
# Instead of creating Engine as
# a completely separate class,
# we can place it inside Car.
#
# This keeps related code together.


# ==========================================================
# Example: Create an Inner Class
# ==========================================================

class Outer:

    def __init__(self):
        self.name = "Outer Class"

    class Inner:

        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print("This is the inner class")


# Creating an object of Outer
outer = Outer()

# Uncomment to check manually
# print(outer.Inner.display)


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Does creating an Outer object
# automatically create an Inner object?
#
# NO.
#
# Outer and Inner are still
# separate classes.
#
#
# Creating:
#
# outer = Outer()
#
# creates ONLY:
#
# Outer object
#
#
# It does NOT create:
#
# Inner object.
#
#
# You must create Inner separately.


# ==========================================================
# Accessing Inner Class from Outside
# ==========================================================
#
# To use the inner class,
# first create an Outer object,
# then create an Inner object.


# ==========================================================
# Example
# ==========================================================

class Outer:

    def __init__(self):
        self.name = "Outer"

    class Inner:

        def __init__(self):
            self.name = "Inner"

        def display(self):
            print("Hello from inner class")


# Creating Outer object
outer = Outer()

# Creating Inner object
inner = outer.Inner()

# Uncomment to check manually
# inner.display()


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Why do we write:
#
# outer.Inner()
#
# ?
#
# Because Inner belongs to Outer.
#
#
# Think of it like folders.
#
# Outer
# └── Inner
#
#
# So Python finds Inner
# inside Outer.
#
#
# It is similar to:
#
# math.sqrt()
#
# sqrt belongs to math.
#
#
# Likewise:
#
# Inner belongs to Outer.


# ==========================================================
# Accessing Outer Class from Inner Class
# ==========================================================
#
# One of the biggest beginner mistakes:
#
# They think Inner automatically knows
# everything about Outer.
#
# It DOES NOT.
#
#
# The Inner object and the Outer object
# are two different objects.
#
#
# If Inner needs Outer's data,
# we must pass the Outer object.


# ==========================================================
# Example
# ==========================================================

class Outer:

    def __init__(self):
        self.name = "Emil"

    class Inner:

        def __init__(self, outer):

            # Save Outer object
            self.outer = outer

        def display(self):
            print(f"Outer class name: {self.outer.name}")


# Creating Outer object
outer = Outer()

# Pass Outer object to Inner
inner = outer.Inner(outer)

# Uncomment to check manually
# inner.display()


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Why do we pass "outer"?
#
# Because:
#
# Outer object
#
# and
#
# Inner object
#
# are separate.
#
#
# Memory Diagram
#
# Outer Object
# -------------------
# name = "Emil"
#
#
# Inner Object
# -------------------
# outer ---> Outer Object
#
#
# When we write:
#
# self.outer.name
#
# Python follows:
#
# Inner Object
#      │
#      ▼
# Outer Object
#      │
#      ▼
# name
#
#
# Without passing "outer",
# the Inner object has no idea
# which Outer object it belongs to.


# ==========================================================
# Practical Example
# ==========================================================
#
# Inner classes are commonly used
# for helper classes that are only
# meaningful inside another class.
#
# Example:
#
# Car
# └── Engine


# ==========================================================
# Example: Car and Engine
# ==========================================================

class Car:

    def __init__(self, brand, model):

        self.brand = brand
        self.model = model

        # Create an Engine object
        self.engine = self.Engine()

    class Engine:

        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def drive(self):

        if self.engine.status == "Running":

            print(f"Driving the {self.brand} {self.model}")

        else:

            print("Start the engine first!")


# Creating a Car object
car = Car("Toyota", "Corolla")

# Uncomment to check manually
#
# car.drive()
# #
# car.engine.start()
# #
# car.drive()
# #
# car.engine.stop()


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Notice this line:
#
# self.engine = self.Engine()
#
#
# This creates an Engine object
# automatically whenever a Car
# object is created.
#
#
# Memory Diagram
#
# Car Object
# ---------------------
# brand
# model
# engine ───────────────┐
#                       │
#                       ▼
#                  Engine Object
#                  status = "Off"
#
#
# Therefore:
#
# car.engine.start()
#
# first goes to:
#
# car
#   │
#   ▼
# engine
#   │
#   ▼
# start()


# ==========================================================
# Multiple Inner Classes
# ==========================================================
#
# A class can contain
# more than one inner class.
#
# Example:
#
# Computer
# ├── CPU
# └── RAM


# ==========================================================
# Example
# ==========================================================

class Computer:

    def __init__(self):

        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:

        def process(self):
            print("Processing data...")

    class RAM:

        def store(self):
            print("Storing data...")


# Creating a Computer object
computer = Computer()

# Uncomment to check manually
#
# computer.cpu.process()
# #
# computer.ram.store()


# ==========================================================
# Why Use Inner Classes?
# ==========================================================
#
# ✔ Better organization
#
# Related classes stay together.
#
#
# ✔ Encapsulation
#
# Hide helper classes inside
# the main class.
#
#
# ✔ Cleaner code
#
# Avoid unnecessary global classes.
#
#
# ✔ Improves readability
#
# Makes relationships between
# classes obvious.


# ==========================================================
# Difference Between Normal Class and Inner Class
# ==========================================================
#
# Normal Class
# ----------------------------
#
# class Engine:
#     ...
#
# class Car:
#     ...
#
#
# Engine exists independently.
#
#
# Inner Class
# ----------------------------
#
# class Car:
#
#     class Engine:
#         ...
#
#
# Engine is closely tied
# to Car.
#
#
# Use Inner Class when
# the helper class is not
# useful on its own.


# ==========================================================
# Summary
# ==========================================================
#
# ✔ An Inner Class is a class
#   inside another class.
#
# ✔ Creating an Outer object
#   does NOT automatically
#   create an Inner object.
#
# ✔ Access Inner using:
#
#       outer.Inner()
#
# ✔ Inner objects do NOT
#   automatically know about
#   Outer objects.
#
# ✔ Pass the Outer object
#   if Inner needs its data.
#
# ✔ Inner classes help
#   organize related code.
#
# ✔ They are commonly used
#   for helper classes such as:
#
#     Car → Engine
#     Computer → CPU
#     Computer → RAM
#
# ✔ Use Inner Classes when
#   the nested class is only
#   meaningful within the
#   outer class.
#
# ==========================================================