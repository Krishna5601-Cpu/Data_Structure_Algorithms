def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter the operation (+, -, *, /, %): ")

        if op == '+':
            print(f"{a} + {b} = {a + b}")
        elif op == '-':
            print(f"{a} - {b} = {a - b}")
        elif op == '*':
            print(f"{a} * {b} = {a * b}")
        elif op == '/':
            if b == 0:
                print("Error: Division by zero is not allowed!")
            else:
                print(f"{a} / {b} = {a / b}")
        elif op == '%':
            if b == 0:
                print("Error: Modulus by zero is not allowed!")
            else:
                print(f"{int(a)} % {int(b)} = {int(a) % int(b)}")
        else:
            print("Invalid Input! Please use +, -, *, /, or %")
    
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    calculator()