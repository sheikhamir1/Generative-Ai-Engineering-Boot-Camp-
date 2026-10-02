# ============================================================
# Python Sets
# ============================================================

# ------------------------------------------------------------
# What is a Set?
# ------------------------------------------------------------
# A Set is a built-in Python data type used to store multiple
# items in a single variable.
#
# Python has four main collection data types:
# 1. List       -> Ordered, Changeable, Allows Duplicates
# 2. Tuple      -> Ordered, Unchangeable, Allows Duplicates
# 3. Set        -> Unordered, Unchangeable*, No Duplicates
# 4. Dictionary -> Ordered (Python 3.7+), Changeable, No Duplicate Keys
#
# * Set items themselves cannot be modified, but items can be
#   added or removed.
#
# Sets are written using curly braces {}.
# ============================================================


# ------------------------------------------------------------
# Creating a Set
# ------------------------------------------------------------

myset = {"apple", "banana", "cherry"}

# Print the set
# print(myset)


# ============================================================
# Properties of Sets
# ============================================================

# 1. Unordered
# ------------------------------------------------------------
# Set items have NO fixed order.
# Every time you print a set, the order may be different.
#
# Because sets are unordered:
# - No indexing
# - No slicing

thisset = {"apple", "banana", "cherry"}

# print(thisset)


# ------------------------------------------------------------
# 2. Unchangeable
# ------------------------------------------------------------
# Once a set is created, individual items cannot be changed.
#
# ❌ Not Allowed
# thisset[0] = "orange"
#
# ✔ Allowed
# - Add new items
# - Remove existing items


# ------------------------------------------------------------
# 3. No Duplicate Values
# ------------------------------------------------------------
# Duplicate values are automatically ignored.

thisset = {"apple", "banana", "cherry", "apple"}

# Output:
# {'apple', 'banana', 'cherry'}
#
# print(thisset)


# ============================================================
# Special Case: True and 1
# ============================================================

# True and 1 are treated as the SAME value.

thisset = {"apple", "banana", "cherry", True, 1, 2}

# Since True == 1, only one of them is stored.
#
# print(thisset)


# ============================================================
# Special Case: False and 0
# ============================================================

# False and 0 are treated as the SAME value.

thisset = {"apple", "banana", "cherry", False, True, 0}

# False and 0 are duplicates.
#
# print(thisset)


# ============================================================
# Length of a Set
# ============================================================

thisset = {"apple", "banana", "cherry"}

# len() returns the number of unique items.
#
# print(len(thisset))


# ============================================================
# Set Items - Data Types
# ============================================================

# A set can contain strings.
set1 = {"apple", "banana", "cherry"}

# A set can contain integers.
set2 = {1, 5, 7, 9, 3}

# A set can contain booleans.
set3 = {True, False, False}

# False appears only once because duplicates are removed.


# ------------------------------------------------------------
# Mixed Data Types
# ------------------------------------------------------------

# A set can also store different data types together.

mixed_set = {"abc", 34, True, 40, "male"}

# print(mixed_set)


# ============================================================
# Data Type of a Set
# ============================================================

myset = {"apple", "banana", "cherry"}

# type() returns the object's data type.
#
# Output:
# <class 'set'>
#
# print(type(myset))


# ============================================================
# Creating a Set Using set() Constructor
# ============================================================

# Another way to create a set is by using the set() constructor.

thisset = set(("apple", "banana", "cherry"))
# Note the double parentheses:
# set((item1, item2, item3))

# print(thisset)
# print(type(thisset))


# ============================================================
# Python Collection Types Summary
# ============================================================

# ------------------------------------------------------------
# List
# ------------------------------------------------------------
# Ordered      : Yes
# Changeable   : Yes
# Duplicates   : Yes

# Example
my_list = ["apple", "banana", "apple"]


# ------------------------------------------------------------
# Tuple
# ------------------------------------------------------------
# Ordered      : Yes
# Changeable   : No
# Duplicates   : Yes

# Example
my_tuple = ("apple", "banana", "apple")


# ------------------------------------------------------------
# Set
# ------------------------------------------------------------
# Ordered      : No
# Changeable   : No*
# Indexed      : No
# Duplicates   : No
#
# *Items cannot be modified, but they can be added or removed.

# Example
my_set = {"apple", "banana", "cherry"}


# ------------------------------------------------------------
# Dictionary
# ------------------------------------------------------------
# Ordered      : Yes (Python 3.7+)
# Changeable   : Yes
# Duplicate Keys : No

# Example
my_dict = {
    "name": "John",
    "age": 25
}


# ============================================================
# Quick Summary
# ============================================================

# ✔ Stores unique values only
# ✔ Unordered collection
# ✔ Unindexed (no indexing or slicing)
# ✔ Can contain multiple data types
# ✔ Mutable container (can add/remove items)
# ✔ Items themselves are immutable
# ✔ Duplicate values are automatically removed
# ✔ True == 1
# ✔ False == 0
# ✔ Created using {} or set()
#
# Useful Functions:
# -----------------
# len(set_name)     -> Number of elements
# type(set_name)    -> Returns <class 'set'>
# set(iterable)     -> Creates a new set

# -----------------------------------------------------------------------------------------------------------------

# ============================================================
# Python Sets - Access, Add, and Remove Items
# ============================================================

# ============================================================
# Accessing Set Items
# ============================================================

# ------------------------------------------------------------
# Can We Access Set Items Using an Index?
# ------------------------------------------------------------
# ❌ No.
#
# Sets are unordered and unindexed, so you cannot access
# items using an index like:
#
# thisset[0]   ❌ Error
#
# Instead, you can:
# 1. Loop through the set
# 2. Check whether an item exists using 'in'
# 3. Check whether an item does NOT exist using 'not in'


# ============================================================
# Loop Through a Set
# ============================================================

thisset = {"apple", "banana", "cherry"}

# Use a for loop to access every item.

for item in thisset:
    # print(item)
    pass

# Note:
# Since sets are unordered, the order of output
# may be different every time.


# ============================================================
# Check if an Item Exists
# ============================================================

thisset = {"apple", "banana", "cherry"}

# The 'in' keyword returns True if the item exists.

# print("banana" in thisset)

# Output:
# True


# ============================================================
# Check if an Item Does NOT Exist
# ============================================================

thisset = {"apple", "banana", "cherry"}

# The 'not in' keyword returns True if the item
# does not exist.

# print("banana" not in thisset)

# Output:
# False


# ============================================================
# Can We Change Existing Items?
# ============================================================

# ❌ No.
#
# Existing items cannot be modified because set items
# are immutable.
#
# ✔ However, you CAN:
# - Add new items
# - Remove existing items


# ============================================================
# Adding Items to a Set
# ============================================================

# ------------------------------------------------------------
# add() Method
# ------------------------------------------------------------
# Used to add ONE item.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

# print(thisset)


# ============================================================
# Adding Multiple Items (Another Set)
# ============================================================

# ------------------------------------------------------------
# update() Method
# ------------------------------------------------------------
# Adds all items from another set.

thisset = {"apple", "banana", "cherry"}

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

# print(thisset)


# ============================================================
# update() with Any Iterable
# ============================================================

# update() does NOT require another set.
#
# It accepts any iterable:
# ✔ List
# ✔ Tuple
# ✔ Dictionary
# ✔ String
# ✔ Set

thisset = {"apple", "banana", "cherry"}

mylist = ["kiwi", "orange"]

thisset.update(mylist)

# print(thisset)
# print(type(thisset))


# ============================================================
# Removing Items from a Set
# ============================================================

# There are several ways to remove items:
#
# 1. remove()
# 2. discard()
# 3. pop()
# 4. clear()
# 5. del


# ============================================================
# remove() Method
# ============================================================

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

# print(thisset)

# Important:
# If the item does NOT exist,
# remove() raises a KeyError.


# Example (Will Raise Error)

# thisset.remove("orange")


# ============================================================
# discard() Method
# ============================================================

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

# print(thisset)

# Important:
# If the item does NOT exist,
# discard() does NOTHING.
#
# No error is raised.


# Example (Safe)

# thisset.discard("orange")


# ============================================================
# remove() vs discard()
# ============================================================

# remove()
# --------
# Raises an error if the item is missing.

# discard()
# ----------
# Does NOT raise an error if the item is missing.


# ============================================================
# pop() Method
# ============================================================

# Removes and returns a RANDOM item.

thisset = {"apple", "banana", "cherry"}

removed_item = thisset.pop()

# print(removed_item)

# print(thisset)

# Important:
# Sets are unordered.
#
# Therefore, you do NOT know which item
# will be removed.


# ============================================================
# clear() Method
# ============================================================

# Removes ALL items.
#
# The set still exists.

thisset = {"apple", "banana", "cherry"}

thisset.clear()

# print(thisset)

# Output:
# set()


# ============================================================
# del Keyword
# ============================================================

# Deletes the ENTIRE set object.

thisset = {"apple", "banana", "cherry"}

del thisset

# The following line would raise an error because
# the variable no longer exists.

# print(thisset)


# ============================================================
# Summary of Removal Methods
# ============================================================

# remove(item)
# ------------
# Removes the specified item.
# Raises KeyError if the item does not exist.

# discard(item)
# -------------
# Removes the specified item.
# Does NOT raise an error if the item is missing.

# pop()
# -----
# Removes and returns a random item.

# clear()
# -------
# Removes all items.
# The set still exists.

# del
# ---
# Deletes the entire set object.


# ============================================================
# Quick Summary
# ============================================================

# ✔ Sets cannot be accessed by index.
# ✔ Use a for loop to access all items.
# ✔ Use 'in' to check if an item exists.
# ✔ Use 'not in' to check if an item does not exist.
# ✔ add() adds a single item.
# ✔ update() adds multiple items from any iterable.
# ✔ remove() raises an error if the item is missing.
# ✔ discard() safely removes an item.
# ✔ pop() removes a random item.
# ✔ clear() empties the set.
# ✔ del deletes the entire set object.

# -----------------------------------------------------------------------------------------

# ============================================================
# Python Sets - Looping and Joining Sets
# ============================================================

# ============================================================
# Looping Through a Set
# ============================================================

# Since sets are unordered, you cannot access elements
# using indexes like:
#
# thisset[0]   ❌ Error
#
# Instead, use a for loop to iterate through every item.

thisset = {"apple", "banana", "cherry"}

for item in thisset:
    # print(item)
    pass

# Note:
# The order of items may change every time you run the program.


# ============================================================
# Joining Sets
# ============================================================

# Python provides several ways to combine or compare sets.
#
# Main Methods:
#
# union()                     -> Combines all unique elements
# update()                    -> Adds elements to the original set
# intersection()              -> Keeps only common elements
# intersection_update()       -> Same as intersection(), modifies original set
# difference()                -> Keeps elements only in first set
# difference_update()         -> Same as difference(), modifies original set
# symmetric_difference()      -> Keeps elements NOT common to both sets
# symmetric_difference_update()-> Same as above, modifies original set


# ============================================================
# union() Method
# ============================================================

# Combines two sets and returns a NEW set.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

# print(set3)

# Output:
# {'a', 'b', 'c', 1, 2, 3}


# ============================================================
# Using the | Operator
# ============================================================

# The | operator works exactly like union().

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2

# print(set3)


# ============================================================
# Joining Multiple Sets Using union()
# ============================================================

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "banana", "cherry"}

myset = set1.union(set2, set3, set4)

# print(myset)


# ============================================================
# Joining Multiple Sets Using |
# ============================================================

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "banana", "cherry"}

myset = set1 | set2 | set3 | set4

# print(myset)


# ============================================================
# Joining a Set with Other Iterables
# ============================================================

# union() accepts other iterable data types,
# such as tuples and lists.

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)

# print(z)

# Note:
# The | operator ONLY works between sets.
#
# x | y   ❌ Error


# ============================================================
# update() Method
# ============================================================

# update() adds all elements into the ORIGINAL set.
#
# Unlike union(), it does NOT return a new set.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

x = set1.update(set2)

# print(x)
# print(set1)


# ============================================================
# union() vs update()
# ============================================================

# union()
# -------
# ✔ Returns a NEW set
# ✔ Original sets remain unchanged

# update()
# --------
# ✔ Modifies the ORIGINAL set
# ✔ Returns None


# ============================================================
# intersection() Method
# ============================================================

# Keeps ONLY the common (duplicate) elements.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)

# print(set3)

# Output:
# {'apple'}


# ============================================================
# Using the & Operator
# ============================================================

# The & operator performs the same operation
# as intersection().

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2

# print(set3)

# Note:
# & only works with sets.


# ============================================================
# intersection_update() Method
# ============================================================

# Keeps only common elements.
#
# Changes the ORIGINAL set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

# print(set1)

# Output:
# {'apple'}


# ============================================================
# Special Case: True, False, 1 and 0
# ============================================================

# True == 1
# False == 0

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

# print(set3)

# Because:
# True == 1
# False == 0


# ============================================================
# difference() Method
# ============================================================

# Keeps only items that exist in the FIRST set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

# print(set3)

# Output:
# {'banana', 'cherry'}


# ============================================================
# Using the - Operator
# ============================================================

# The - operator performs the same task
# as difference().

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2

# print(set3)

# Note:
# - only works with sets.


# ============================================================
# difference_update() Method
# ============================================================

# Removes common elements from the ORIGINAL set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

# print(set1)

# Output:
# {'banana', 'cherry'}


# ============================================================
# symmetric_difference() Method
# ============================================================

# Keeps everything EXCEPT the common elements.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

# print(set3)

# Output:
# {'banana', 'cherry', 'google', 'microsoft'}


# ============================================================
# Using the ^ Operator
# ============================================================

# The ^ operator performs the same operation
# as symmetric_difference().

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

# print(set3)

# Note:
# ^ only works with sets.


# ============================================================
# symmetric_difference_update() Method
# ============================================================

# Keeps non-common elements.
#
# Modifies the ORIGINAL set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

# print(set1)


# ============================================================
# Comparison of Set Operations
# ============================================================

# ------------------------------------------------------------
# union()
# ------------------------------------------------------------
# Symbol: |
#
# Returns:
# All unique elements from both sets.

# Example:
# {1,2} | {2,3}
# Result:
# {1,2,3}


# ------------------------------------------------------------
# intersection()
# ------------------------------------------------------------
# Symbol: &
#
# Returns:
# Only common elements.

# Example:
# {1,2} & {2,3}
# Result:
# {2}


# ------------------------------------------------------------
# difference()
# ------------------------------------------------------------
# Symbol: -
#
# Returns:
# Elements in the first set but NOT in the second.

# Example:
# {1,2} - {2,3}
# Result:
# {1}


# ------------------------------------------------------------
# symmetric_difference()
# ------------------------------------------------------------
# Symbol: ^
#
# Returns:
# Elements present in either set,
# but NOT in both.

# Example:
# {1,2} ^ {2,3}
# Result:
# {1,3}


# ============================================================
# Methods That Modify the Original Set
# ============================================================

# update()
# -------------------------------
# Adds all unique elements.

# intersection_update()
# -------------------------------
# Keeps only common elements.

# difference_update()
# -------------------------------
# Removes common elements.

# symmetric_difference_update()
# -------------------------------
# Keeps only non-common elements.


# ============================================================
# Quick Summary
# ============================================================

# ✔ Use a for loop to iterate through a set.
# ✔ union() or | combines sets.
# ✔ update() modifies the original set.
# ✔ intersection() or & keeps common elements.
# ✔ difference() or - keeps only unique elements from the first set.
# ✔ symmetric_difference() or ^ keeps non-common elements.
# ✔ *_update() methods modify the original set instead of creating a new one.
# ✔ union() accepts other iterables (list, tuple, etc.).
# ✔ |, &, -, and ^ only work between sets.

# ----------------------------------------------------------------------------------------------

# ============================================================
# Python frozenset
# ============================================================

# ============================================================
# What is a frozenset?
# ============================================================

# A frozenset is an IMMUTABLE version of a set.
#
# Immutable means:
# ❌ You cannot add elements.
# ❌ You cannot remove elements.
# ❌ You cannot modify existing elements.
#
# Like a normal set, a frozenset:
# ✔ Stores only unique values.
# ✔ Is unordered.
# ✔ Is unindexed.
# ✔ Automatically removes duplicates.
#
# Unlike a normal set:
# ✔ It cannot be changed after creation.


# ============================================================
# Creating a frozenset
# ============================================================

# Use the frozenset() constructor.
#
# It accepts any iterable such as:
# - List
# - Tuple
# - Set
# - String
# - Dictionary (keys only)

fruits = frozenset({"apple", "banana", "cherry"})

# print(fruits)

# print(type(fruits))

# Output:
# <class 'frozenset'>


# ============================================================
# Duplicate Values
# ============================================================

# Like normal sets, duplicate values are ignored.

numbers = frozenset([1, 2, 2, 3, 3, 4])

# print(numbers)

# Output:
# frozenset({1, 2, 3, 4})


# ============================================================
# Cannot Modify a frozenset
# ============================================================

items = frozenset({"apple", "banana"})
# print(items)
# The following operations are NOT allowed.

# items.add("orange")          ❌ AttributeError
# items.remove("apple")        ❌ AttributeError
# items.discard("banana")      ❌ AttributeError
# items.clear()                ❌ AttributeError
# items.pop()                  ❌ AttributeError

# A frozenset is read-only.


# ============================================================
# Supported Operations
# ============================================================

# Since frozensets cannot be modified,
# only NON-MUTATING methods are available.

# Available Methods:
#
# copy()
# difference()
# intersection()
# isdisjoint()
# issubset()
# issuperset()
# symmetric_difference()
# union()


# ============================================================
# copy()
# ============================================================

set1 = frozenset({"apple", "banana", "cherry"})

copy_set = set1.copy()

# print(copy_set)

# Note:
# Since frozensets are immutable,
# copy() simply returns another frozenset.


# ============================================================
# union()
# ============================================================

# Combines all unique elements.

set1 = frozenset({"apple", "banana"})
set2 = frozenset({"orange", "banana"})

result = set1.union(set2)

# print(result)

# Equivalent operator:
# result = set1 | set2


# ============================================================
# intersection()
# ============================================================

# Keeps only common elements.

set1 = frozenset({"apple", "banana"})
set2 = frozenset({"banana", "orange"})

result = set1.intersection(set2)

# print(result)

# Equivalent operator:
# result = set1 & set2


# ============================================================
# difference()
# ============================================================

# Keeps elements that exist only in the first frozenset.

set1 = frozenset({"apple", "banana", "orange"})
set2 = frozenset({"banana"})

result = set1.difference(set2)

# print(result)

# Equivalent operator:
# result = set1 - set2


# ============================================================
# symmetric_difference()
# ============================================================

# Keeps elements that are NOT common.

set1 = frozenset({"apple", "banana"})
set2 = frozenset({"banana", "orange"})

result = set1.symmetric_difference(set2)

# print(result)

# Equivalent operator:
# result = set1 ^ set2


# ============================================================
# isdisjoint()
# ============================================================

# Returns True if two frozensets
# have NO common elements.

set1 = frozenset({"apple", "banana"})
set2 = frozenset({"orange", "kiwi"})

# print(set1.isdisjoint(set2))

# Output:
# True


# ============================================================
# issubset()
# ============================================================

# Returns True if every element of the first
# frozenset exists in the second.

small = frozenset({1, 2})
large = frozenset({1, 2, 3, 4})

# print(small.issubset(large))

# Equivalent:
# print(small <= large)


# ============================================================
# issuperset()
# ============================================================

# Returns True if the first frozenset
# contains every element of the second.

large = frozenset({1, 2, 3, 4})
small = frozenset({1, 2})

# print(large.issuperset(small))

# Equivalent:
# print(large >= small)


# ============================================================
# frozenset Operators
# ============================================================

# |   -> union()
# &   -> intersection()
# -   -> difference()
# ^   -> symmetric_difference()
# <=  -> issubset()
# >=  -> issuperset()


# ============================================================
# Set vs frozenset
# ============================================================

# ------------------------------------------------------------
# Feature Comparison
# ------------------------------------------------------------

# Normal Set
# ----------
# Mutable*            ✔ Yes
# Can add()          ✔ Yes
# Can remove()       ✔ Yes
# Can update()       ❌ No
# Duplicate values   ❌ Not allowed
# Ordered            ❌ No
# Indexed            ❌ No

# Frozenset
# ----------
# Mutable            ❌ No
# Can add()          ❌ No
# Can remove()       ❌ No
# Can update()       ❌ No
# Duplicate values   ❌ Not allowed
# Ordered            ❌ No
# Indexed            ❌ No


# ============================================================
# Python Set Methods
# ============================================================

# Python provides many built-in methods for working with sets.

# ============================================================
# Methods That MODIFY a Set
# ============================================================

# add(item)
# --------------------------
# Adds one element.

# update(iterable)
# --------------------------
# Adds multiple elements.

# remove(item)
# --------------------------
# Removes an item.
# Raises KeyError if missing.

# discard(item)
# --------------------------
# Removes an item.
# Does NOT raise an error if missing.

# pop()
# --------------------------
# Removes and returns a random element.

# clear()
# --------------------------
# Removes all elements.

# difference_update()
# --------------------------
# Removes common elements from the original set.

# intersection_update()
# --------------------------
# Keeps only common elements.

# symmetric_difference_update()
# --------------------------
# Keeps only non-common elements.


# ============================================================
# Methods That RETURN a New Set
# ============================================================

# copy()
# --------------------------
# Returns a shallow copy.

# union()
# --------------------------
# Returns all unique elements.

# intersection()
# --------------------------
# Returns only common elements.

# difference()
# --------------------------
# Returns elements only in the first set.

# symmetric_difference()
# --------------------------
# Returns non-common elements.


# ============================================================
# Comparison Methods
# ============================================================

# isdisjoint()
# --------------------------
# Returns True if no common elements exist.

# issubset()
# --------------------------
# Returns True if every element exists
# in another set.

# issuperset()
# --------------------------
# Returns True if all elements of another
# set exist in this set.


# ============================================================
# Set Method Shortcuts (Operators)
# ============================================================

# union()                     |
# update()                    |=
#
# intersection()              &
# intersection_update()        &=
#
# difference()                -
# difference_update()         -=
#
# symmetric_difference()      ^
# symmetric_difference_update()^=
#
# issubset()                  <=
# Proper subset               <
#
# issuperset()                >=
# Proper superset             >


# ============================================================
# Quick Summary
# ============================================================

# ✔ frozenset is an immutable version of a set.
# ✔ It stores only unique values.
# ✔ It is unordered and unindexed.
# ✔ You cannot add, remove, or update elements.
# ✔ Use frozenset() to create one.
# ✔ Only read-only (non-mutating) operations are allowed.
# ✔ Supports union(), intersection(), difference(),
#   symmetric_difference(), issubset(),
#   issuperset(), isdisjoint(), and copy().
# ✔ Normal sets are mutable.
# ✔ frozensets are immutable.