name = "Krishna Singh Chauhan"
age = 20
is_student = True

print(name)

# Python -> Interpreter -> Bytecode -> Python Virtual Machine Code

# To run - python filename.py

# Single Line Comment

"""
Multiline
"""

if True:
    print("Okay")  # Indentation very important

    print("Hello World")

    name = "Krishna"
age = 20

print(name, age)

print("A", "B", "C", sep="-")

print("Hello", end=" ")
print("World")

print("=== CyberVault ===")

name = input("Enter your name: ")

print(f"Welcome {name}")

a = 17
b = 5

print(a % b)  # 2


n = 5
if n % 2 == 0:
    print("Even")

x = 10

print(x == 10)  # True
print(x != 5)  # True

age = 20
student = True

print(age >= 18 and student)

x = 5

x += 2
x -= 1
x *= 3
x //= 2

n = int(input())

a, b = map(int, input().split())

arr = list(map(int, input().split()))

n = int(input())
arr = list(map(int, input().split()))

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

    marks = 78

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

    age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible")

i = 1

while i <= 5:
    print(i)
    i += 1

for i in range(5):
    print(i)

for i in range(2, 8):
    print(i)

    arr = [10, 20, 30]

for num in arr:
    print(num)


for i, num in enumerate(arr):
    print(i, num)


for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(6):
    if i == 3:
        continue
    print(i)

arr = [1, 2, 3, 2, 2]

count = 0

for num in arr:
    if num == 2:
        count += 1

print(count)

