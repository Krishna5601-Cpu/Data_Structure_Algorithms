"""
Python Variables & Data Types - Short Notes
"""

# VARIABLES
# A variable is a name that refers to an object stored in memory.

name = "Krishna"
age = 20

print(name)
print(age)

# Check type
print(type(name))
print(type(age))

# VARIABLE NAMING RULES
# Can contain letters, numbers and underscore (_)
student_name = "Krishna"
age2 = 20
_value = 100

# Cannot start with a number
# 2age = 20

# No spaces
# student name = "Krishna"

# No special symbols
# marks$ = 95

# Cannot use Python keywords
# class = "BCA"
# True = False

# Python naming convention
total_marks = 95  # snake_case

# DYNAMIC TYPING

# The same variable can store different data types.

x = 10
print(x, type(x))

x = "Python"
print(x, type(x))

x = True
print(x, type(x))

# DATA TYPES

# int
a = 10

# float
b = 3.14

# complex
c = 2 + 3j

# bool
d = True

# str
e = "Hello"

# None
f = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# Complex number parts
print(c.real)
print(c.imag)

# String examples
language = "Python"
print(language[0])  # First character
print(language[-1])  # Last character
print(len(language))

# Boolean examples
print(10 > 5)
print(5 > 10)

# None check (Recommended)
user = None

if user is None:
    print("No user logged in.")

# IMPORTANT DSA NOTES
# 1. Python is dynamically typed.
# 2. Python is strongly typed.
# 3. Variables store references to objects.
# 4. Use type() to check data type.
# 5. Use 'is None' instead of '== None'.
# 6. Follow snake_case naming convention.

# PRACTICE QUESTIONS (WITHOUT RUNNING)
#
# Q1
# x = 10
# print(type(x))
#
# Q2
# x = 10
# x = "Python"
# print(x)
# print(type(x))
#
# Q3
# a = 5
# b = 2.5
# print(type(a))
# print(type(b))
#
# Q4
# name = "Python"
# print(name[0])
# print(name[-1])
#
# Q5
# x = None
# print(type(x))
#
# Q6
# print(10 > 5)
# print(3 == 7)

# YOUR ANSWERS (Corrections)
#
# Q1 -> <class 'int'>
# Q2 -> Python
#       <class 'str'>
# Q3 -> <class 'int'>
#       <class 'float'>
# Q4 -> P
#       n
# Q5 -> <class 'NoneType'>
# Q6 -> True
#       False
#
# Common mistakes:
# - Python type names are lowercase:
#   int, float, str, bool
# - NoneType has a capital T:
#   <class 'NoneType'>
# - Last character of "Python" is 'n', not 'N'.

