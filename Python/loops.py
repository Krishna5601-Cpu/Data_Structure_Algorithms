# try:
#     num = int(input("Enter num: "))
# except TypeError:
#     print("Wrong input value")

# sum = 0

# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10

# print(f"Sum is: {sum}")

# sum = 0
# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0:
#         sum = sum + i

# print(sum)

# example = [4, 8, 10, 15, 9, 7, 14]

# for i in example:
#     if i % 2 == 0:
#         pass
#     else:
#         is_prime = True

#         if i <= 1:
#             is_prime = False
#         else:

#             for j in range(2, i):
#                 if i % j == 0:
#                     is_prime = False
#                     break

#         if is_prime:
#             print(f"First prime found: {i}")
#             break


# for i in range(1, 31):
#     if i % 4 == 0 or i % 10 == 7:
#         continue
#     print(i)

