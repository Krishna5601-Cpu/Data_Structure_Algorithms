# Empty list
empty_list = []
empty_list2 = list()

# List with elements
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]  # Can mix types

# Using list() constructor
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']
range_list = list(range(5))  # [0, 1, 2, 3, 4]

# List repetition
zeros = [0] * 5  # [0, 0, 0, 0, 0]
repeated = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]

# List from other sequences
tuple_to_list = list((1, 2, 3))  # [1, 2, 3]
set_to_list = list({1, 2, 3})  # [1, 2, 3] (order may vary)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (forward)
print(fruits[0])  # 'apple'
print(fruits[2])  # 'cherry'
print(fruits[4])  # 'elderberry'

# Negative indexing (backward)
print(fruits[-1])  # 'elderberry'
print(fruits[-3])  # 'cherry'
print(fruits[-5])  # 'apple'

# Accessing nested lists
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested[0])  # [1, 2, 3]
print(nested[1][2])  # 6
print(nested[-1][-1])  # 9

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(numbers[2:7])  # [2, 3, 4, 5, 6]
print(numbers[:5])  # [0, 1, 2, 3, 4]
print(numbers[5:])  # [5, 6, 7, 8, 9]
print(numbers[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copy)

# Step parameter
print(numbers[::2])  # [0, 2, 4, 6, 8]
print(numbers[1:8:2])  # [1, 3, 5, 7]
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)

# Negative slicing
print(numbers[-5:-2])  # [5, 6, 7]
print(numbers[-3:])  # [7, 8, 9]
print(numbers[:-3])  # [0, 1, 2, 3, 4, 5, 6]

# Slicing with out-of-range indices
print(numbers[5:20])  # [5, 6, 7, 8, 9] (safe, no error)
print(numbers[20:30])  # [] (empty list)


# Creating nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing nested elements
print(matrix[0])  # [1, 2, 3]
print(matrix[0][0])  # 1
print(matrix[2][1])  # 8

# Creating a 3D list
three_d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(three_d[0][1][1])  # 4

# Modifying nested lists
matrix[1][1] = 99
print(matrix)  # [[1, 2, 3], [4, 99, 6], [7, 8, 9]]

# Creating nested lists with comprehensions
rows, cols = 3, 4
grid = [[0 for _ in range(cols)] for _ in range(rows)]
print(grid)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Beware of this common mistake
# Wrong way - creates references to same sublist
wrong_grid = [[0] * 4] * 3
wrong_grid[0][0] = 1
print(wrong_grid)  # [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]] - all rows affected!

# Right way - creates independent sublists
right_grid = [[0] * 4 for _ in range(3)]
right_grid[0][0] = 1
print(right_grid)  # [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

fruits = ["apple", "banana"]

# append() - adds to end
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'orange']

# insert() - adds at specific position
fruits.insert(1, "grape")
print(fruits)  # ['apple', 'grape', 'banana', 'orange']

# extend() - adds multiple elements
fruits.extend(["kiwi", "mango"])
print(fruits)  # ['apple', 'grape', 'banana', 'orange', 'kiwi', 'mango']

# Using + operator (creates new list)
more_fruits = fruits + ["peach", "pear"]
print(more_fruits)  # [... 'peach', 'pear']

# Using += operator (modifies original)
fruits += ["plum"]
print(fruits)  # [... 'plum']

fruits = ["apple", "banana", "cherry", "banana", "date"]

# remove() - removes first occurrence
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'banana', 'date']

# pop() - removes and returns last item (or specific index)
last = fruits.pop()
print(last)  # 'date'
print(fruits)  # ['apple', 'cherry', 'banana']

second = fruits.pop(1)
print(second)  # 'cherry'
print(fruits)  # ['apple', 'banana']

# del statement
del fruits[0]
print(fruits)  # ['banana']

# clear() - removes all elements
fruits.clear()
print(fruits)  # []


numbers = [1, 2, 3, 2, 4, 2, 5]

# index() - finds first occurrence
print(numbers.index(2))  # 1
print(numbers.index(2, 2))  # 3 (start searching from index 2)
# print(numbers.index(10))   # ValueError: 10 is not in list

# count() - counts occurrences
print(numbers.count(2))  # 3
print(numbers.count(10))  # 0

# in operator - membership testing
print(3 in numbers)  # True
print(10 in numbers)  # False

# Sorting and Reversing
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - sorts in place (modifies original)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# sorted() - returns new sorted list (doesn't modify original)
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 3, 4, 5]
print(numbers)  # [3, 1, 4, 1, 5] (unchanged)

# reverse() - reverses in place
numbers.reverse()
print(numbers)  # [5, 1, 4, 1, 3]

# Using slicing to reverse (creates new list)
reversed_list = numbers[::-1]


# copy() - shallow copy
original = [1, 2, [3, 4]]
copy = original.copy()
copy[0] = 99
copy[2][0] = 99
print(original)  # [1, 2, [99, 4]] - nested list affected
print(copy)  # [99, 2, [99, 4]]

# Deep copy (for nested structures)
import copy

deep_copy = copy.deepcopy(original)
deep_copy[2][0] = 100
print(original)  # [1, 2, [99, 4]] - unaffected

# len() - returns length
print(len([1, 2, 3, 4]))  # 4

# max(), min(), sum()
numbers = [1, 2, 3, 4, 5]
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sum(numbers) / len(numbers))  # Average: 3.0


# Basic: [expression for item in iterable]
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# With if-else
numbers = [x if x % 2 == 0 else -x for x in range(10)]
print(numbers)  # [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

# String manipulation
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Filtering with multiple conditions
numbers = range(50)
filtered = [x for x in numbers if x % 3 == 0 and x % 5 == 0]
print(filtered)  # [0, 15, 30, 45]

# Using set to remove duplicates
data = [1, 2, 2, 3, 3, 3, 4]
unique = [x for x in set(data)]
print(unique)  # [1, 2, 3, 4] (order may vary)

# Dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict_from_lists = {k: v for k, v in zip(keys, values)}
print(dict_from_lists)  # {'a': 1, 'b': 2, 'c': 3}

# Nested comprehension with condition
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transformed = [[x**2 if x % 2 == 0 else x**3 for x in row] for row in matrix]
print(transformed)  # [[1, 8, 27], [16, 125, 36], [343, 64, 729]]


# Basic unpacking
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # 1 2 3

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5

# Swapping variables
a, b = [1, 2]
a, b = b, a
print(a, b)  # 2 1

# Unpacking nested lists
nested = [1, [2, 3], 4]
a, [b, c], d = nested
print(a, b, c, d)  # 1 2 3 4

original = [1, 2, [3, 4]]

# Shallow copies
copy1 = original[:]  # Slicing
copy2 = original.copy()  # copy() method
copy3 = list(original)  # list() constructor
copy4 = copy.copy(original)  # copy module

# All are shallow - nested lists still referenced
copy1[2][0] = 99
print(original)  # [1, 2, [99, 4]] - affected!

# Deep copy (truly independent)
import copy

deep = copy.deepcopy(original)
deep[2][0] = 100
print(original)  # [1, 2, [99, 4]] - not affected

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Repetition
repeated = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]

# Membership
print(3 in [1, 2, 3])  # True
print(4 not in [1, 2, 3])  # True

# Comparison (lexicographic)
print([1, 2] < [1, 3])  # True
print([1, 2] == [1, 2])  # True
print([1, 2, 3] > [1, 2])  # True

# Zip - combine multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
pairs = list(zip(names, ages))
print(pairs)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Enumerate - get index and value
for i, fruit in enumerate(["apple", "banana", "cherry"]):
    print(f"{i}: {fruit}")
