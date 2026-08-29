def build_profile(name, role="Developer", *skills, **details):
    print(f"Name: {name} | Role: {role}")
    print(f"Skills: {skills}")  # Tuple
    print(f"Details: {details}")  # Dictionary


# Call with a mix of argument types
build_profile(
    "Alex",  # Positional
    "Lead Architect",  # Overrides default 'role'
    "Python",
    "Docker",  # Collected by *args
    location="Remote",  # Collected by **kwargs
    experience="8 years",  # Collected by **kwargs
)


# BAD: Shares the same list across calls
def add_item(item, target_list=[]): ...


# GOOD: Creates a new list instance per call
def add_item(item, target_list=None):
    if target_list is None:
        target_list = []


# Sorting a list of tuples by the second element
data = [("apple", 5), ("banana", 2), ("cherry", 8)]
sorted_data = sorted(data, key=lambda item: item[1])
# Result: [('banana', 2), ('apple', 5), ('cherry', 8)]


def factorial(n):
    # Base Case
    if n <= 1:
        return 1
    # Recursive Step
    return n * factorial(n - 1)


print(factorial(5))  # Output: 120
