# def greet():
#     print("Hello Krishna: ")


# greet()  # Calling the function


# def greet_user(name):  # 'name' is the parameter
#     print(f"Hello, {name}!")


# greet_user("Krishna Jii")  # '"Alex"' is the argument


# def add(a, b):
#     return a + b


# result = add(5, 10)  # result holds 15
# print(result)


# x = "Global"  # Global variable


# def check_scope():
#     y = "Local"  # Local variable
#     print(x)  # Can read global variables
#     print(y)


# # check_scope()
# # print(y)  # Error! 'y' does not exist outside the function.


# def square(num):
#     return num * num


# sq = square(5)
# print(sq)

# print(square(6) + 5)

# def power(base, exponent = 2):
#     return base * exponent

# resultOfPower = power(3, 6)
# print(resultOfPower)

count = 0


def increment():
    count = 5
    return count


increment()
print(count)
