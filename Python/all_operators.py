"""
Python Operators Master Reference
Categories:
1. Arithmetic
2. Assignment (including Walrus operator)
3. Comparison (including chained comparisons)
4. Logical (and short-circuit behavior)
5. Bitwise
6. Identity vs. Equality
7. Membership
"""


def section(title: str) -> None:
    """Helper function to print formatted section headers."""
    print(f"\n{'=' * 50}")
    print(f" {title.upper()} ")
    print(f"{'=' * 50}")


# 1. ARITHMETIC OPERATORS
section("1. Arithmetic Operators")

a, b = 10, 3

print(f"Base values: a = {a}, b = {b}\n")
print(f"Addition (a + b):         {a + b}")
print(f"Subtraction (a - b):      {a - b}")
print(f"Multiplication (a * b):   {a * b}")
print(f"Division (a / b):         {a / b}")  # Always returns a float
print(f"Floor Division (a // b):  {a // b}")  # Rounds down to nearest integer
print(f"Modulo (a % b):           {a % b}")  # Remainder
print(f"Exponentiation (a ** b):  {a ** b}")

# Floor Division Nuance with negative numbers
print("\n-- Floor Division Nuance --")
print(f"-7 // 2 = {-7 // 2}  (Rounds down toward negative infinity, not -3)")


# 2. ASSIGNMENT OPERATORS
section("2. Assignment Operators")

x = 10
print(f"Initial x: {x}")

x += 5
print(f"x += 5  -> {x}")
x -= 2
print(f"x -= 2  -> {x}")
x *= 2
print(f"x *= 2  -> {x}")
x /= 4
print(f"x /= 4  -> {x}")
x //= 2
print(f"x //= 2 -> {x}")
x %= 2
print(f"x %= 2  -> {x}")

# Walrus Operator (:=) - Assigns and returns a value in-place
print("\n-- Walrus Operator (:=) --")
sample_data = [10, 20, 30, 40, 50]
if (data_len := len(sample_data)) > 3:
    print(f"Data length is {data_len}, which exceeds threshold.")


# 3. COMPARISON OPERATORS
section("3. Comparison Operators")

num1, num2 = 15, 20

print(f"Values: num1 = {num1}, num2 = {num2}\n")
print(f"num1 == num2 : {num1 == num2}")
print(f"num1 != num2 : {num1 != num2}")
print(f"num1 > num2  : {num1 > num2}")
print(f"num1 < num2  : {num1 < num2}")
print(f"num1 >= num2 : {num1 >= num2}")
print(f"num1 <= num2 : {num1 <= num2}")

# Chained Comparisons
print("\n-- Chained Comparisons --")
val = 15
print(f"Is 10 < {val} < 20? -> {10 < val < 20}")


# 4. LOGICAL OPERATORS
section("4. Logical Operators")

is_admin = True
has_token = False

print(f"is_admin = {is_admin}, has_token = {has_token}\n")
print(f"is_admin and has_token : {is_admin and has_token}")
print(f"is_admin or has_token  : {is_admin or has_token}")
print(f"not is_admin           : {not is_admin}")


# Short-Circuiting Example
def trigger_side_effect():
    print("WARNING: This function was executed!")
    return True


print("\n-- Short-Circuit Evaluation --")
print("Evaluating: False and trigger_side_effect()...")
result = False and trigger_side_effect()  # Function is NEVER called
print(f"Result: {result}")


# 5. BITWISE OPERATORS
section("5. Bitwise Operators")

p, q = 6, 3  # 6 = 0110 in binary, 3 = 0011 in binary

print(f"p = {p} ({bin(p)}), q = {q} ({bin(q)})\n")
print(f"Bitwise AND (p & q) : {p & q:<3} | Binary: {bin(p & q)}")
print(f"Bitwise OR  (p | q) : {p | q:<3} | Binary: {bin(p | q)}")
print(f"Bitwise XOR (p ^ q) : {p ^ q:<3} | Binary: {bin(p ^ q)}")
print(f"Bitwise NOT (~p)    : {~p:<3} | Binary: {bin(~p)} (Uses two's complement)")
print(f"Left Shift  (p << 1): {p << 1:<3} | Binary: {bin(p << 1)}")
print(f"Right Shift (p >> 1): {p >> 1:<3} | Binary: {bin(p >> 1)}")


# 6. IDENTITY OPERATORS
section("6. Identity Operators")

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(f"list_a: {list_a} (ID: {id(list_a)})")
print(f"list_b: {list_b} (ID: {id(list_b)})")
print(f"list_c: {list_c} (ID: {id(list_c)})\n")

print(f"list_a == list_b : {list_a == list_b}  (Equality: Same content)")
print(f"list_a is list_b : {list_a is list_b} (Identity: Different memory locations)")
print(f"list_a is list_c : {list_a is list_c}  (Identity: Same memory location)")
print(f"list_a is not list_b: {list_a is not list_b}")


# 7. MEMBERSHIP OPERATORS
section("7. Membership Operators")

tech_stack = ["Python", "FastAPI", "PostgreSQL", "Docker"]
user_profile = {"username": "coder123", "role": "developer"}

print(f"List: {tech_stack}")
print(f"'Python' in tech_stack     : {'Python' in tech_stack}")
print(f"'Java' not in tech_stack   : {'Java' not in tech_stack}")

print(f"\nDictionary: {user_profile}")
print(f"'username' in user_profile  : {'username' in user_profile}  (Checks keys)")
print(
    f"'coder123' in user_profile  : {'coder123' in user_profile} (Does NOT check values)"
)
print(f"'coder123' in user_profile.values() : {'coder123' in user_profile.values()}")
