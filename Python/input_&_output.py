"""
Python Input & Output 
"""

# print()

print("Hello World")
print(100)
print(3.14)
print(True)

name = "Krishna"
age = 20

print(name)
print(age)

# Multiple values
print(name, age)

# sep parameter
print(1, 2, 3)
print(1, 2, 3, sep="-")
print("Python", "Java", "C++", sep=" | ")

# end parameter
print("Hello", end=" ")
print("World")

print()  # newline

# Escape characters
print("Hello\nWorld")
print("Python\tDSA")
print("C:\\Users\\Krishna")

# input()
# # input() ALWAYS returns a string.

# name = input("Enter your name: ")
# print(name)
# print(type(name))

# Type Conversion (Casting)

num = "10"

print(int(num))
print(float(num))
print(str(100))
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))

# Taking integer input
# age = int(input("Enter age: "))
# print(age + 1)

# Taking float input
# height = float(input("Enter height: "))

# f-Strings

name = "Krishna"
age = 20

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"Next year I will be {age + 1}.")
print(f"Uppercase: {name.upper()}")

pi = 3.14159265
print(f"Pi (2 decimal places): {pi:.2f}")

number = 7
print(f"Padded Number: {number:05}")

# Multiple Inputs (Very Important for DSA)

# a = int(input())
# b = int(input())

# a, b = map(int, input().split())

# Example:
# Input:
# 10 20
#
# input()          -> "10 20"
# .split()         -> ["10", "20"]
# map(int, ...)    -> 10, 20
# a = 10
# b = 20

# Common Mistakes

# Wrong
# age = input()
# print(age + 5)

# Correct
# age = int(input())
# print(age + 5)

# Wrong
# print("Age: " + 20)

# Correct
print("Age:", 20)
print(f"Age: {20}")

# DSA Examples

# Square of a number
# n = int(input())
# print(n * n)

# Greeting
# name = input()
# print(f"Welcome {name}")

# Sum of two numbers
# a, b = map(int, input().split())
# print(a + b)

# SHORT NOTES
# #
# ✔ print() displays output.
# ✔ input() always returns a string.
# ✔ Use int(), float(), str(), bool() for type conversion.
# ✔ Prefer f-strings for formatting.
# ✔ sep changes separator between printed values.
# ✔ end changes what print ends with.
# ✔ map(int, input().split()) is the standard DSA input style.
#
# Default values:
# sep = " "
# end = "\n"

# PRACTICE QUESTIONS

# 1. What does input() return?
# 2. Difference between print(a,b) and print(a+b)?
# 3. What are sep and end?
# 4. Why use int(input())?
# 5. Why are f-strings preferred?

# Predict the output:
#
# print("Python", "DSA")
# print("A", "B", sep="-")
# print("Hello", end=" ")
# print("World")
# print(bool(""))
# print(bool("0"))
# print(f"{7:04}")

