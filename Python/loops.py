try:
    num = int(input("Enter num: "))
except TypeError:
    print("Wrong input value")

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print(f"Sum is: {sum}")

