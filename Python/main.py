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

a = 10
b = 20
print(a + b)

x = 5
y = 8
print(x + y)


def add(a, b):
    return a + b


print(add(10, 20))
print(add(5, 8))


def greet():
    print("Hello Krishna")


greet()


def add(x, y):  # Parameters
    return x + y


add(3, 5)  # Arguments


def square(n):
    return n * n


x = square(5)
print(x)


x = 100


def demo():
    x = 10
    print(x)


demo()
print(x)


def power(base, exp=2):
    return base**exp


print(power(5))
print(power(5, 3))


def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)


countdown(5)


def func(n):
    if n == 0:  # Base Case
        return

    func(n - 1)


def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)


def fun():
    return 10


print(fun())


def add(a, b):
    print(a + b)


x = add(3, 4)
print(x)


def f(n):
    if n == 0:
        return

    print(n)
    f(n - 1)


f(3)


def f(n):
    if n == 0:
        return

    f(n - 1)
    print(n)


f(4)


s = "Krishna"

print(s[0])
print(s[3])
print(s[-1])

s = "Krishna"

print(s[0:3])

s = "hello"

print(s[::-1])

s = "Krishna"

print(len(s))

s = "cat"

s = "b" + s[1:]

print(s)


for ch in s:
    print(ch)


for i in range(len(s)):
    print(i, s[i])


s = "banana"

count = 0

for ch in s:
    if ch == "a":
        count += 1

print(count)

arr = [10, 20, 30, 40]
nums = [1, 2, 3]
mixed = [10, "Krishna", True]

arr = [10, 20, 30]

print(arr[1])

arr[1] = 99

print(arr)

for num in arr:
    print(num)

for i in range(len(arr)):
    print(i, arr[i])

arr = [1, 2, 3]

arr.append(4)

print(arr)

arr = [5, 6, 7]

arr.pop()

print(arr)


arr.pop(1)


arr = [1, 3]

arr.insert(1, 2)

print(arr)

arr = [10, 20, 30]

arr.remove(20)

print(arr)


arr[::-1]

arr = [1, 2, 3, 4, 5]

print(arr[1:4])


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(grid[1][2])


arr = [5, 1, 8, 3]

len(arr)
max(arr)
min(arr)
sum(arr)
sorted(arr)

arr.sort()


# Dictionary - Hash Maps
student = {
    "Name": "Krishna",
    "Age": 20,
    "is_Student": True,
    "branch": "BCA",
}

print(student["Name"])

college = {}
college["name"] = "College hun"
college["location"] = "India"
college["course"] = ["BCA", "BTECH", "BBA"]


if "phone" in student:
    print("Exists")

print(student.get("phone"))

freq = {}

arr = [1, 2, 3, 45, 6, 78, 7, 6]

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1


print(freq)


for key in freq:
    print(key)


for value in freq.values():
    print(value)


for key, value in freq.items():
    print(key, value)


freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

        freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

# Sets

nums = {1, 2, 35, 6, 45}
print(nums)

nums = {1, 2, 2, 3, 3, 3}
print(nums)

s = {1, 2, 3, 4}

s.add(5)
s.add(6)
s.remove(3)

if 4 in s:
    print("Found")

arr = [1, 2, 2, 3, 1, 4]

onlyUnique = list(set(arr))
print(onlyUnique)

# Unique
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)

# Intersection
print(A & B)

print(A ^ B)

print(A - B)
