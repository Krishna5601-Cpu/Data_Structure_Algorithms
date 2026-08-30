name = "Krishna"

single_quoted = "Python"
double_quoted = "Python"
single_quoted = """Python"""
single_quoted = """Python"""

empty_string = ""

text = "Python"

# Positive indexing (left to right)
print(text[0])  # 'P'
print(text[1])  # 'y'
print(text[5])  # 'n'

# Negative indexing (right to left)
print(text[-1])  # 'n' (last character)
print(text[-2])  # 'o'
print(text[-6])  # 'P'

# Accessing out of range raises IndexError
# print(text[10])  # IndexError: string index out of range

text = "Python Programming"

# Basic slicing [start:end] (end is exclusive)
print(text[0:6])  # 'Python'
print(text[7:18])  # 'Programming'
print(text[:6])  # 'Python' (start defaults to 0)
print(text[7:])  # 'Programming' (end defaults to length)
print(text[:])  # Entire string

# Negative slicing
print(text[-11:-1])  # 'Programmin'
print(text[-11:])  # 'Programming'

# Step parameter
print(text[::2])  # 'Pto rgamn' (every 2nd character)
print(text[1:10:2])  # 'yhnP'
print(text[::-1])  # 'gnimmargorP nohtyP' (reverse string)

# Slicing with out-of-range indices (safe - no error)
print(text[0:100])  # Entire string
print(text[50:60])  # Empty string

text = "  Hello Python World  "

# Case manipulation
print(text.upper())  # '  HELLO PYTHON WORLD  '
print(text.lower())  # '  hello python world  '
print(text.title())  # '  Hello Python World  '
print(text.capitalize())  # '  hello python world  '
print(text.swapcase())  # '  hELLO pYTHON wORLD  '

# Whitespace removal
print(text.strip())  # 'Hello Python World'
print(text.lstrip())  # 'Hello Python World  '
print(text.rstrip())  # '  Hello Python World'

# Finding and replacing
print(text.find("Python"))  # 9 (returns index)
print(text.find("Java"))  # -1 (not found)
print(text.index("Python"))  # 9 (raises ValueError if not found)
print(text.replace("Python", "Java"))  # '  Hello Java World  '

# Counting
print(text.count("o"))  # 2
print(text.count("l"))  # 2

# Checking content
print(text.isalpha())  # False (has spaces)
print("Hello".isalpha())  # True
print("123".isdigit())  # True
print("Hello123".isalnum())  # True
print("   ".isspace())  # True
print("Hello".startswith("He"))  # True
print("World".endswith("ld"))  # True

# Splitting and joining
words = text.split()  # ['Hello', 'Python', 'World']
print(words)
print("-".join(words))  # 'Hello-Python-World'

# String formatting with methods
print(text.center(30, "*"))  # '***  Hello Python World  ***'
print(text.ljust(30, "-"))  # '  Hello Python World  ------'
print(text.rjust(30, "-"))  # '------  Hello Python World  '
print("Hello".zfill(10))  # '00000Hello'


text = "Hello"

# This will NOT work (uncomment to see error)
# text[0] = 'J'  # TypeError: 'str' object does not support item assignment

# Instead, create new strings
text = "J" + text[1:]  # Creates new string 'Jello'
print(text)  # 'Jello'

# Reassignment is fine
text = "Python"  # Points to new string object

# Example showing immutability
s1 = "Hello"
s2 = s1  # Both point to same string
s1 = "World"  # s1 now points to new string, s2 still "Hello"
print(s2)  # 'Hello'


name = "Alice"
age = 30
height = 5.6

# Basic f-string
print(f"Name: {name}, Age: {age}, Height: {height}")

# Formatting numbers
print(f"Age: {age:03d}")  # 'Age: 030'
print(f"Height: {height:.2f}")  # 'Height: 5.60'
print(f"Percentage: {0.25:.1%}")  # 'Percentage: 25.0%'

# Expressions inside braces
print(f"Next year you'll be {age + 1}")
print(f"Name length: {len(name)}")

# Dictionary and attributes
person = {"name": "Bob", "age": 25}
print(f"Person: {person['name']} is {person['age']}")

name = "Alice"
age = 30

# Positional arguments
print("Name: {}, Age: {}".format(name, age))

# Indexed arguments
print("Name: {0}, Age: {1}".format(name, age))

# Named arguments
print("Name: {n}, Age: {a}".format(n=name, a=age))

# Formatting numbers
print("Pi: {:.2f}".format(3.14159))  # 'Pi: 3.14'
print("Hex: {:x}".format(255))  # 'Hex: ff'
print("Binary: {:b}".format(10))  # 'Binary: 1010'

# Common escape sequences
print("Hello\nWorld")  # Newline
print("Hello\tWorld")  # Tab
print("Hello\\World")  # Backslash
print('Hello"World"')  # Double quote
print("Hello'World'")  # Single quote
print("Hello\bWorld")  # Backspace (deletes one char)
print("Hello\rWorld")  # Carriage return (overwrites)

# Raw strings (ignore escape characters)
print(r"Hello\nWorld")  # 'Hello\nWorld'
print(r"C:\Users\Name")  # 'C:\Users\Name'

# Unicode characters
print("\u03a9")  # Ω (Omega)
print("\u2605")  # ★ (Star)
print("\U0001f600")  # 😀 (Emoji)


# Membership testing
print("Py" in "Python")  # True
print("Java" not in "Python")  # True

# String concatenation and multiplication
print("Hello" + " " + "World")  # 'Hello World'
print("-" * 20)  # '--------------------'

# Comparing strings (lexicographic)
print("apple" < "banana")  # True (a < b)
print("Python" > "python")  # True (P > p in ASCII)

# Length
print(len("Python"))  # 6

# Converting other types to string
print(str(123))  # '123'
print(str(3.14))  # '3.14'
print(str(True))  # 'True'
print(str(None))  # 'None'


# Password validation
def validate_password(password):
    import string

    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    return all([has_upper, has_lower, has_digit, has_special, len(password) >= 8])


print(validate_password("Pass123!"))  # True


# Email validation (simple)
def validate_email(email):
    return "@" in email and "." in email and email.count("@") == 1


print(validate_email("user@example.com"))  # True

# Text processing
text = "The quick brown fox jumps over the lazy dog"
words = text.split()
print(f"Word count: {len(words)}")
print(f"Uppercase: {text.upper()}")
print(f"Reversed words: {' '.join(words[::-1])}")

# URL slug generator
title = "Python String Tutorial!"
slug = title.lower().replace(" ", "-").strip("!")
print(slug)  # 'python-string-tutorial'

# Character counting
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
