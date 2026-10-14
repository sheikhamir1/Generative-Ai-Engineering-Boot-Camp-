# ==========================================================
# Python File Handling - Opening Files
# ==========================================================

# ----------------------------------------------------------
# What is File Handling?
# ----------------------------------------------------------
#
# File Handling means working with files stored
# on your computer using Python.
#
# A file may contain:
#
# ✔ Text
# ✔ Numbers
# ✔ Images
# ✔ Videos
# ✔ Audio
# ✔ PDF documents
# ✔ Excel files
# ✔ JSON data
# ✔ CSV data
#
#
# Python allows us to:
#
# ✔ Create files
# ✔ Open files
# ✔ Read files
# ✔ Write files
# ✔ Append data
# ✔ Delete files
# ✔ Rename files
#
#
# Almost every real-world application
# uses file handling.
#
#
# Examples:
#
# • Saving user accounts
# • Saving game progress
# • Reading configuration files
# • Logging errors
# • Reading datasets
# • Processing images
# • Creating reports
# • Reading PDFs
# • Exporting Excel files


# ==========================================================
# Why Do We Need File Handling?
# ==========================================================
#
# Variables only exist while
# the program is running.
#
# Example:
#
# name = "Emil"
#
# When the program closes,
# this variable disappears.
#
#
# Files solve this problem.
#
# Files permanently store data.
#
#
# Memory (RAM)
# -----------------------
#
# Temporary
#
# Program Ends
#      ↓
# Data Lost
#
#
# File (Hard Disk / SSD)
# -----------------------
#
# Permanent
#
# Program Ends
#      ↓
# Data Still Exists


# ==========================================================
# The open() Function
# ==========================================================
#
# Python uses the open() function
# to work with files.
#
#
# Syntax:
#
# file_object = open(filename, mode)
#
#
# Example:
#
# f = open("data.txt", "r")
#
#
# open() returns a File Object.
#
# This object lets Python
# communicate with the file.


# ==========================================================
# Parameters of open()
# ==========================================================
#
# open(filename, mode)
#
#
# Parameter 1
# --------------------
#
# filename
#
# Name (or path) of the file.
#
#
# Examples:
#
# "notes.txt"
#
# "students.csv"
#
# "C:/Users/Emil/file.txt"
#
#
#
# Parameter 2
# --------------------
#
# mode
#
# Determines HOW the file
# will be opened.
#
# Read?
#
# Write?
#
# Append?
#
# Binary?
#
# Text?


# ==========================================================
# File Opening Modes
# ==========================================================
#
# Python provides several modes.
#
# The most common are:
#
# "r"
# "w"
# "a"
# "x"
#
#
# Text Modes:
#
# "t"
#
#
# Binary Mode:
#
# "b"


# ==========================================================
# Mode: "r" (Read)
# ==========================================================
#
# "r" means:
#
# Read an existing file.
#
#
# If the file DOES NOT exist,
# Python raises:
#
# FileNotFoundError
#
#
# Example:

# f = open("demofile.txt", "r")
# print(f)


# ==========================================================
# Mode: "w" (Write)
# ==========================================================
#
# "w" means:
#
# Open a file for writing.
#
#
# If the file exists:
#
# EVERYTHING inside it
# is erased first.
#
#
# If the file does NOT exist:
#
# Python creates it.
#
#
# Example:

# f = open("demofile.txt", "w")


# ==========================================================
# Important Warning
# ==========================================================
#
# Beginners often confuse
# "w" and "a".
#
#
# Existing file:
#
# Hello
# World
#
#
# Using:
#
# open("notes.txt", "w")
#
#
# File becomes:
#
# (Empty)
#
#
# Everything is deleted
# before writing.
#
#
# Use "w" carefully.


# ==========================================================
# Mode: "a" (Append)
# ==========================================================
#
# "a" means:
#
# Add new data
# to the END of a file.
#
#
# Existing data
# is NOT removed.
#
#
# If the file does not exist,
# Python creates it.
#
#
# Example:

# f = open("notes.txt", "a")


# ==========================================================
# Difference Between "w" and "a"
# ==========================================================
#
# Existing File
#
# Hello
# World
#
#
# Using "w"
#
# ↓
#
# Old content removed.
#
#
# Result:
#
# New Data
#
#
#
# Using "a"
#
# ↓
#
# Old content stays.
#
#
# Result:
#
# Hello
# World
# New Data


# ==========================================================
# Mode: "x" (Create)
# ==========================================================
#
# "x" means:
#
# Create a NEW file.
#
#
# If file already exists:
#
# Python raises:
#
# FileExistsError
#
#
# Example:

# f = open("newfile.txt", "x")


# ==========================================================
# When should you use "x"?
# ==========================================================
#
# Suppose you're creating:
#
# report.txt
#
#
# If the file already exists,
# you DON'T want to overwrite it.
#
#
# Using "x" protects you from
# accidentally replacing files.


# ==========================================================
# Text Mode ("t")
# ==========================================================
#
# "t" means:
#
# Text Mode.
#
#
# Used for:
#
# ✔ .txt
# ✔ .csv
# ✔ .json
# ✔ .xml
# ✔ .py
#
#
# Text mode is the DEFAULT.
#
#
# Example:

# f = open("notes.txt", "rt")

#
# Same as:
#

# f = open("notes.txt")


# ==========================================================
# Binary Mode ("b")
# ==========================================================
#
# Binary mode is used for
# NON-TEXT files.
#
#
# Examples:
#
# Images
#
# Videos
#
# Audio
#
# PDF
#
# ZIP
#
#
# Example:

# f = open("photo.jpg", "rb")


# ==========================================================
# Why Binary Mode?
# ==========================================================
#
# Text files contain characters.
#
#
# Example:
#
# Hello
#
#
# Image files contain bytes.
#
#
# Example:
#
# 101001011010100...
#
#
# Therefore:
#
# Images use:
#
# "rb"
#
#
# Not:
#
# "r"


# ==========================================================
# Default Mode
# ==========================================================
#
# Python automatically assumes:
#
# Read Mode
#
# and
#
# Text Mode
#
#
# Therefore:
#

# f = open("demofile.txt")

#
# is exactly the same as:
#

# f = open("demofile.txt", "rt")


# ==========================================================
# What Does open() Return?
# ==========================================================
#
# This is one of the most important
# beginner concepts.
#
# open() DOES NOT return
# the file contents.
#
#
# It returns:
#
# A File Object
#
#
# Example:

# f = open("notes.txt")

#
# Here:
#
# f
#
# is NOT a string.
#
#
# It is a special object
# that knows how to communicate
# with the file.
#
#
# Think of it like:
#
# Remote Control
#      │
#      ▼
# Television
#
#
# File Object
#      │
#      ▼
# Actual File


# ==========================================================
# Relative Path vs Absolute Path
# ==========================================================
#
# Files can be opened using
# either:
#
# Relative Path
#
# or
#
# Absolute Path


# ----------------------------------------------------------
# Relative Path
# ----------------------------------------------------------
#
# Relative paths start from
# the current project folder.
#
# Example:
#

# open("notes.txt")

#
# Project
# ├── main.py
# └── notes.txt
#
# Python finds notes.txt
# inside the same folder.


# ----------------------------------------------------------
# Absolute Path
# ----------------------------------------------------------
#
# Full path from the drive.
#
# Windows:
#

# open("C:/Users/Emil/Documents/notes.txt")

#
# Linux:
#

# open("/home/emil/notes.txt")


# ==========================================================
# Common File Modes
# ==========================================================
#
# "r"
# Read
#
#
# "w"
# Write (overwrite)
#
#
# "a"
# Append
#
#
# "x"
# Create new file
#
#
# "rb"
# Read binary
#
#
# "wb"
# Write binary
#
#
# "ab"
# Append binary


# ==========================================================
# Common Errors
# ==========================================================
#
# 1.
#
# FileNotFoundError
#
# Cause:
#
# File doesn't exist.
#
#
# Example:
#

# open("abc.txt")


#
# 2.
#
# PermissionError
#
# Cause:
#
# No permission to access file.
#
#
#
# 3.
#
# FileExistsError
#
# Cause:
#
# Using "x"
# on an existing file.


# ==========================================================
# Best Practice (VERY IMPORTANT)
# ==========================================================
#
# Always close a file
# after using it.
#
#
# Example:
#

# f = open("notes.txt", "r")
#
# Do work...
#
# f.close()
#
#
# Why?
#
# Because an open file uses
# operating system resources.
#
# Closing releases those resources.
#
#
# Even better (modern Python):
#
# Use:
#
# with open(...) as f:
#
# We'll learn this later.
#
# It automatically closes the file.


# ==========================================================
# Real-World Uses of File Handling
# ==========================================================
#
# Banking System
# ----------------
#
# Store customer data.
#
#
# Hospital
# ----------------
#
# Store patient records.
#
#
# School
# ----------------
#
# Store student marks.
#
#
# Web Applications
# ----------------
#
# Store logs.
#
#
# AI / Data Science
# ----------------
#
# Read datasets.
#
#
# Image Processing
# ----------------
#
# Read images.
#
#
# Games
# ----------------
#
# Save game progress.


# ==========================================================
# File Handling Roadmap
# ==========================================================
#
# File Handling
# │
# ├── open()
# │
# ├── Read Files
# │     ├── read()
# │     ├── readline()
# │     └── readlines()
# │
# ├── Write Files
# │     ├── write()
# │     └── writelines()
# │
# ├── File Pointer
# │     ├── seek()
# │     └── tell()
# │
# ├── Close Files
# │     └── close()
# │
# ├── Context Manager
# │     └── with open()
# │
# ├── File Paths
# │     ├── Relative
# │     └── Absolute
# │
# ├── Binary Files
# │
# └── Exception Handling
#       └── try...except


# ==========================================================
# Summary
# ==========================================================
#
# ✔ File handling allows Python
#   to create, read, write,
#   append, and delete files.
#
# ✔ open() is used to open files.
#
# ✔ Syntax:
#
#       open(filename, mode)
#
# ✔ Modes:
#
#     "r"  → Read
#     "w"  → Write (overwrite)
#     "a"  → Append
#     "x"  → Create new file
#
# ✔ Text mode:
#
#     "t"
#
# ✔ Binary mode:
#
#     "b"
#
# ✔ open() returns a File Object,
#   not the file contents.
#
# ✔ Relative paths start from
#   the current project folder.
#
# ✔ Absolute paths use the full
#   file location.
#
# ✔ Always close files after use,
#   or preferably use:
#
#       with open(...)
#
#   which closes files automatically.
#
# ==========================================================

# ----------------------------------------------------------------------------------------------------

# ==========================================================
# Python File Handling
# Reading, Writing, Creating & Deleting Files
# ==========================================================

# ----------------------------------------------------------
# Assume We Have This File
# ----------------------------------------------------------
#
# File Name:
#
# demofile.txt
#
#
# Contents:
#
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!
#
#
# Assume this file is in the SAME folder
# as our Python program.


# ==========================================================
# Opening and Reading a File
# ==========================================================
#
# open() returns a File Object.
#
# Then we use:
#
# read()
#
# to read its contents.


# ==========================================================
# Example
# ==========================================================

# Open file
f = open("demofile.txt", "rt")
# print(f)

# Uncomment to check manually
# print(f.read())


# ==========================================================
# What does read() do?
# ==========================================================
#
# read()
#
# Reads the ENTIRE file.
#
#
# Example Output:
#
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Remember:
#
# open()
#
# does NOT read the file.
#
#
# It only opens it.
#
#
# Then:
#
# read()
#
# actually reads the contents.
#
#
# Flow
#
# open()
#    │
#    ▼
# File Object
#    │
#    ▼
# read()
#    │
#    ▼
# File Contents


# ==========================================================
# Opening a File from Another Folder
# ==========================================================
#
# If the file is NOT inside the current folder,
# provide its path.
#
#
# Windows Example
#

# f = open("D:\\myfiles\\welcome.txt")

f = open("D:\\Youtube\\Javascipt\\Python Level 2\\Code\\0-Other\\welcome.txt")

# Uncomment to check manually
# print(f.read())


# ==========================================================
# Relative Path vs Absolute Path
# ==========================================================
#
# Relative Path
# -------------------------
#
# Starts from the current project.
#
#
# Example:
#
# open("notes.txt")
#
#
#
# Absolute Path
# -------------------------
#
# Full location.
#
#
# Example:
#
# open("D:\\myfiles\\welcome.txt")
#
#
# Linux Example:
#
# open("/home/user/file.txt")


# ==========================================================
# Using the with Statement
# ==========================================================
#
# Modern Python recommends:
#
# with open(...)
#
#
# Why?
#
# Because Python automatically
# closes the file.
#
#
# No need to call:
#
# close()


# ==========================================================
# Example
# ==========================================================

# Uncomment to check manually
#
# with open("demofile.txt") as f:
#     print(f.read())

with open("demofile.txt", "rt") as file:
    # print(file.read())
    pass


# ==========================================================
# Difficult Concept Explained
# ==========================================================
#
# Think of opening a file like
# opening a door.
#
#
# open()
#
# Door opens.
#
#
# close()
#
# Door closes.
#
#
# If you forget to close it,
# resources stay occupied.
#
#
# with
#
# automatically closes the door
# even if an error happens.
#
#
# Flow
#
# with open(...)
#      │
#      ▼
# Open File
#      │
#      ▼
# Execute Code
#      │
#      ▼
# Automatically Close File


# ==========================================================
# Closing Files
# ==========================================================
#
# If NOT using with,
# always call:
#
# close()


# ==========================================================
# Example
# ==========================================================

# f = open("demofile.txt")

# Uncomment to check manually
# print(f.readline())

# Close file
# f.close()


# ==========================================================
# Why Close Files?
# ==========================================================
#
# Closing files:
#
# ✔ Saves resources
#
# ✔ Flushes buffered data
#
# ✔ Prevents corruption
#
# ✔ Prevents file locking
#
#
# Especially important
# after writing to files.


# ==========================================================
# Buffering (Important Concept)
# ==========================================================
#
# Python doesn't always write
# data immediately.
#
# It temporarily stores data
# in memory.
#
#
# This temporary storage is called:
#
# Buffer
#
#
# Memory
# --------------------
#
# Write Data
#      │
#      ▼
# Buffer
#      │
#      ▼
# File
#
#
# Closing the file ensures
# everything reaches the file.


# ==========================================================
# read(size)
# ==========================================================
#
# read()
#
# reads everything.
#
#
# read(number)
#
# reads only that many characters.


# ==========================================================
# Example
# ==========================================================

# Uncomment to check manually
#
# with open("demofile.txt") as f:
#     print(f.read(5))


# Output:
#
# Hello


# ==========================================================
# Important Difference
# ==========================================================
#
# read()
#
# Reads entire file.
#
#
# read(5)
#
# Reads only
# five characters.


# ==========================================================
# readline()
# ==========================================================
#
# Reads ONE line
# at a time.


# ==========================================================
# Example
# ==========================================================

# Uncomment to check manually
#
# with open("demofile.txt") as f:
#     print(f.readline())


# Output:
#
# Hello! Welcome to demofile.txt


# ==========================================================
# Reading Multiple Lines
# ==========================================================

# Uncomment to check manually
#
# with open("demofile.txt") as f:
#     print(f.readline())
#     print(f.readline())


# Output:
#
# Hello! Welcome to demofile.txt
#
# This file is for testing purposes.


# ==========================================================
# How readline() Works
# ==========================================================
#
# Python remembers
# where it stopped reading.
#
#
# File
#
# Line 1
# Line 2
# Line 3
#
#
# First readline()
#
# ↓
#
# Reads Line 1
#
#
# Second readline()
#
# ↓
#
# Reads Line 2
#
#
# Third readline()
#
# ↓
#
# Reads Line 3


# ==========================================================
# Reading File Line by Line
# ==========================================================
#
# Files are iterable.
#
# Therefore we can use:
#
# for loop


# ==========================================================
# Example
# ==========================================================

# Uncomment to check manually
#
# with open("demofile.txt") as f:
#     for line in f:
#         print(line)


# ==========================================================
# Why Use a for Loop?
# ==========================================================
#
# Good for VERY LARGE files.
#
#
# read()
#
# loads everything into memory.
#
#
# for line in file
#
# reads one line at a time.
#
#
# Uses less memory.
#
#
# Therefore,
# for big files,
# use iteration.


# ==========================================================
# Writing to Existing Files
# ==========================================================
#
# Two common modes:
#
# "a"
#
# Append
#
#
# "w"
#
# Write (overwrite)


# ==========================================================
# Append Mode
# ==========================================================
#
# "a"
#
# Adds new text
# to the END.
#
#
# Existing content stays.


# ==========================================================
# Example
# ==========================================================

# Uncomment to check manually
#
# with open("demofile.txt", "a") as f:

#     f.write("Now the file has more content!")
# #
# #
# with open("demofile.txt") as f:

#     print(f.read())


# ==========================================================
# Append Flow
# ==========================================================
#
# Before
#
# Hello
# World
#
#
# After Append
#
# Hello
# World
# New Text


# ==========================================================
# Write Mode
# ==========================================================
#
# "w"
#
# Deletes EVERYTHING first.
#
# Then writes new content.


# ==========================================================
# Example
# ==========================================================

# Uncomment to check manually
#
# with open("demofile.txt", "w") as f:

#     f.write("Woops! I have deleted the content!")


# with open("demofile.txt") as f:

#     print(f.read())


# ==========================================================
# Write Flow
# ==========================================================
#
# Before
#
# Hello
# World
#
#
# Using "w"
#
# ↓
#
# File becomes empty
#
# ↓
#
# New text written.
#
#
# Result
#
# Woops!
# I have deleted the content!


# ==========================================================
# Creating New Files
# ==========================================================
#
# Three modes create files.
#
#
# "x"
#
# Create ONLY if
# file doesn't exist.
#
#
# "w"
#
# Creates if missing.
#
#
# "a"
#
# Creates if missing.


# ==========================================================
# Example
# ==========================================================

# Uncomment to check manually
#
# with open("myfile.txt", "x") as f :
#     f.write("Hello")


# with open("myfile.txt") as f:
#     print(f.read())


# ==========================================================
# Difference Between x, w and a
# ==========================================================
#
# x
#
# Existing?
#
# Error
#
#
# w
#
# Existing?
#
# Overwrite
#
#
# a
#
# Existing?
#
# Append


# ==========================================================
# Deleting Files
# ==========================================================
#
# Python uses the
# os module.


# ==========================================================
# Example
# ==========================================================

import os

# Uncomment to check manually
#
# os.remove("myfile.txt")


# ==========================================================
# Why Import os?
# ==========================================================
#
# File deletion is handled
# by the Operating System.
#
#
# Python asks:
#
# os.remove(...)
#
#
# The OS actually deletes it.


# ==========================================================
# Check Before Deleting
# ==========================================================
#
# Prevents:
#
# FileNotFoundError


# ==========================================================
# Example
# ==========================================================

# Uncomment to check manually
#
# if os.path.exists("test.txt"):

#     os.remove("test.txt")

# else:

#     print("The file does not exist")


# ==========================================================
# Why Check First?
# ==========================================================
#
# Suppose:
#
# demofile.txt
#
# was already deleted.
#
#
# Without checking:
#
# Error
#
#
# With checking:
#
# Safe.


# ==========================================================
# Deleting a Folder
# ==========================================================
#
# Use:
#
# os.rmdir()


# ==========================================================
# Example
# ==========================================================

# Uncomment to check manually
#
# os.rmdir("myfolder")


# ==========================================================
# Important Limitation
# ==========================================================
#
# os.rmdir()
#
# only removes
# EMPTY folders.
#
#
# Folder
# ├── file1.txt
# └── file2.txt
#
#
# os.rmdir()
#
# ❌ Error
#
#
# Folder
#
# (Empty)
#
# os.rmdir()
#
# ✔ Success


# ==========================================================
# File Handling Workflow
# ==========================================================
#
# File
# │
# ├── Open
# │      │
# │      └── open()
# │
# ├── Read
# │      ├── read()
# │      ├── readline()
# │      └── for loop
# │
# ├── Write
# │      ├── write()
# │      ├── "a"
# │      └── "w"
# │
# ├── Create
# │      └── "x"
# │
# ├── Close
# │      ├── close()
# │      └── with
# │
# └── Delete
#        ├── os.remove()
#        └── os.rmdir()


# ==========================================================
# Common Interview Questions
# ==========================================================
#
# Q1. Difference between read() and readline()?
#
# read()
# → Reads the whole file.
#
# readline()
# → Reads one line.
#
#
# Q2. Difference between "a" and "w"?
#
# a
# → Adds data.
#
# w
# → Deletes old data first.
#
#
# Q3. Why use with open()?
#
# It automatically closes
# the file.
#
#
# Q4. Why use os.path.exists()?
#
# To avoid errors when deleting files.
#
#
# Q5. What does open() return?
#
# A File Object,
# not the file contents.


# ==========================================================
# Summary
# ==========================================================
#
# ✔ open() opens a file.
#
# ✔ read() reads the whole file.
#
# ✔ read(size) reads a fixed number
#   of characters.
#
# ✔ readline() reads one line.
#
# ✔ Files can be iterated using
#   a for loop.
#
# ✔ with open() is the preferred
#   way because it automatically
#   closes files.
#
# ✔ close() should be called if
#   you're not using with.
#
# ✔ "a" appends data.
#
# ✔ "w" overwrites data.
#
# ✔ "x" creates a new file and
#   raises an error if it exists.
#
# ✔ os.remove() deletes files.
#
# ✔ os.path.exists() checks
#   if a file exists before
#   deleting it.
#
# ✔ os.rmdir() deletes only
#   empty folders.
#
# ==========================================================
