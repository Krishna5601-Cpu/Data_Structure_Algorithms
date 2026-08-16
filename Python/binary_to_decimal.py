binary = int(input("Enter the binary number: "))

decimal = 0
base = 1

while binary > 0:
    digit = binary % 10

    # Input validation
    if digit != 0 and digit != 1:
        print("Invalid binary input!")
        exit(1)

    if digit == 1:
        decimal += base

    base *= 2
    binary //= 10

print(f"Decimal: {decimal}")
